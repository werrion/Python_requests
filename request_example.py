# import requests
# data = requests.post ("https://petstore.swagger.io/v2/user/createWithList")
# print(data.status_code)
# assert data.status_code == 200
import allure
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
@allure.story("Тест POST запрос")
@allure.step("Проверка ответа POST запроса ")
def test_post():
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

@allure.step("Тест Ok статус")
def test_ok():
    assert 1==1

@allure.step("Тест fail статус")
def test_fail():
    assert 1==2
