import operations
import random
import boto3
from botocore.exceptions import ClientError


def test_max(capsys):
    input = { 'Items': [
        {'gramm': {'N': '95'
            }, '__typename': {'S': 'Weigh'
            }, 'date': {'S': '2021-03-06'
            }, 'userID': {'S': '1'
            }, 'updatedAt': {'S': '2021-03-06T18: 51: 23.540Z'
            }, 'createdAt': {'S': '2021-03-06T18: 51: 23.540Z'
            }, 'id': {'S': 'af594cf0-1a6c-4b9a-af13-66fe41ad2b42'
            }
        },
        {'gramm': {'N': '95'
            }, '__typename': {'S': 'Weigh'
            }, 'date': {'S': '2021-03-06'
            }, 'userID': {'S': '1'
            }, 'updatedAt': {'S': '2021-03-06T18: 51: 21.816Z'
            }, 'createdAt': {'S': '2021-03-06T18: 51: 21.816Z'
            }, 'id': {'S': '65efff19-1d6b-4142-8ff1-184056d46ace'
            }
        },
        {'gramm': {'N': '98'
            }, '__typename': {'S': 'Weigh'
            }, '_lastChangedAt': {'N': '1615052540582'
            }, 'date': {'S': '2021-03-06'
            }, '_version': {'N': '1'
            }, 'userID': {'S': '1'
            }, 'updatedAt': {'S': '2021-03-06T17: 42: 20.561Z'
            }, 'createdAt': {'S': '2021-03-06T17: 42: 20.561Z'
            }, 'id': {'S': 'c502db88-5ab6-430b-8233-3744620d7764'
            }
        }
    ]
    }
    max_weight = operations.max(input)
    # weight = max_weight['gramm']
    weight = max_weight
    assert weight['gramm'] ==  98

def _create_dynamodb_client(region="eu-central-1"):
    return boto3.client("dynamodb", region_name=region)

def _create_get_item_input_test_put_weight():
    return {
        "TableName": "daily-weight",
        "Key": {
            "id": {"S":"2#2021-03-14"}
        },
        "ProjectionExpression": "#05560",
        "ExpressionAttributeNames": {"#05560":"hectogramm"}
    }

def _execute_get_item(dynamodb_client, input):
    try:
        response = dynamodb_client.get_item(**input)
        return response
        # Handle response
    except ClientError as error:
        handle_error(error)
    except BaseException as error:
        print("Unknown error while getting item: " + error.response['Error']['Message'])        


def test_put_weight():
    # die Uid "2" ist für Test reserviert
    random_weight=random.randint(1, 10000)
    operations.put_weight("2","2021-03-14", random_weight)
    dynamodb_client_test = _create_dynamodb_client(region="eu-central-1")
    get_item_input = _create_get_item_input_test_put_weight()
    response = _execute_get_item(dynamodb_client_test, get_item_input)
    print(response)
    assert response['Item']['hectogramm']['N'] == str(random_weight)





