
# Load the AWS SDK for Python
import boto3
from botocore.exceptions import ClientError
import operations

ERROR_HELP_STRINGS = {
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

# Use the following function instead when using DynamoDB Local
#def create_dynamodb_client(region):
#    return boto3.client("dynamodb", region_name="localhost", endpoint_url="http://localhost:8000", aws_access_key_id="access_key_id", aws_secret_access_key="secret_access_key")

def create_dynamodb_client(region="us-east-1"):
    return boto3.client("dynamodb", region_name=region)


def create_scan_input():
    return {
        "TableName": "Weigh-rmzevapjnnfmtob77w4mwegpia-dev",
        "FilterExpression": "#93f40 = :93f40 And #93f41 = :93f41",
        "ExpressionAttributeNames": {"#93f40":"userID","#93f41":"date"},
        "ExpressionAttributeValues": {":93f40": {"S":"1"},":93f41": {"S":"2021-03-06"}}
    }


def execute_scan(dynamodb_client, input):
    try:
        response = dynamodb_client.scan(**input)
        # Handle response
    except ClientError as error:
        handle_error(error)
    except BaseException as error:
        print("Unknown error while scanning: " + error.response['Error']['Message'])
    return (response.get('Items', []))


def handle_error(error):
    error_code = error.response['Error']['Code']
    error_message = error.response['Error']['Message']

    error_help_string = ERROR_HELP_STRINGS[error_code]

    print('[{error_code}] {help_string}. Error message: {error_message}'
          .format(error_code=error_code,
                  help_string=error_help_string,
                  error_message=error_message))

# Custom code
def print_items(weights):
    print(weights)
    for item in weights:
        print(f"\n{item['date']} : {item['gramm']} : {item['userID']}")

def main():
    # Create the DynamoDB Client with the region you want
    dynamodb_client = create_dynamodb_client(region="eu-central-1")

    # Create the dictionary containing arguments for scan call
    scan_input = create_scan_input()

    # Call DynamoDB's scan API
    scan_output=execute_scan(dynamodb_client, scan_input)
    max_weight_day = operations.max(scan_output)

if __name__ == "__main__":
    main()

