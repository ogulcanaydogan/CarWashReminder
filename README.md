# CarWashReminder

A simple AWS Lambda function that sends daily reminders to different people for their turn to wash the car. The reminders are sent via **Amazon SNS** and can be delivered through **SMS** or **Email**.

The reminders are scheduled to rotate through a group of friends (Ziya, Omer, Ogulcan, and Mesut). The cycle repeats every 4 days, and only the person assigned to that day receives the reminder.

## Features

- **Automated reminders**: Sends daily reminders for car washing.
- **SNS-based notifications**: Sends notifications via SMS and Email using Amazon SNS.
- **Customizable reminder schedule**: Customize the rotation of who gets the reminder each day.
- **End-date handling**: Automatically unsubscribes from SNS when the scheduled date range ends.

## Workflow

1. **Car Wash Rotation**: The function assigns each person to a specific day in a repeating cycle:
    - Day 1: Ziya
    - Day 2: Omer
    - Day 3: Ogulcan
    - Day 4: Mesut
    - After Day 4, the cycle repeats from Ziya.
   
2. **Notifications**: The function sends a reminder via Amazon SNS to the correct person based on the day of the cycle.

3. **Subscription Management**: The Lambda function automatically unsubscribes all SNS subscriptions when the scheduled date range is over.

## Prerequisites

- An **AWS account** with access to **AWS Lambda**, **Amazon SNS**, and **AWS CloudWatch**.
- The **SNS Subscription ARNs** for each person (to receive SMS or Email notifications).
- **Terraform** installed to deploy infrastructure.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ogulcanaydogan/CarWashReminder.git
cd CarWashReminder

2. Set up AWS Resources using Terraform
This project uses Terraform to provision the necessary AWS resources such as SNS topics, Lambda functions, and CloudWatch events.

Configure AWS CLI: Make sure your AWS credentials are configured using the AWS CLI.
bash
Copy
aws configure
Run Terraform commands:
bash
Copy
terraform init  # Initialize Terraform
terraform plan  # Preview the changes
terraform apply # Apply the changes and create AWS resources
This will create the necessary SNS topic, subscriptions, and Lambda function, as well as set up a CloudWatch event to trigger the Lambda function daily.

3. Deploy Lambda Function
The Lambda function is written in Python and deployed as a ZIP file.

Ensure the Lambda function code is correctly zipped as lambda_function.zip.
The Lambda function is triggered daily by CloudWatch Events.
4. SNS Subscription ARNs
Update the sns_subscription_arns in the Lambda function code with the actual Subscription ARNs of the users. You can find these ARNs in the SNS Console for each subscription.

5. Test the Lambda Function
You can manually test the Lambda function in the AWS Lambda Console by creating a simple test event (e.g., {}). Check the CloudWatch logs to verify that the correct person receives the reminder.

6. Unsubscribe Logic
If the end date of the scheduled period is passed, the Lambda function will automatically unsubscribe from the SNS topic to prevent further notifications.

Example SNS Subscription ARN
Here are the SNS Subscription ARNs for each person:

Ziya: arn:aws:sns:us-east-1:211125457564:CarWashReminder:92dc4f1a-3ca5-4009-b918-50f4c370b403
Omer: arn:aws:sns:us-east-1:211125457564:CarWashReminder:57e4c29a-26cb-4c9f-9d26-10b1114d9dc3
Ogulcan: arn:aws:sns:us-east-1:211125457564:CarWashReminder:a77c881f-f877-461d-8aa2-8ca7e5d010e
Mesut: arn:aws:sns:us-east-1:211125457564:CarWashReminder:b7cbca87-0676-4733-852c-9aacaefa864f
Replace these ARNs in the sns_subscription_arns dictionary in the code to ensure that notifications are sent to the correct person.

Troubleshooting
No notifications sent: Make sure the SNS subscription is correctly confirmed (check for confirmation emails for email subscriptions, and ensure phone numbers are properly subscribed).
Incorrect notifications: Verify that the days elapsed logic is correctly calculating the current day and selecting the appropriate person.
Subscription issues: Ensure the Subscription ARNs are accurate and valid.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to AWS for providing the tools for serverless computing.
Thanks to Terraform for making infrastructure management easier.


### Explanation of the README:
1. **Overview**: Describes the purpose and functionality of the project (a car wash reminder system using AWS services).
2. **Features**: Lists the key features of the Lambda function (automated reminders, SNS notifications, etc.).
3. **Getting Started**: Provides instructions for cloning the repository, setting up AWS resources using Terraform, and deploying the Lambda function.
4. **SNS Subscription ARNs**: Explains where to find and update the SNS Subscription ARNs for the users.
5. **Example SNS ARNs**: Shows example SNS Subscription ARNs for each friend.
6. **Troubleshooting**: Offers solutions to common issues like missed notifications or incorrect logic.
7. **License**: Indicates that the project is licensed under the MIT License.

Let me know if you need more details or adjustments!
