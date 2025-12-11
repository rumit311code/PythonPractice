import time
import requests

#####
##### OAuth2 configuration
#####

token_url = "https://authorization-server.com/oauth2/token"
client_id = "your_client_id"
client_secret = "your_client_secret"

def get_access_token():
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(url=token_url, data=data, auth=(client_id, client_secret))
    response.raise_for_status()
    token_info = response.json()
    access_token = token_info['access_token']
    expires_in = token_info.get('expires_in', 3600)  # default 1 hour if not provided
    return access_token, expires_in

def call_protected_api(access_token):
    api_url = "https://api-server.com/protected/resource"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url=api_url, headers=headers) # works same for post also, just that post will have some data.
    return response

#####
##### Main logic
#####
access_token, expires_in = get_access_token()
token_expiry = time.time() + expires_in

#####
##### Example usage loop
#####
for _ in range(5):  # Make 5 API calls as an example
    if time.time() >= token_expiry:
        print("Access token expired, refreshing...")
        access_token, expires_in = get_access_token()
        token_expiry = time.time() + expires_in

    response = call_protected_api(access_token)
    print(f"API status: {response.status_code}, Response: {response.text}")
    time.sleep(10)  # wait before next call
