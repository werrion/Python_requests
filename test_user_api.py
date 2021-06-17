import allure
import requests
from request_example import *


@allure.story("Тест POST запрос")
@allure.step("Проверка ответа POST запроса ")
def test_post():
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


@allure.step("Тест Ok статус")
def test_ok():
    assert 1 == 1

"""@allure.step("Тест fail статус")
def test_fail():
    assert 1 == 2
    
"""



@allure.step("Тест Ok1 статус")
def test_ok1():
    assert 2 == 2
