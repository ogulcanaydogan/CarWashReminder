import boto3
import datetime

sns_client = boto3.client('sns')

# List of friends' names in order
friends = ["Ziya", "Omer", "Ogulcan", "Mesut"]

# Set the start and end dates
start_date = datetime.datetime(2025, 1, 28)  # Set your actual start date
end_date = datetime.datetime(2025, 3, 31)  # Set your actual end date

# Calculate the total days between start and end date
total_days = (end_date - start_date).days

def lambda_handler(event, context):
    # Get the current date
    today = datetime.datetime.now()

    # Calculate how many days have passed since the start date
    days_elapsed = (today - start_date).days

    # Ensure the days_elapsed is within the range of start and end dates
    if today > end_date:
        # If the end date has passed, stop the service and send a final notification
        message = "The car wash reminder service has ended. Thank you for participating!"
        sns_client.publish(
            TopicArn="arn:aws:sns:your-region:your-account-id:CarWashReminder",  # Use your actual ARN
            Message=message,
            Subject='Car Wash Service Ended'
        )
        print("Service ended, no more reminders will be sent.")
    else:
        if days_elapsed <= 0:
            print("Today is out of the scheduled date range.")
        else:
            # Select the friend based on the days_elapsed
            selected_friend = friends[days_elapsed % len(friends)]

            # Prepare the reminder message
            message = f"Reminder: It's {selected_friend}'s turn to wash the car today!"

            # Send the message via SNS to email and phone
            sns_client.publish(
                TopicArn="arn:aws:sns:your-region:your-account-id:CarWashReminder",  # Use your actual ARN
                Message=message,
                Subject='Car Wash Reminder'
            )

            print(f"Reminder sent to {selected_friend}.")
