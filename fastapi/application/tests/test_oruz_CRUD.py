import unittest
import random
from application.config import SessionLocal
from application.services.repository_service import *

class TestOruzCrud(unittest.TestCase):
    def setUp(self):
        """ Наследуемый метод setUp определяет инструкции,
            которые должны быть выполнены ПЕРЕД тестированием """
        self.session = SessionLocal()

    def tearDown(self):
        """ Наследуемый метод tearDown определяет инструкции,
            которые должны быть выполнены ПОСЛЕ тестирования """
        self.session.close()

    def test_create_ingredient(self):
        """ Тест функции создания записи Ingredient """
        result = create_ingredient(self.session, name="Курица", count=0)
        self.assertTrue(result)

    def test_get_ingredient(self):
        ingredient = get_ingredient_by_name(self.session,name="Курица")
        self.assertIsNotNone(ingredient)  # запись должна существовать
        self.assertTrue(ingredient.count == 0)  # идентификатор city_id == 1 (т.е. город UFA в таблице city)
        self.assertTrue(ingredient.name == "Курица")

    def test_delete_ingredient(self):
        """ Тест функции удаления записи Weather по наименованию населённого пункта """
        delete_ingredient_by_id(self.session, id=2)
        result = get_ingredient_by_id(self.session, id=2)        # ищем запись по идентификатору города UFA
        self.assertIsNone(result)

    def test_test_add(self):
        result = create_test(self.session, name="Курица")
        create_test(self.session, name="Курица2")
        create_test(self.session, name="Курица3")
        self.assertTrue(result)
    def test_test_update(self):
        result=uprade_test_by_id(self.session,2,"Картошка")
        self.assertTrue(result)

    def test_test_delete(self):
        result=delete_test_by_id(self.session,2)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()