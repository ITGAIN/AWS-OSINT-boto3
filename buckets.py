# Example for bucket

import boto3
import os

key = os.environ['aws_key']
secret = os.environ['aws_secret']

s3 = boto3.client('s3',
        aws_access_key_id=key,
        aws_secret_access_key=secret)

response = s3.list_buckets()

for bucket in response['Buckets']:
    print(f'{bucket["Name"]}')
