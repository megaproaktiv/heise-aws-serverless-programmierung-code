import boto3
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')

def get_buckets():
    try:
        buckets = list(s3.buckets.all())
    except ClientError:
        print("Couldn't get buckets.")
        raise
    else:
        return buckets

def count_buckets():
    count = 0
    buckets = [b for b in get_buckets()]
    for bucket in buckets:
        print(f"Got bucket {bucket.name}.")
        count = count+1
    return count
