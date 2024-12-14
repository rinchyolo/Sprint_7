import allure
import requests

from config import BASE_URL, CREATE_COURIER, LOGIN_COURIER, DELETE_COURIER


class CourierMethods:
    @allure.step('Вызов метода POST для создание курьера')
    def create_courier(self, payload):
        return requests.post(f'{BASE_URL}{CREATE_COURIER}', json=payload)

    @allure.step('Вызов метода POST для авторизации курьера')
    def login_courier(self, payload):
        return requests.post(f'{BASE_URL}{LOGIN_COURIER}', json=payload)

    @allure.step('Вызов метода DELETE для удаления курьера')
    def delete_courier(self, id_courier):
        return requests.delete(f'{BASE_URL}{DELETE_COURIER}/{id_courier}')
