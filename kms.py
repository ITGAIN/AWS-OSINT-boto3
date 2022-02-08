import boto3
import os

key = os.environ['aws_key']
secret = os.environ['aws_secret']

kms = boto3.client('kms',
        aws_access_key_id=key,
        aws_secret_access_key=secret)

response = kms.list_keys()

print(response)
