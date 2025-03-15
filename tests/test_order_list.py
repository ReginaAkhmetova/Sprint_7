import allure
import requests

from urls import Urls


class TestOrderList:

    @allure.title("Проверка получения списка заказов")
    def test_get_order_list(self):
        response = requests.get(f"{Urls.BASE}{Urls.ORDERS}")
        # этот тест не проходит на текущий момент - возвращается 504 вместо ожидаемого 200
        # E       assert (504 == 200)
        assert response.status_code == 200 and isinstance(response.json()["orders"], list)
