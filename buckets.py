import boto3

key = ""
secret = ""

s3 = boto3.client('s3',
        aws_access_key_id=key,
        aws_secret_access_key=secret)

response = s3.list_buckets()

for bucket in response['Buckets']:
    print(f'{bucket["Name"]}')
