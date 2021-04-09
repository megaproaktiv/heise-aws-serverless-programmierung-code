import json
import extract


with open('s3put.json') as json_file:
    event = json.load(json_file)

print(extract.extractKey(event))