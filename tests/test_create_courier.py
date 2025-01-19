import allure
import pytest
import requests

from data import DataForAuth
from urls import Urls

from helper import generate_login, generate_password, generate_firstname


class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    @allure.description("Передаются все обязательные поля")
    def test_create_courier(self):
        payload = {
            "login": generate_login(),
            "password": generate_password(),
            "firstName": generate_firstname(),
        }
        response = requests.post(Urls.COURIER_CREATE, data=payload)
        assert response.status_code == 201 and response.json().get("ok") is True

    @allure.title("Невозможность создания двух одинаковых курьеров")
    @allure.description("Возвращается ошибка при создании пользователя с уже существующим логином")
    def test_not_create_same_couriers(self):
        payload = {
            "login": DataForAuth.MY_LOGIN,
            "password": generate_password(),
            "firstName": generate_firstname(),
        }
        response = requests.post(Urls.COURIER_CREATE, data=payload)
        # в этом месте на текущий момент тест не проходит, потому что ответ не соответствует
        # описанию в документации к API
        # E         - Этот логин уже используется
        # E         + Этот логин уже используется. Попробуйте другой.)
        # проверять вхождение <expected> in .get("message") не стала, потому что не уверена, является ли
        # другое сообщение об ошибке (расширенное) ожидаемым поведением на бекенде
        assert response.status_code == 409 and response.json().get("message") == "Этот логин уже используется"

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
        response = requests.post(Urls.COURIER_CREATE, data=params)
        assert (
            response.status_code == 400
            and response.json().get("message") == "Недостаточно данных для создания учетной записи"
        )
