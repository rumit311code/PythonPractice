import requests

#####
##### GET
#####
def get_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    try:
        response = requests.get(url=url)
        if response.status_code == 200:
            return response.json()
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

posts = get_posts()
if posts:
    print('First Post Title:', posts[0]['title'])
    print('First Post Body:', posts[0]['body'])
else:
    print('Failed to fetch posts from API.')

#####
##### POST
#####

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}

response = requests.post(url=api_url, json=todo)
print(response.json())
print(response.status_code)

#####
##### HTTP Basic authentication with username/password
#####
from requests.auth import HTTPBasicAuth

url = 'https://httpbin.org/basic-auth/user/passwd'
username = 'user'
password = 'passwd'

response = requests.get(url=url, auth=HTTPBasicAuth(username, password))

if response.status_code == 200:
    print("Authentication successful:", response.json())
else:
    print("Authentication failed with status code:", response.status_code)


#####
##### API key authentication
#####
url = 'https://api.mockapi.com/data'
api_key = 'your_api_key_here'

headers = {
    'x-api-key': api_key
}
response = requests.get(url=url, headers=headers)
print("Status Code:", response.status_code)
print("Response Body:", response.text)
headers = {
    'x-api-key': api_key
}

response = requests.get(url=url, headers=headers)

print("Status Code:", response.status_code)
print("Response Body:", response.text)

#####
##### Token-Based Authentication with JWT Example
#####
auth_url = 'https://example.com/api/authenticate'
api_url = 'https://example.com/api/resource'
username = 'user'
password = 'pass'

# Step 1: Authenticate and get JWT token
auth_response = requests.post(url=auth_url, json={'username': username, 'password': password})

if auth_response.status_code == 200:
    token = auth_response.json().get('token')
    print("Received token:", token)

    # Step 2: Use token to access protected resource
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url=api_url, headers=headers)

    if response.status_code == 200:
        print("Access granted to resource:", response.json())
    else:
        print("Failed to access resource, status code:", response.status_code)
else:
    print("Authentication failed with status code:", auth_response.status_code)