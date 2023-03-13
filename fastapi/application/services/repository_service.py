from typing import Optional, Iterable
from sqlalchemy.orm import Session
from application.models.dao.oruz import *
import functools
import traceback


"""

    Данный модуль является промежуточным слоем приложения, который отделяет операции 
    для работы с моделями DAO от основной бизнес-логики приложения. Создание данного 
    слоя позволяет унифицировать функции работы с источником данных, и, например, если 
    в приложении нужно будет использовать другой framework для работы с БД, вы можете 
    создать новый модуль (newframework_repository_service.py) и реализовать в нем функции 
    с аналогичными названиями (get_weather_by_city_id, и т.д.). Новый модуль можно будет
    просто импортировать в модуль с основной бизнес-логикой, практически не меняя при этом
    остальной код.
    Также отделение функций работы с БД можно сделать через отдельный абстрактный класс и 
    использовать порождающий паттерн для переключения между необходимыми реализациями.

"""


def dbexception(db_func):
    """ Функция-декоратор для перехвата исключений БД.
        Данный декоратор можно использовать перед любыми
        функциями, работающими с БД, чтобы не повторять в
        теле функции конструкцию try-except (как в функции add_weather). """
    @functools.wraps(db_func)
    def decorated_func(db: Session, *args, **kwargs) -> bool:
        try:
            db_func(db, *args, **kwargs)    # вызов основной ("оборачиваемой") функции
            db.commit()     # подтверждение изменений в БД
            return True
        except Exception as ex:
            # выводим исключение и "откатываем" изменения
            print(f'Exception in {db_func.__name__}: {traceback.format_exc()}')
            db.rollback()
            return False
    return decorated_func

""" -------------------------- Orders -------------------------- """

#ПОЛУЧЕНИЕ
def get_order_by_id(db: Session, id: int) -> Optional[Orders]:
    result = db.query(Orders).filter(Orders.id == id).first()
    return result

#ДОБАВЛЕНИЕ

@dbexception
def add_order(db: Session) -> Optional[Orders]:
    order = Orders()
    try:
        db.add(order)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return None
    return order

#УДАЛЕНИЕ
@dbexception
def delete_order_by_id(db: Session, id: int) -> bool:
    order = get_order_by_id(db, id)
    try:
        db.delete(order)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True

""" -------------------------- Dishes -------------------------- """

#ПОЛУЧЕНИЕ ПО ID
def get_dish_by_id(db: Session, id: int) -> Optional[Dishes]:
    result = db.query(Dishes).filter(Dishes.id == id).first()
    return result

#ПОЛУЧЕНИ ПО ИМЕНИ
def get_dish_by_name(db: Session, name: String) -> Optional[Dishes]:
    result = db.query(Dishes).filter_by(name=name).first()
    return result

#ДОБАВЛЕНИЕ
def create_dish(db: Session, name) -> Optional[Dishes]:
    dish = Dishes(name=name)
    return add_dish(db, dish)

def add_dish(db: Session, dish: Dishes) -> Optional[Dishes]:
    try:
        db.add(dish)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return None
    return dish

#ИЗМЕНЕНИЕ
def upgrade_dish_by_id(db: Session,id, name) -> bool:
    dish = get_dish_by_id(db,id)
    dish.name = name
    return add_ingredient(db, dish)

#УДАЛЕНИЕ
def delete_dish_by_id(db: Session, id: int) -> bool:
    dish = get_dish_by_id(db, id)
    try:
        db.delete(dish)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True

""" -------------------------- Ingredients -------------------------- """
#ПОЛУЧЕНИЕ ПО ID
def get_ingredient_by_id(db: Session, id: int) -> Optional[Ingredients]:
    result = db.query(Ingredients).filter_by(id=id).first()
    return result

#ПОЛУЧЕНИ ПО ИМЕНИ
def get_ingredient_by_name(db: Session, name: String) -> Optional[Ingredients]:
    result = db.query(Ingredients).filter_by(name=name).first()
    return result

#СОЗДАНИЕ
def create_ingredient(db: Session, name,count=0 ) -> bool:
    ingredient = Ingredients(name=name, count=count)
    return add_ingredient(db, ingredient)

def add_ingredient(db: Session, ingredient: Ingredients) -> bool:
    try:
        db.add(ingredient)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True

#ИЗМЕНЕНИЕ
def uprade_ingredient_by_id(db: Session, id,name,count ) -> bool:
    ingredient = get_ingredient_by_id(db,id)
    ingredient.name = name
    ingredient.count=count
    return add_ingredient(db, ingredient)

#УДАЛЕНИЕ
def delete_ingredient_by_id(db: Session, id: int) -> bool:
    ingredient = get_ingredient_by_id(db, id)
    try:
        db.delete(ingredient)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True

""" -------------------------- Storage -------------------------- """

#ПОЛУЧЕНИЕ ПО ID
def get_storage_by_id(db: Session, id: int) -> Optional[Storage]:
    result = db.query(Storage).filter(Storage.id == id).first()
    return result

#ПОЛУЧЕНИЕ ПО ID ИНГРЕДИЕНТА
def get_storage_by_ingredient_id(db: Session, id: int) -> Optional[Storage]:
    result = db.query(Storage).filter(Storage.id_ingredient == id).first()
    return result

#СОЗДАНИЕ
def create_storage(db: Session, count, date, id_ingredient) -> bool:
    storage = Storage(count=count, expiry_date=date, id_ingredient=id_ingredient)
    return add_storage(db, storage)

def add_storage(db: Session, storage: Storage) -> bool:
    try:
        db.add(storage)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True

#ИЗМЕНЕНИЕ
def uprade_storage_amount_by_id(db: Session, id,count ) -> bool:
    storage = get_storage_by_id(db,id)
    storage.count=count
    return add_ingredient(db, storage)

#УДАЛЕНИЕ
def delete_storage_by_id(db: Session, id: int) -> bool:
    storage = get_storage_by_id(db, id)
    try:
        db.delete(storage)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True


""" -------------------------- DishesIngredients -------------------------- """
#ПОЛУЧЕНИЕ ПО ID БЛЮДА
def get_dish_ingredient_by_dish_id(db: Session, id_dish: int) -> Iterable[DishesIngredients]:
    result = db.query(DishesIngredients).filter(DishesIngredients.id_dish == id_dish).all()
    return result

#ПОЛУЧЕНИЕ ПО ID ИНГРЕДИЕНТА
def get_dish_ingredient_by_ingredient_id(db: Session, id_ingredient: int) -> Optional[DishesIngredients]:
    result = db.query(DishesIngredients).filter(DishesIngredients.id_ingredient == id_ingredient).all()
    return result

#СОЗДАНИЕ
def create_dish_ingredient(db: Session, id_dish, id_ingredient, amount) -> bool:
    dish_ingredient = DishesIngredients(id_dish=id_dish, id_ingredient=id_ingredient, amount=amount)
    return add_dish_ingredient(db, dish_ingredient)

def add_dish_ingredient(db: Session, dish_ingredient: DishesIngredients) -> bool:
    try:
        db.add(dish_ingredient)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True

#ИЗМЕНЕНИЕ ПО ID БЛЮДА
def uprade_dish_ingredient_amount_by_dish_id(db: Session, id,count ) -> bool:
    dish_ingredient = get_dish_ingredient_by_dish_id(db,id)
    dish_ingredient.count=count
    return add_ingredient(db, dish_ingredient)

#ИЗМЕНЕНИЕ ПО ID ИНГРЕДИЕНТА
def uprade_dish_ingredient_amount_by_ingredient_id(db: Session, id,count ) -> bool:
    dish_ingredient = get_dish_ingredient_by_ingredient_id(db,id)
    dish_ingredient.count=count
    return add_ingredient(db, dish_ingredient)

#УДАЛЕНИЕ ПО ID БЛЮДА
def delete_dish_ingredient_by_dish_id(db: Session, id: int) -> bool:
    dish_ingredient = get_dish_ingredient_by_dish_id(db, id)
    try:
        for di_in in dish_ingredient:
            db.delete(di_in)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True

#УДАЛЕНИЕ ПО ID ИНГРЕДИЕНТА
def delete_dish_ingredient_by_ingredient_id(db: Session, id: int) -> bool:
    dish_ingredient = get_dish_ingredient_by_ingredient_id(db, id)
    try:
        db.delete(dish_ingredient)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True

""" -------------------------- OrdersDishes -------------------------- """

#ПОЛУЧЕНИЕ ПО ID ЗАКАЗА
def get_order_dish_by_order_id(db: Session, dish_id: int) -> Optional[OrdersDishes]:
    result = db.query(OrdersDishes).filter(OrdersDishes.dish_id == dish_id).all()
    return result

#ПОЛУЧЕНИЕ ВСЕХ ПО ID ЗАКАЗА
# def get_all_order_dish_by_order_id(db: Session, dish_id: int) -> Optional[OrdersDishes]:
#     result = db.query(OrdersDishes).filter(OrdersDishes.dish_id == dish_id).all()
#     return result

#ПОЛУЧЕНИЕ ПО ID БЛЮДА
def get_order_dish_by_dish_id(db: Session, order_id: int) -> Optional[OrdersDishes]:
    result = db.query(OrdersDishes).filter(OrdersDishes.order_id == order_id).all()
    return result

#ПОЛУЧЕНИЕ ВСЕХ ПО ID БЛЮДА
# def get_all_order_dish_by_dish_id(db: Session, order_id: int) -> Optional[OrdersDishes]:
#     result = db.query(OrdersDishes).filter(OrdersDishes.order_id == order_id).all()
#     return result

#СОЗДАНИЕ
def create_order_dish(db: Session, id_order, id_dish, amount) -> bool:
    order_dish = OrdersDishes(id_order=id_order, id_dish=id_dish, amount=amount)
    return add_order_dish(db, order_dish)

def add_order_dish(db: Session, order_dish: OrdersDishes) -> bool:
    try:
        db.add(order_dish)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True

#ИЗМЕНЕНИЕ ПО ID ЗАКАЗА
def uprade_order_dish_amount_by_order_id(db: Session, id,count ) -> bool:
    order_dish = get_order_dish_by_order_id(db,id)
    order_dish.count=count
    return add_ingredient(db, order_dish)

#ИЗМЕНЕНИЕ ПО ID БЛЮДА
def uprade_order_dish_amount_by_dish_id(db: Session, id,count ) -> bool:
    order_dish = get_order_dish_by_dish_id(db,id)
    order_dish.count=count
    return add_ingredient(db, order_dish)

#УДАЛЕНИЕ ПО ID ЗАКАЗА
def delete_order_dish_by_order_id(db: Session, id: int) -> bool:
    order_dish = get_order_dish_by_order_id(db, id)
    try:
        db.delete(order_dish)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True

#УДАЛЕНИЕ ПО ID БЛЮДА
def delete_order_dish_by_dish_id(db: Session, id: int) -> bool:
    order_dish = get_order_dish_by_dish_id(db, id)
    try:
        db.delete(order_dish)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True


""" -------------------------- Test -------------------------- """
#ПОЛУЧЕНИЕ ПО ID
def get_test_by_id(db: Session, id: int) -> Optional[DishesIngredients]:
    result = db.query(Test).filter(Test.id == id).first()
    return result

#СОЗДАНИЕ
def create_test(db: Session, name) -> bool:
    test = Test(name=name)
    return add_test(db, test)

def add_test(db: Session, test: Test) -> bool:
    try:
        db.add(test)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True

#ИЗМЕНЕНИЕ ПО ID
def uprade_test_by_id(db: Session, id,name ) -> bool:
    test = get_test_by_id(db,id)
    test.name=name
    return add_ingredient(db, test)

def delete_test_by_id(db: Session, id: int) -> bool:
    test = get_test_by_id(db, id)
    try:
        db.delete(test)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True

# def get_weather_by_city_id(db: Session, city_id: int) -> Optional[Weather]:
#     """ Выборка одной записи о погоде по идентификатору (PrimaryKey) населённого пункта """
#     result = db.query(Weather).filter(Weather.city == city_id).first()
#     return result
#
#
# def get_weather_by_city_name(db: Session, city_name: str) -> Iterable[Weather]:
#     """ Выборка всех записей о погоде по наименованию населённого пункта """
#     result = db.query(Weather).join(City).filter(City.name == city_name).all()
#     return result
#
#
# def create_weather(db: Session, temp_c: float, pressure: int, city_id: int, weather_type: int) -> bool:
#     """ Создание нового объекта Weather и добавление записи о погоде """
#     weather = Weather(
#         temperature_c=temp_c,
#         pressure=pressure,
#         city=city_id,
#         type=weather_type
#         )
#     return add_weather(db, weather)
#
#
# def add_weather(db: Session, weather: Weather) -> bool:
#     """ Добавление записи о погоде (с помощью готового объекта Weather) """
#     try:
#         db.add(weather)
#         db.commit()
#     except Exception as ex:
#         print(traceback.format_exc())
#         db.rollback()
#         return False
#     return True
#
#
# def update_weather_temp_and_pressure(db: Session, temp_c: float, pressure: int, city_id: int) -> bool:
#     """ Обновление значений температуры и давления для заданного населённого пункта """
#     weather = get_weather_by_city_id(db, city_id)
#     weather.temperature_c = temp_c
#     weather.pressure = pressure
#     return add_weather(db, weather)
#
#
# @dbexception
# def delete_weather_by_city_name(db: Session, city_name: str) -> bool:
#     """ Удаление записей о погоде в указанном населённом пункте """
#     city_weather = get_weather_by_city_name(db, city_name)
#     for weather_obj in city_weather:
#         db.delete(weather_obj)
#
#
# @dbexception
# def add_city(db: Session, city_name: str) -> None:
#     """ Добавление нового населённого пункта """
#     city = City(name=city_name)
#     db.add(city)
#
#
# @dbexception
# def add_weather_type(db: Session, weather_type_name: str) -> None:
#     """ Добавление нового типа погоды """
#     weather_type = WeatherType(type=weather_type_name)
#     db.add(weather_type)
