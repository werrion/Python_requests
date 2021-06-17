# import requests
# import json
#
# url = "https://petstore.swagger.io/v2/user/createWithList"
#
# payload = json.dumps([
#   {
#     "id": "999889898989",
#     "username": "{{username}}",
#     "firstName": "Test2",
#     "lastName": "Test2",
#     "email": "Test2@gmail.com",
#     "password": "123",
#     "phone": "{{phone}}",
#     "userStatus": 1
#   }
# ])
# headers = {
#   'Content-Type': 'application/json',
#   'Accept': 'application/json'
# }
# def test_post():
#     response = requests.request("POST", url, headers=headers, data=payload)
#     print(response.text)
from request_example import *
if __name__ == '__main__':
    test_post()
    test_ok()
    #test_fail()
    test_ok1()
