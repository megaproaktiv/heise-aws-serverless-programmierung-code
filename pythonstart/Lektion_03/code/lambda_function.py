import json
import extract

def lambda_handler(event, context):
    # TODO implement
    print(extract.extractKey(event))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

