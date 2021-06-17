import allure
import requests
from request_example import *


@allure.story("Тесты - POST запрос")
@allure.step("Проверка ответа POST запроса ")
def test_post1():
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


@allure.story("Тесты для проверки Ассертейшенов")
@allure.step("Тест Ok статус")
def test_ok11():
    assert 1 == 1

@allure.story("Тесты для проверки Ассертейшенов")
@allure.step("Тест fail статус")
def test_fail1():
    assert 1 == 2

@allure.story("Тесты для проверки Ассертейшенов")
@allure.step("Тест Ok1 статус")
def test_ok111():
    assert 2 == 2
