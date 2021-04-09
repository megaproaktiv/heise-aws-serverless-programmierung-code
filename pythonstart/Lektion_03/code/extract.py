import json

def extractKey(event):
    record = event['Records'][0]
    return record['s3']['object']['key']
