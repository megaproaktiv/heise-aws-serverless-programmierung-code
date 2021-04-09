import json
import s3list

def lambda_handler(event, context):
    # TODO implement
    print(s3list.count_buckets())
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

