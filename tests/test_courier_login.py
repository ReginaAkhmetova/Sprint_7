import allure
import pytest
import requests

from data import DataForAuth
from urls import Urls


class TestCourierLogin:

    @allure.title("Успешная авторизация курьера при заполненых обязательных полях")
    def test_courier_login(self):
        response = requests.post(Urls.COURIER_LOG, data=DataForAuth.AUTHDATA_VALID)
        assert response.status_code == 200 and "id" in response.json()

    @allure.title("Проверка получения ошибки, если неправильно указать логин или пароль")
    @pytest.mark.parametrize(
        "params",
        [
            DataForAuth.AUTHDATA_WITH_WRONG_LOGIN,
            DataForAuth.AUTHDATA_WITH_WRONG_PASSWORD,
        ],
    )
    def test_login_courier_with_wrong_params(self, params):
        response = requests.post(Urls.COURIER_LOG, data=params)
        assert response.status_code == 404 and response.json().get("message") == "Учетная запись не найдена"

    @allure.title("Проверка получения ошибки авторизации с пустыми полями логина или пароля")
    @pytest.mark.parametrize(
        "params",
        [
            {"login": "", "password": DataForAuth.MY_PASSWORD},  # пустой логин
            {"login": DataForAuth.MY_LOGIN, "password": ""},  # пустой пароль
            {"password": DataForAuth.MY_PASSWORD},  # не передали логин
            {"login": DataForAuth.MY_LOGIN},  # не передали пароль - падает (504 вместо ожидаемого 400)
        ],
    )
    def test_login_courier_empty_params(self, params):
        response = requests.post(Urls.COURIER_LOG, data=params)
        assert response.status_code == 400 and response.json().get("message") == "Недостаточно данных для входа"
