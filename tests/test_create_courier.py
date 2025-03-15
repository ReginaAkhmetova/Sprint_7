import allure
import pytest
import requests

from data import DataMessage
from urls import Urls

from helpers import generate_login, generate_password, generate_firstname


class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    @allure.description("Передаются все обязательные поля")
    def test_create_courier(self):
        payload = {
            "login": generate_login(),
            "password": generate_password(),
            "firstName": generate_firstname(),
        }
        response = requests.post(f"{Urls.BASE}{Urls.COURIER_CREATE}", data=payload)
        assert response.status_code == 201 and response.json().get("ok") is True

    @allure.title("Невозможность создания двух одинаковых курьеров")
    @allure.description("Возвращается ошибка при создании пользователя с уже существующим логином")
    def test_not_create_same_couriers(self, auth_data):
        payload = {
            "login": auth_data["login"],
            "password": generate_password(),
            "firstName": generate_firstname(),
        }
        response = requests.post(f"{Urls.BASE}{Urls.COURIER_CREATE}", data=payload)
        assert response.status_code == 409 and DataMessage.MES_LOGIN_ALREADY_IN_USE in response.json().get("message")

    @allure.title("Получение ошибки при создании пользователя без одного из обязательных полей")
    @pytest.mark.parametrize(
        "params",
        [
            {  # пустое значение логина
                "login": "",
                "password": generate_password(),
                "firstName": generate_firstname(),
            },
            {  # пустое значение пароля
                "login": generate_login(),
                "password": "",
                "firstName": generate_firstname(),
            },
            {  # не передали логин
                "password": generate_password(),
                "firstName": generate_firstname(),
            },
            {  # не передали пароль
                "login": generate_login(),
                "firstName": generate_firstname(),
            },
        ],
    )
    def test_not_create_courier_with_empty_line(self, params):
        response = requests.post(f"{Urls.BASE}{Urls.COURIER_CREATE}", data=params)
        assert (
                response.status_code == 400
                and DataMessage.MES_CREATE_COURIER_MISSED_DATA in response.json().get("message")
        )  # fmt: skip
