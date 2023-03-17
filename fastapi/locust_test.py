import json
import time
import random
import json
from locust import HttpUser, task, tag, between

class RESTServerUser(HttpUser):
    """ Класс, эмулирующий пользователя / клиента сервера """
    wait_time = between(1.0, 5.0)       # время ожидания пользователя перед выполнением новой task

    # Адрес, к которому клиенты (предположительно) обращаются в первую очередь (это может быть индексная страница, страница авторизации и т.п.)
    def on_start(self):
        self.client.get("/docs")

    @tag("get_ingredients")
    @task(5)
    def get_ingredients(self):
        """ Тест GET-запроса (получение нескольких записей о погоде) """
        ingredient_id = random.randint(10, 41)  # генерируем случайный id в диапазоне [0, 3]
          # получаем случайное значение населенного пункта из списка CITY_NAMES
        with self.client.get(f'/api/ingredient?id={ingredient_id}',
                             catch_response=True,
                             name='/api/ingredient?id={ID}') as response:
            # Если получаем код HTTP-код 200, то оцениваем запрос как "успешный"
            if response.status_code == 200:
                response.success()
            # Иначе обозначаем как "отказ"
            else:
                response.failure(f'Status code is {response.status_code}')


