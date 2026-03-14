# AWS Event-Driven EC2 Automation with Monitoring

This project demonstrates an **event-driven cloud automation system** using AWS services.

When a file is uploaded to an S3 bucket, a Lambda function is triggered that starts an EC2 instance automatically. The system also monitors failures and sends email alerts.

---

## AWS Services Used

- Amazon S3
- AWS Lambda
- Amazon EC2
- Amazon CloudWatch
- Amazon SNS
---

## Features

- Event-driven automation
- EC2 instance start triggered by S3 upload
- Lambda environment variables for configuration
- CloudWatch monitoring and logging
- Failure alerts via email using SNS
- Use of Lambda Layers for external libraries
- Audit tracking using CloudTrail

---

## Workflow

1. File uploaded to S3 bucket
2. S3 triggers Lambda function
3. Lambda starts EC2 instance
4. CloudWatch logs Lambda execution
5. CloudWatch alarm detects errors
6. SNS sends email notification if failure occurs

---

## Lambda Function

```python
import boto3
import logging
import os

ec2 = boto3.client('ec2')

INSTANCE_ID = os.environ['EC2_INSTANCE_ID']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    try:
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']

        logger.info(f"File {file_key} uploaded to {bucket_name}")

        response = ec2.start_instances(
            InstanceIds=[INSTANCE_ID]
        )

        logger.info(response)

    except Exception as e:
        logger.error(str(e))
        raise e
