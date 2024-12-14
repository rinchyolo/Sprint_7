import allure
import pytest

from data import ORDER_DATA_1, ORDER_DATA_2, ORDER_DATA_3, ORDER_DATA_4
from methods.order_methods import OrderMethods


class TestCreateOrder:
    @pytest.mark.parametrize(
        "payload", [
            ORDER_DATA_1, ORDER_DATA_2, ORDER_DATA_3, ORDER_DATA_4
        ]
    )
    @allure.title("Создание заказа")
    def test_create_order(self, payload):
        response = OrderMethods().post_order(payload)
        assert response.status_code == 201
        assert "track" in response.json()
