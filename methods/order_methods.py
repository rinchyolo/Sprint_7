import requests

from config import BASE_URL, CREATE_ORDER, ORDER_LIST


class OrderMethods:

    def post_order(self, params):
        return requests.post(f'{BASE_URL}{CREATE_ORDER}', json=params)

    def get_orders(self, courier_id):
        return requests.get(f'{BASE_URL}{ORDER_LIST}{courier_id}')
