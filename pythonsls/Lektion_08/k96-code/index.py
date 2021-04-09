import operations
import datetime


def handler(event, context):
    now = datetime.datetime.now()
    today = now.strftime('%Y-%m-%d')
    client = operations.create_dynamodb_client(region="eu-central-1")
    scan_input = operations.create_scan_input(today)
    response = operations.execute_scan(client,scan_input)

    max_weight = operations.max(response)
    ## Im Moment verwenden wir nur einen User mit der ID 1
    operations.put_weight("1",today, max_weight['gramm'])

    return {
        'statusCode': 200,
        'body': "Weight: "+today+str(max_weight)
    }


