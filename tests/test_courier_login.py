import allure
import pytest
import requests

from data import DataMessage
from helpers import generate_login, generate_password
from urls import Urls


class TestCourierLogin:

    @allure.title("Успешная авторизация курьера при заполненых обязательных полях")
    def test_courier_login(self, auth_data):
        response = requests.post(f"{Urls.BASE}{Urls.COURIER_LOGIN}", data=auth_data)
        assert response.status_code == 200 and "id" in response.json()

    @allure.title("Проверка получения ошибки, если неправильно указать логин или пароль")
    @pytest.mark.parametrize(
        "params",
        [
            {"login": generate_login()},
            {"password": generate_password()},
        ],
    )
    def test_login_courier_with_wrong_params(self, params, auth_data):
        data = auth_data.copy()
        data.update(params)
        response = requests.post(f"{Urls.BASE}{Urls.COURIER_LOGIN}", data=data)
        assert response.status_code == 404 and DataMessage.MES_ACCOUNT_NOT_FOUND in response.json().get("message")

    @allure.title("Проверка получения ошибки авторизации с пустыми полями логина или пароля")
    @pytest.mark.parametrize(
        "params",
        [
            {"login": ""},
            {"password": ""},
        ],
    )
    def test_login_courier_empty_params(self, params, auth_data):
        data = auth_data.copy()
        data.update(params)
        response = requests.post(f"{Urls.BASE}{Urls.COURIER_LOGIN}", data=data)
        assert response.status_code == 400 and DataMessage.MES_LOGIN_MISSED_DATA in response.json().get("message")

    @allure.title("Проверка получения ошибки авторизации с отсутствующими полями логина или пароля")
    @pytest.mark.parametrize(
        "field",
        [
            "login",  # удаляем логин из данных запроса
            "password",  # удаляем пароль из данных запроса (тест провален, 504)
        ],
    )
    def test_login_courier_empty_params(self, field, auth_data):
        data = auth_data.copy()
        data.pop(field)
        response = requests.post(f"{Urls.BASE}{Urls.COURIER_LOGIN}", data=data)
        assert response.status_code == 400 and DataMessage.MES_LOGIN_MISSED_DATA in response.json().get("message")
