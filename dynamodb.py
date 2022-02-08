import boto3
import os

key = os.environ['aws_key']
secret = os.environ['aws_secret']

db = boto3.client('dynamodb',
        aws_access_key_id=key,
        aws_secret_access_key=secret,
        )

response = db.list_tables()

print(response)
