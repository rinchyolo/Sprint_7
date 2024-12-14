import requests

from config import BASE_URL, CREATE_COURIER, LOGIN_COURIER, DELETE_COURIER


class CourierMethods:
    def create_courier(self, payload):
        return requests.post(f'{BASE_URL}{CREATE_COURIER}', json=payload)

    def login_courier(self, payload):
        return requests.post(f'{BASE_URL}{LOGIN_COURIER}', json=payload)

    def delete_courier(self, id_courier):
        return requests.delete(f'{BASE_URL}{DELETE_COURIER}/{id_courier}')
