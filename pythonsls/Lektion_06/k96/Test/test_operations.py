import operations

class TestOpsClass:

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

