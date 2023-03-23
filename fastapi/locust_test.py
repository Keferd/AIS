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

    @tag("get_orders")
    @task(5)
    def get_orders(self):
        """ Тест GET-запроса (получение нескольких записей о погоде) """
        order_id = random.randint(18, 900)  # генерируем случайный id в диапазоне [0, 3]
        # получаем случайное значение населенного пункта из списка CITY_NAMES
        with self.client.get(f'/api/order?id={order_id}',
                             catch_response=True,
                             name='/api/order?id={ID}') as response:
            # Если получаем код HTTP-код 200, то оцениваем запрос как "успешный"
            if response.status_code == 200:
                response.success()
            # Иначе обозначаем как "отказ"
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("get_dish")
    @task(5)
    def get_dish(self):
        """ Тест GET-запроса (получение нескольких записей о погоде) """
        dish_id = random.randint(3, 22)  # генерируем случайный id в диапазоне [0, 3]
        # получаем случайное значение населенного пункта из списка CITY_NAMES
        with self.client.get(f'/api/dish?id={dish_id}',
                             catch_response=True,
                             name='/api/dish?id={ID}') as response:
            # Если получаем код HTTP-код 200, то оцениваем запрос как "успешный"
            if response.status_code == 200:
                response.success()
            # Иначе обозначаем как "отказ"
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("get_storage")
    @task(5)
    def get_storage(self):
        """ Тест GET-запроса (получение нескольких записей о погоде) """
        id = random.randint(16, 491)  # генерируем случайный id в диапазоне [0, 3]
        # получаем случайное значение населенного пункта из списка CITY_NAMES
        with self.client.get(f'/api/storage?id={id}',
                             catch_response=True,
                             name='/api/storage?id={ID}') as response:
            # Если получаем код HTTP-код 200, то оцениваем запрос как "успешный"
            if response.status_code == 200:
                response.success()
            # Иначе обозначаем как "отказ"
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("post_order")
    @task(1)
    def post_order(self):
        """ Тест POST-запроса (создание записи о погоде) """
        # Генерируем случайные данные в опредленном диапазоне
        fields_amount = random.randint(1, 6)
        dishes={}
        for i in range(fields_amount):
            dish=random.randint(3, 22)
            amount = random.randint(1,5)
            dishes.update({f"{dish}":amount})
        test_data = {'dishes': dishes}
        post_data = json.dumps(test_data)  # сериализуем тестовые данные в json-строку
        # отправляем POST-запрос с данными (POST_DATA) на адрес <SERVER>/api/weatherforecast
        with self.client.post('/api/order',
                              catch_response=True,
                              name='/api/order', data=post_data,
                              headers={'content-type': 'application/json'}) as response:
            # проверяем, корректность возвращаемого HTTP-кода
            if response.status_code == 201:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("post_dish")
    @task(1)
    def post_dish(self):
        """ Тест POST-запроса (создание записи о погоде) """
        # Генерируем случайные данные в опредленном диапазоне
        fields_amount = random.randint(1, 6)
        ingredients = {}
        for i in range(fields_amount):
            ingredient = random.randint(9, 42)
            amount = random.randint(10, 500)
            ingredients.update({f"{ingredient}": amount})
        name=random.randint(12,67890)
        test_data = {'name':name,'ingredients': ingredients}
        post_data = json.dumps(test_data)  # сериализуем тестовые данные в json-строку
        # отправляем POST-запрос с данными (POST_DATA) на адрес <SERVER>/api/weatherforecast
        with self.client.post('/api/dish',
                              catch_response=True,
                              name='/api/dish', data=post_data,
                              headers={'content-type': 'application/json'}) as response:
            # проверяем, корректность возвращаемого HTTP-кода
            if response.status_code == 201:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("post_storage")
    @task(1)
    def post_storage(self):
        """ Тест POST-запроса (создание записи о погоде) """
        # Генерируем случайные данные в опредленном диапазоне
        ingredient_count = random.randint(50, 200)
        ingredient_id = random.randint(9, 42)
        test_data = {'count': ingredient_count,
                     'expiry_date':"2023-03-26T11:37:45.330Z",
                     'ingredient_id':ingredient_id}
        post_data = json.dumps(test_data)  # сериализуем тестовые данные в json-строку
        # отправляем POST-запрос с данными (POST_DATA) на адрес <SERVER>/api/weatherforecast
        with self.client.post('/api/storage',
                              catch_response=True,
                              name='/api/storage', data=post_data,
                              headers={'content-type': 'application/json'}) as response:
            # проверяем, корректность возвращаемого HTTP-кода
            if response.status_code == 201:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("put_ingredient")
    @task(3)
    def put_ingredient(self):
        """ Тест PUT-запроса (обновление записи о погоде) """
        ingredient_id = random.randint(9, 42)
        # получаем случайное значение населенного пункта из списка CITY_NAMES
        test_data = {'count': random.randint(100, 2000)}
        put_data = json.dumps(test_data)
        # отправляем PUT-запрос на адрес <SERVER>/api/weatherforecast/{city_name}
        with self.client.put(f'/api/ingredient?id={ingredient_id}',
                             catch_response=True,
                             name='/api/ingredient?id={ID}',
                             data=put_data,
                             headers={'content-type': 'application/json'}) as response:
            if response.status_code == 202:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("put_storage")
    @task(3)
    def put_storage(self):
        """ Тест PUT-запроса (обновление записи о погоде) """
        storage_id = random.randint(18, 700)
        # получаем случайное значение населенного пункта из списка CITY_NAMES
        test_data = {'count': random.randint(100, 2000),
                     'expiry_date':random.randint(100, 2000),
                     'ingredient_id':random.randint(100, 2000)}
        put_data = json.dumps(test_data)
        # отправляем PUT-запрос на адрес <SERVER>/api/weatherforecast/{city_name}
        with self.client.put(f'/api/storage?id={storage_id}',
                             catch_response=True,
                             name='/api/storage?id={ID}',
                             data=put_data,
                             headers={'content-type': 'application/json'}) as response:
            if response.status_code == 202:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("put_order")
    @task(3)
    def put_order(self):
        """ Тест PUT-запроса (обновление записи о погоде) """
        order_id = random.randint(18, 700)
        fields_amount = random.randint(3, 6)
        dishes = {}
        for i in range(fields_amount):
            dish = random.randint(3, 22)
            amount = random.randint(1, 5)
            dishes.update({f"{dish}": amount})
        test_data = {'dishes': dishes}
        put_data = json.dumps(test_data)
        # отправляем PUT-запрос на адрес <SERVER>/api/weatherforecast/{city_name}
        with self.client.put(f'/api/order?id={order_id}',
                             catch_response=True,
                             name='/api/order?id={ID}',
                             data=put_data,
                             headers={'content-type': 'application/json'}) as response:
            if response.status_code == 202:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')



