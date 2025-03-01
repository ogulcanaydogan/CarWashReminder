import boto3
import datetime

sns_client = boto3.client('sns', region_name='us-east-1')  # Ensure region is correct

# SNS Subscription ARNs for each friend
sns_subscription_arns = {
    "Ziya": "arn:aws:sns:us-east-1:211125457564:CarWashReminder:92dc4f1a-3ca5-4009-b918-50f4c370b403",
    "Omer": "arn:aws:sns:us-east-1:211125457564:CarWashReminder:57e4c29a-26cb-4c9f-9d26-10b1114d9dc3",
    "Ogulcan": "arn:aws:sns:us-east-1:211125457564:CarWashReminder:a77c881f-f877-461d-8aa2-8ca7e5d010e",
    "Mesut": "arn:aws:sns:us-east-1:211125457564:CarWashReminder:b7cbca87-0676-4733-852c-9aacaefa864f"
}

# List of friends' names in order
friends = ["Ziya", "Omer", "Ogulcan", "Mesut"]

# Set the start and end dates
start_date = datetime.datetime(2025, 1, 28)  # Set your actual start date
end_date = datetime.datetime(2025, 3, 31)  # Set your actual end date

# Calculate the total days between start and end date
total_days = (end_date - start_date).days

# Define the mapping of days to friends
def get_friend_for_day(day):
    """Returns the friend to be reminded on a specific day"""
    return friends[(day - 1) % len(friends)]  # Assign each friend to a specific day in a cycle

def lambda_handler(event, context):
    # Get the current date
    today = datetime.datetime.now()

    # Calculate how many days have passed since the start date
    days_elapsed = (today - start_date).days

    # Ensure the days_elapsed is within the range of start and end dates
    if today > end_date:
        # If the end date has passed, stop the service and send a final notification
        message = "The car wash reminder service has ended. Thank you for participating!"

        # Unsubscribe from all SNS subscriptions if the date has passed
        for subscription_arn in sns_subscription_arns.values():
            sns_client.unsubscribe(SubscriptionArn=subscription_arn)
            print(f"Unsubscribed from {subscription_arn}")

        sns_client.publish(
            TopicArn="arn:aws:sns:us-east-1:211125457564:CarWashReminder",  # Correct ARN
            Message=message,
            Subject='Car Wash Service Ended'
        )
        print("Service ended, no more reminders will be sent.")
    elif days_elapsed <= 0:
        # If the days_elapsed is 0 or negative, it means we're out of the scheduled date range
        print("Today is out of the scheduled date range.")
        
        # Unsubscribe from all SNS services (SMS and Email)
        for subscription_arn in sns_subscription_arns.values():
            sns_client.unsubscribe(SubscriptionArn=subscription_arn)
            print(f"Unsubscribed from {subscription_arn}")
    else:
        # Get the friend for the current day
        selected_friend = get_friend_for_day(days_elapsed + 1)  # Day 1 should be Ziya, etc.

        # Get the subscription ARN for the selected friend
        subscription_arn = sns_subscription_arns[selected_friend]

        # Prepare the reminder message
        message = f"Reminder: It's {selected_friend}'s turn to wash the car today!"

        # Send the message via SNS to the selected friend's ARN
        sns_client.publish(
            TopicArn=subscription_arn,  # Use the specific ARN for that person
            Message=message,
            Subject='Car Wash Reminder'
        )

        print(f"Reminder sent to {selected_friend}.")
