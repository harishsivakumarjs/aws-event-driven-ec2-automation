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

        logger.info(f"EC2 start response: {response}")

        return {
            "statusCode": 200,
            "body": "EC2 instance starting"
        }

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise e
