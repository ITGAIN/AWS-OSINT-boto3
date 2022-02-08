import boto3

key = ""
secret = ""

ec2 = boto3.client('ec2',
        aws_access_key_id=key,
        aws_secret_access_key=secret)

response = ec2.describe_instances()
print(response)
