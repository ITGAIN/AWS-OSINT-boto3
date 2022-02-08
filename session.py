import boto3
import os

key = os.environ['aws_key']
secret = os.environ['aws_secret']

session = boto3.session.Session(
        aws_access_key_id=key,
        aws_secret_access_key=secret,
        region_name="eu-central-1"
        )

response = session.get_available_resources()

print(response)
