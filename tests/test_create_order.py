import pytest
import allure
import requests

from data import DataOrders
from urls import Urls


class TestCreateOrder:

    @allure.title("Проверка создания заказа с разными значениями цвета")
    @pytest.mark.parametrize(
        "order_data",
        [
            DataOrders.CREATE_ORDERS_NO_COLORS,
            DataOrders.CREATE_ORDERS_BLACK_COLOR,
            DataOrders.CREATE_ORDERS_GREY_COLOR,
            DataOrders.CREATE_ORDERS_TWO_COLORS,
        ],
    )
    def test_create_order(self, order_data):
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{Urls.BASE}{Urls.ORDERS}", json=order_data, headers=headers)
        assert response.status_code == 201
        res = response.json()
        assert "track" in res and isinstance(res["track"], int)

        # дополнительно проверим, что этот заказ действительно существует - для этого
        # попытаемся его получить по его трек-номеру
        track_number = res["track"]
        response = requests.get(f"{Urls.BASE}{Urls.ORDER_GET_BY_TRACK}?t={track_number}")
        res = response.json()
        assert (
            response.status_code == 200
            and "order" in res
            and isinstance(res["order"], dict)
            and res["order"].get("track") == track_number
        )
