import allure

from methods.order_methods import OrderMethods


class TestGetOrder:

    @allure.title("Получение списка заказов")
    def test_get_order(self):
        response = OrderMethods().get_orders(436659)
        assert response.status_code == 200
        assert "orders" in response.json()
