import json

# remove . for Lambda
from .clockify_api import check_account
from .db import get_user_id, set_clockify_api_key

def lambda_handler(event, context):

    if event['httpMethod'] == "POST":
        
        try:
            body = json.loads(event['body'])
            user_token = body['user_token']
            print("user_token: ",user_token)
            user_api_key = body['user_api_key']
            print("user_api_key: ",user_api_key)

            user_id = get_user_id(user_token)

            if user_id:
                valid = check_account(user_api_key)
                if valid:
                    set_clockify_api_key(user_id,user_api_key)
        except : 
            return {
            'statusCode': 400,
            'body': json.dumps({"valid":False}, ensure_ascii=False)
        }

        return {
            'statusCode': 200,
            'body': json.dumps({"valid":valid}, ensure_ascii=False)
        }

    else:
        return {
            'statusCode': 405,
            'headers': {
                'Allow': 'POST'
            },
        }
