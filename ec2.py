import boto3
import os

#aws_access_key_id = AKIAVF46BXA33KWOJENT
#aws_secret_access_key = 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

key = os.environ['aws_key']
secret = os.environ['aws_secret']

ec2 = boto3.client('ec2',
        aws_access_key_id=key,
        aws_secret_access_key=secret)

response = ec2.describe_instances()
print(response)
