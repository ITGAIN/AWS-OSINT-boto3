# Example for ec2
import boto3
import os

key = os.environ['aws_key']
secret = os.environ['aws_secret']

ec2 = boto3.client('ec2',
        aws_access_key_id=key,
        aws_secret_access_key=secret)

response = ec2.describe_instances()
print(response)
