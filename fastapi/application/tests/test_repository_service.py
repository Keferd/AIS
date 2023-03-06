import unittest
import random
from application.config import SessionLocal
from application.services.repository_service import *


"""
   Данный модуль реализует "тестовые случаи/ситуации" для модуля repository_service.
   Для создания "тестового случая" необходимо создать отдельный класс, который наследует 
   базовый класс TestCase. Класс TestCase предоставляется встроенным 
   в Python модулем для тестирования - unittest.
   
   Более детально см.: https://pythonworld.ru/moduli/modul-unittest.html
"""


CITY = []

WEATHER_TYPE = []


class TestWeatherRepositoryService(unittest.TestCase):
    """ Все тестовые методы в классе TestCase (по соглашению)
        должны начинаться с префикса test_* """

    def setUp(self):
        """ Наследуемый метод setUp определяет инструкции,
            которые должны быть выполнены ПЕРЕД тестированием """
        self.session = SessionLocal()       # создаем сессию подключения к БД
        try:
            for city_name in CITY:
                add_city(self.session, city_name)
            for weather_type_name in WEATHER_TYPE:
                add_weather_type(self.session, weather_type_name)
        except:
            print('Test data already created')

    def test_create_weather(self):
        """ Тест функции создания записи Weather """
        result = create_weather(self.session,
                                temp_c=random.uniform(20.0, 29.9),
                                pressure=random.randint(735, 755),
                                city_id=1,
                                weather_type=1)
        self.assertTrue(result)     # валидируем результат (result == True)

    def test_get_weather(self):
        """ Тест функции поиска записи Weather по наименованию населённого пункта """
        weather_in_ufa_rows = get_weather_by_city_name(self.session, city_name='UFA')
        for row in weather_in_ufa_rows:
            self.assertIsNotNone(row)           # запись должна существовать
            self.assertTrue(row.city_id == 1)   # идентификатор city_id == 1 (т.е. город UFA в таблице city)
            self.assertTrue(row.city_name.name == 'UFA')  # проверка связи (relation) по FK

    def test_delete_weather(self):
        """ Тест функции удаления записи Weather по наименованию населённого пункта """
        delete_weather_by_city_name(self.session, city_name='UFA')
        result = get_weather_by_city_id(self.session, city_id=1)        # ищем запись по идентификатору города UFA
        self.assertIsNone(result)       # запись не должна существовать

    def tearDown(self):
        """ Наследуемый метод tearDown определяет инструкции,
            которые должны быть выполнены ПОСЛЕ тестирования """
        self.session.close()        # закрываем соединение с БД


if __name__ == '__main__':
    unittest.main()
