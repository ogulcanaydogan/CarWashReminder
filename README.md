
# CarWashReminder

**CarWashReminder** is an AWS-based solution that automates car wash reminders using AWS Lambda, Amazon SNS, and CloudWatch. The system sends daily reminders to a group of friends for their assigned car wash day. The schedule is cyclic, and the system automatically unsubscribes from notifications once the scheduled period ends.

## Features

- **Automated Car Wash Reminders**: Sends daily notifications to the person assigned to wash the car.
- **SNS Notifications**: Uses Amazon SNS to deliver reminders via SMS or email.
- **Customizable Schedule**: The system uses a rotating schedule where each friend is assigned a specific day in a repeating 4-day cycle.
- **Automatic Unsubscription**: Unsubscribes users from reminders after the scheduled period has ended.

## Workflow

1. **Rotation of Reminders**:
   - Day 1: Ziya
   - Day 2: Omer
   - Day 3: Ogulcan
   - Day 4: Mesut
   - The cycle repeats after Day 4.
   
2. **Unsubscribing**:
   - Once the **scheduled period** ends (based on the configured start and end date), the system automatically unsubscribes all users from SNS.

## Prerequisites

Before deploying the solution, you’ll need:

- **AWS Account** with access to **AWS Lambda**, **SNS**, **CloudWatch**, and **IAM**.
- **SNS Subscription ARNs** for each user (SMS/Email).
- **Terraform** to provision the necessary AWS resources.

## Getting Started

### 1. Clone the Repository

Start by cloning the repository:

```bash
git clone https://github.com/ogulcanaydogan/CarWashReminder.git
cd CarWashReminder
```

### 2. Configure AWS CLI

Ensure that your AWS CLI is configured with the appropriate credentials:

```bash
aws configure
```

### 3. Deploy Infrastructure with Terraform

The solution uses **Terraform** to provision the necessary AWS resources such as **SNS**, **Lambda**, and **CloudWatch Events**.

- **Initialize Terraform**:

```bash
terraform init
```

- **Plan the Terraform deployment**:

```bash
terraform plan
```

- **Apply the Terraform configuration**:

```bash
terraform apply
```

This will set up the **SNS Topic**, **Lambda Function**, and **CloudWatch Event Rule**.

### 4. Update SNS Subscription ARNs

In the `lambda_function.py` file, you'll need to replace the **SNS Subscription ARNs** with the actual subscription ARNs for your users.

Example SNS Subscription ARNs for each user:
- **Ziya**: `arn:aws:sns:us-east-1:211125457564:CarWashReminder:92dc4f1a-3ca5-4009-b918-50f4c370b403`
- **Omer**: `arn:aws:sns:us-east-1:211125457564:CarWashReminder:57e4c29a-26cb-4c9f-9d26-10b1114d9dc3`
- **Ogulcan**: `arn:aws:sns:us-east-1:211125457564:CarWashReminder:a77c881f-f877-461d-8aa2-8ca7e5d010e`
- **Mesut**: `arn:aws:sns:us-east-1:211125457564:CarWashReminder:b7cbca87-0676-4733-852c-9aacaefa864f`

### 5. Upload the Lambda Function

The **Lambda function** is written in **Python** and deployed as a **ZIP file**. Ensure the file `lambda_function.zip` is ready and properly uploaded to Lambda.

```bash
zip lambda_function.zip lambda_function.py
```

Upload this zip file to the **Lambda function** in the AWS Console.

### 6. Test the Lambda Function

You can manually trigger the Lambda function from the **AWS Lambda Console** using a **test event** (e.g., `{}`). Check **CloudWatch Logs** to ensure the function works as expected.

### 7. Monitor SNS Subscriptions

Check that the **SNS subscription** for each person is correctly confirmed and that the reminders are being sent as expected.

You can manage the SNS subscriptions via the **SNS Console**.

## Example SNS Subscription ARN

Here are the **SNS Subscription ARNs** for each person:
- **Ziya**: `arn:aws:sns:us-east-1:211125457564:CarWashReminder:92dc4f1a-3ca5-4009-b918-50f4c370b403`
- **Omer**: `arn:aws:sns:us-east-1:211125457564:CarWashReminder:57e4c29a-26cb-4c9f-9d26-10b1114d9dc3`
- **Ogulcan**: `arn:aws:sns:us-east-1:211125457564:CarWashReminder:a77c881f-f877-461d-8aa2-8ca7e5d010e`
- **Mesut**: `arn:aws:sns:us-east-1:211125457564:CarWashReminder:b7cbca87-0676-4733-852c-9aacaefa864f`

## Troubleshooting

- **No notifications sent**: Ensure the **SNS subscription** is confirmed (check email for email subscriptions and verify phone numbers for SMS).
- **Incorrect notifications**: Double-check the `days_elapsed` logic and ensure the correct person is selected for the given day.
- **Unsubscription issues**: Make sure the subscription ARNs are valid and correctly listed in the Lambda code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- AWS for providing the infrastructure tools to build serverless applications.
- Terraform for automating the deployment of AWS infrastructure.

