import json
import requests

API_BASE_URL = "https://api.clockify.me/api/v1"

def check_account(api_key):

    header = {'X-Api-Key': api_key,
          'content-type':'application/json'}

    url = API_BASE_URL + "/user"

    response = requests.get(url, headers=header)

    if response.status_code == 200:
        user_info = response.json()
        print(user_info)
        return True 
    else:
        print("User not found!")
        return False

if __name__ == '__main__':

    api_key = "sdfojsdfhgasid"

    clockify = check_account(api_key)

    print(clockify)
    