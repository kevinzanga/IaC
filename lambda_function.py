import boto3
import os
from boto3.dynamodb.conditions import Key


DYNAMO_CLOUD = os.environ['DYNAMO_CLOUD']

class DynamoAccessor:
    def __init__(self, dynamo_table):
        dynamo_db = boto3.resource('dynamodb')
        self.table = dynamo_db.Table(dynamo_table)

    def get_data_from_dynamo(self, ci):
        response = self.table.query(KeyConditionExpression=Key('ci').eq(ci))
        return response["Items"][0] if any(response["Items"]) else None

def lambda_handler(event, context):
    dynamo_backend = DynamoAccessor(DYNAMO_CLOUD)
    db_element = dynamo_backend.get_data_from_dynamo(event['ci'])
    return db_element

