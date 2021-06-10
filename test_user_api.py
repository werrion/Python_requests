import requests
import json

url = "https://petstore.swagger.io/v2/user/createWithList"

payload = json.dumps([
  {
    "id": "999889898989",
    "username": "{{username}}",
    "firstName": "Test2",
    "lastName": "Test2",
    "email": "Test2@gmail.com",
    "password": "123",
    "phone": "{{phone}}",
    "userStatus": 1
  }
])
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
