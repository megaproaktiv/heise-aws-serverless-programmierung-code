
def handler(event, context):
    print(event['key1'])
    return {
        'statusCode': 200,
        'body': event['key1']
    }


