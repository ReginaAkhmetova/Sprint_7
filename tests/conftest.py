import pytest
import requests

from helpers import generate_login, generate_password, generate_firstname
from urls import Urls


@pytest.fixture(scope="session")
def auth_data():
    # генерим валидные данные курьера
    courier_data = {
        "login": generate_login(),
        "password": generate_password(),
        "firstName": generate_firstname(),
    }
    auth_data = {k: v for k, v in courier_data.items() if k in ("login", "password")}

    # создаем курьера для использования в тестах
    response = requests.post(f"{Urls.BASE}{Urls.COURIER_CREATE}", data=courier_data)
    if response.status_code != 201:
        raise RuntimeError(
            f"Что-то пошло не так, не могу создать курьера для тестов! {response.status_code}: {response.text}"
        )

    # получаем его айдишник - единственный способ это сделать - залогиниться под ним
    response = requests.post(f"{Urls.BASE}{Urls.COURIER_LOGIN}", data=auth_data)
    courier_id = response.json().get("id")

    # выполняем тест - йелдим данные для логина под этим курьером
    yield auth_data

    # удаляем созданного для тестов курьера
    requests.delete(f"{Urls.BASE}{Urls.COURIER_DELETE}/{courier_id}")
