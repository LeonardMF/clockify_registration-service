import boto3
import pytz

from datetime import datetime
from decouple import config

LMF_AWS_ACCESS_KEY_ID = config("LMF_AWS_ACCESS_KEY_ID")
LMF_AWS_SECRET_ACCESS_KEY = config("LMF_AWS_SECRET_ACCESS_KEY")
LMF_AWS_DB_REGION = config("LMF_AWS_DB_REGION")
LMF_AWS_TABLE_NAME = config("LMF_AWS_TABLE_NAME")

CLOCKIFY_API_KEY = config('CLOCKIFY_API_KEY')
TIME_ZONE = config('TIME_ZONE')

# https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.04.html#GettingStarted.Python.04.Scan
def get_user_id(user_token):

    client = boto3.client('dynamodb', region_name=LMF_AWS_DB_REGION, aws_access_key_id=LMF_AWS_ACCESS_KEY_ID, aws_secret_access_key=LMF_AWS_SECRET_ACCESS_KEY)
    paginator = client.get_paginator('scan')
    operation_parameters = {
        'TableName': LMF_AWS_TABLE_NAME,
        'FilterExpression': 'user_token =:user_token ',
        'ExpressionAttributeValues': {
            ':user_token': {'S': user_token},
        }
    }

    page_iterator = paginator.paginate(**operation_parameters)
    for page in page_iterator:
        return page['Items'][0]['user_id']['S']
    return False

def set_clockify_api_key(user_id, clockify_api_key):

    tz = pytz.timezone(TIME_ZONE)
    now = datetime.now(tz)
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")

    try:
        dynamodb = boto3.resource('dynamodb', region_name=LMF_AWS_DB_REGION, aws_access_key_id=LMF_AWS_ACCESS_KEY_ID, aws_secret_access_key=LMF_AWS_SECRET_ACCESS_KEY)
        table = dynamodb.Table(LMF_AWS_TABLE_NAME)
        response = table.update_item(
                Key = {
                        'user_id': user_id
                },
                UpdateExpression="set clockify_api_key=:c_a_k, onboarded_at=:o_a",
                ExpressionAttributeValues={
                    ':c_a_k': clockify_api_key,
                    ':o_a': now_str,
                },
        )
    except:
        print("Clockify API key could not be set!")
        return False
    else:
        return True

if __name__ == '__main__':

    user_token = "LMF"
    user_id = get_user_id(user_token)
    clockify_api_key = CLOCKIFY_API_KEY
    print(set_clockify_api_key(user_id, clockify_api_key))
