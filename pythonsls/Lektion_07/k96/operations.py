import boto3
from botocore.exceptions import ClientError

ERROR_HELP_STRINGS = {
    # Operation specific errors
    'ConditionalCheckFailedException': 'Condition check specified in the operation failed, review and update the condition check before retrying',
    'TransactionConflictException': 'Operation was rejected because there is an ongoing transaction for the item, generally safe to retry with exponential back-off',
    'ItemCollectionSizeLimitExceededException': 'An item collection is too large, you\'re using Local Secondary Index and exceeded size limit of items per partition key.' +
                                                ' Consider using Global Secondary Index instead',
    # Common Errors
    'InternalServerError': 'Internal Server Error, generally safe to retry with exponential back-off',
    'ProvisionedThroughputExceededException': 'Request rate is too high. If you\'re using a custom retry strategy make sure to retry with exponential back-off.' +
                                              'Otherwise consider reducing frequency of requests or increasing provisioned capacity for your table or secondary index',
    'ResourceNotFoundException': 'One of the tables was not found, verify table exists before retrying',
    'ServiceUnavailable': 'Had trouble reaching DynamoDB. generally safe to retry with exponential back-off',
    'ThrottlingException': 'Request denied due to throttling, generally safe to retry with exponential back-off',
    'UnrecognizedClientException': 'The request signature is incorrect most likely due to an invalid AWS access key ID or secret key, fix before retrying',
    'ValidationException': 'The input fails to satisfy the constraints specified by DynamoDB, fix input before retrying',
    'RequestLimitExceeded': 'Throughput exceeds the current throughput limit for your account, increase account level throughput before retrying',
}


def max(response):
    # Return Structure
    # gramm: 100
    # uid: 1
    # date: 2020-12-30
    max = { 'gramm': 0,
            'uid': "0",
            'date': "1937-12-30"}
    
    for item in response.get('Items', []):
        current_weight = max['gramm']
        

        item_weight = item['gramm']['N']
        item_weight = int(item_weight)

        if  item_weight > current_weight:
            max['gramm'] = item_weight
            max['uid'] = item['userID']['S']
            max['date'] = item['date']['S']
        
    return max

def put_weight(uid, day, weight):
    dynamodb_client = create_dynamodb_client(region="eu-central-1")
    put_item_input = create_put_item_input_weight(uid,day,weight)

    # Call DynamoDB's put_item API
    execute_put_item(dynamodb_client, put_item_input)

def create_dynamodb_client(region="eu-central-1"):
    return boto3.client("dynamodb", region_name=region)    

# Hier würde ein Test gut passen
def create_put_item_input_weight(uid,day,weight):
    id=uid+"#"+day
    return {
        "TableName": "daily-weight",
        "Item": {
            "id": {"S": id},
            "uid": {"S": uid},
            "day": {"S": day},
            "hectogramm": { "N": str(weight)}
        }
    }


# ----------------------------------------
# funktionen für alle DynamoDB Operationen
# ----------------------------------------
def execute_put_item(dynamodb_client, input):
    try:
        response = dynamodb_client.put_item(**input)
        print("Successfully put item.")
        # Handle response
    except ClientError as error:
        handle_error(error)
    except BaseException as error:
        print("Unknown error while putting item: " + error.response['Error']['Message'])


def handle_error(error):
    error_code = error.response['Error']['Code']
    error_message = error.response['Error']['Message']

    error_help_string = ERROR_HELP_STRINGS[error_code]

    print('[{error_code}] {help_string}. Error message: {error_message}'
          .format(error_code=error_code,
                  help_string=error_help_string,
                  error_message=error_message))

