import boto3

s3 = boto3.client('s3',
        aws_access_key_id="",
        aws_secret_access_key="",
        region="")

response = s3.list_buckets()

for bucket in response['Buckets']:
    print(f'{bucket["Name"]}')
