provider "aws" {
  region = "us-east-1"  
}

# SNS Topic to send car wash reminders
resource "aws_sns_topic" "car_wash_reminder" {
  name = "CarWashReminder"
}

# SNS Phone Subscription for Friend 1
resource "aws_sns_topic_subscription" "phone_subscription" {
  topic_arn = aws_sns_topic.car_wash_reminder.arn
  protocol  = "sms"
  endpoint  = "+16479068124"  # Replace with actual phone number
}

# SNS Phone Subscription for Friend 2
resource "aws_sns_topic_subscription" "phone_subscription_2" {
  topic_arn = aws_sns_topic.car_wash_reminder.arn
  protocol  = "sms"
  endpoint  = "+16474823342"  # Replace with actual phone number
}

# SNS Phone Subscription for Friend 3
resource "aws_sns_topic_subscription" "phone_subscription3" {
  topic_arn = aws_sns_topic.car_wash_reminder.arn
  protocol  = "sms"
  endpoint  = "+16475755209"  # Replace with actual phone number
}

# SNS Phone Subscription for Friend 4
resource "aws_sns_topic_subscription" "phone_subscription_4" {
  topic_arn = aws_sns_topic.car_wash_reminder.arn
  protocol  = "sms"
  endpoint  = "+14169030097"  # Replace with actual phone number
}

# Attach existing IAM role for Lambda function with permissions to publish to SNS
resource "aws_lambda_function" "car_wash_reminder_function" {
  filename         = "lambda_function.zip"  # Path to the zipped Lambda function
  function_name    = "CarWashReminderFunction"
  role             = "arn:aws:iam::211125457564:role/service-role/aa.CarWash"  # Use the existing IAM role ARN
  handler          = "lambda_function.lambda_handler"  # Correct handler reference for Python
  runtime          = "python3.8"
  source_code_hash = filebase64sha256("lambda_function.zip")  # Ensure this is correct

  environment {
    variables = {
      SNS_TOPIC_ARN = aws_sns_topic.car_wash_reminder.arn
    }
  }
}

# CloudWatch Event Rule to trigger Lambda function every day
resource "aws_cloudwatch_event_rule" "daily_trigger" {
  name                = "DailyCarWashReminderTrigger"
#   schedule_expression = "rate(1 day)"  # Trigger every day
    schedule_expression = "cron(0 18 * * ? *)"  # Trigger every day at 6 PM UTC

  description = "Triggers the Lambda function to send a car wash reminder"
}

# CloudWatch Event Target to call Lambda function
resource "aws_cloudwatch_event_target" "lambda_target" {
  rule      = aws_cloudwatch_event_rule.daily_trigger.name
  arn       = aws_lambda_function.car_wash_reminder_function.arn
  target_id = "carWashReminderFunctionTarget"
}

# Grant CloudWatch permission to invoke Lambda function
resource "aws_lambda_permission" "allow_cloudwatch_to_invoke_lambda" {
  statement_id  = "AllowCloudWatchToInvokeLambda"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.car_wash_reminder_function.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.daily_trigger.arn
}
