import boto3
import os

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

def download_index(bucket: str, key: str, local_path: str):
    s3.download_file(bucket, key, local_path)

def upload_index(local_path: str, bucket: str, key: str):
    s3.upload_file(local_path, bucket, key)
