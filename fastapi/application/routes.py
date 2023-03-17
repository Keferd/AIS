from fastapi import APIRouter, HTTPException, status, Request, Response
from starlette.responses import RedirectResponse
from application.models.dto import *
from application.models.dto.dishes_dto import DishesDTO
from application.models.dto.ingredients_dto import IngredientsDTO
from application.models.dto.orders_dishes_dto import OrdersDishesDTO
from application.models.dto.orders_dto import OrdersDTO
from application.models.dto.storage_dto import StorageDTO
from application.services.weather_service import WeatherService


from application.config import SessionLocal
import application.services.repository_service as repository_service


"""

    Данный модуль отвечает за маршрутизацию доступных API URI (endpoints) сервера

"""


router = APIRouter(prefix='/api', tags=['Weather Forecast API'])       # подключаем данный роутер к корневому адресу /api
service = WeatherService()              # подключаем слой с дополнительной бизнес-логикой

@router.get('/')
async def root():
    """ Переадресация на страницу Swagger """
    return RedirectResponse(url='/docs', status_code=307)

""" -------------------------- Order -------------------------- """

# @router.get('/order', response_model=OrdersDTO)
# async def get_order_by_id(id: int):
#     """ Получение order по id """
#     with SessionLocal() as session:
#         response = repository_service.get_order_by_id(session, id)
#     if response is None:
#         return Response(status_code=204)
#     return OrdersDTO(time=response.date)
#
# @router.delete('/ingredient', status_code=200)
# async def del_ingredient_by_id(id: int):
#     """ Удаление ingredient по id """
#     with SessionLocal() as session:
#         if repository_service.delete_ingredient_by_id(session, id):
#             return Response(status_code=200)
#         else:
#             raise HTTPException(
#                 status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 detail="Can't delete Ingredient data",
#             )
#
# @router.post('/ingredient', status_code=201)
# async def post_ingredient(ingredient: IngredientsDTO):
#     """ Добавление ingredient """
#     with SessionLocal() as session:
#         if repository_service.create_ingredient(session,
#                                              name = ingredient.name,
#                                              count = ingredient.count):
#             return Response(status_code=201)
#         else:
#             raise HTTPException(
#                 status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 detail="Can't add new Ingredient data",
#             )
#
# @router.put('/ingredient', status_code=202)
# async def put_ingredient(id: int ,ingredient: IngredientsDTO):
#     """ Обновить Ingredients """
#     with SessionLocal() as session:
#         if repository_service.uprade_ingredient_by_id(session,
#                                                      id = id,
#                                                      name = ingredient.name,
#                                                      count = ingredient.count):
#             return Response(status_code=202)
#         else:
#             raise HTTPException(
#                 status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 detail="Can't update Weather data",
#             )

""" -------------------------- Orders -------------------------- """

@router.get('/order', response_model=OrdersDTO)
async def get_order_by_id(id: int):
    """ Получение order по id """
    with SessionLocal() as session:
        response = repository_service.get_order_by_id(session, id)
        result = repository_service.get_order_dish_by_order_id(session, id)
        dishes = {}
        for i in result:
            dishes[i.id_dish] = i.amount
    if response is None:
        return Response(status_code=204)
    return OrdersDTO(time=response.date, dishes=dishes)

@router.put('/order', status_code=202)
async def put_order(id: int ,order: OrdersDTO):
    """ Обновить Order """
    with SessionLocal() as session:
        neworder = repository_service.delete_order_dish_by_order_id(session, id)
        if neworder:
            dishes = order.dishes
            for key in dishes:
                repository_service.create_dish_ingredient(session, id, key, dishes[key])
            return Response(status_code=202)
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Can't update Weather data",
            )

@router.delete('/order', status_code=200)
async def del_order_by_id(id: int):
    """ Удаление order по id """
    with SessionLocal() as session:
        if repository_service.delete_order_by_id(session, id):
            return Response(status_code=200)
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Can't delete Ingredient data",
            )

@router.post('/order', status_code=201)
async def post_order(order: OrdersDTO):
    """ Добавление order """
    with SessionLocal() as session:
        neworder = repository_service.add_order(session)
        if order.dishes!={}:
            dishes = order.dishes
            for key in dishes:
                repository_service.create_order_dish(db=session,order_id=neworder.id,dish_id=key,amount=dishes[key])
                ingredients_for_dishes=repository_service.get_dish_ingredient_by_dish_id(session,key)
                for ing in ingredients_for_dishes:
                     repository_service.increace_ingredient_count_by_id(session, ing.ingredient_id, -dishes[key]*(ing.amount))
            return Response(status_code=201)
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Can't add new Ingredient data",
            )

""" -------------------------- Dishes -------------------------- """

@router.get('/dish', response_model=DishesDTO)
async def get_dish_by_id(id: int):
    """ Получение dish по id """
    with SessionLocal() as session:
        response = repository_service.get_dish_by_id(session, id)
        result = repository_service.get_dish_ingredient_by_dish_id(session, id)
        ingredients = {}
        for i in result:
            ingredients[i.id_ingredient] = i.amount
    if response is None:
        return Response(status_code=204)
    return DishesDTO(name=response.name, ingredients=ingredients)

@router.put('/dish', status_code=202)
async def put_dish(id: int ,dish: DishesDTO):
    """ Обновить Dish """
    with SessionLocal() as session:
        newdish = repository_service.upgrade_dish_by_id(session,id=id,name=dish.name)
        if newdish:
            repository_service.delete_dish_ingredient_by_dish_id(session, id)
            ingredients = dish.ingredients
            for key in ingredients:
                repository_service.create_dish_ingredient(session, id, key, ingredients[key])
            return Response(status_code=202)
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Can't update Weather data",
            )

@router.delete('/dish', status_code=200)
async def del_dish_by_id(id: int):
    """ Удаление dish по id """
    with SessionLocal() as session:
        if repository_service.delete_dish_by_id(session, id):
            return Response(status_code=200)
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Can't delete Ingredient data",
            )

@router.post('/dish', status_code=201)
async def post_dish(dish: DishesDTO):
    """ Добавление dish """
    with SessionLocal() as session:
        newdish = repository_service.create_dish(session, name=dish.name)
        if newdish:
            ingredients = dish.ingredients
            for key in ingredients:
                repository_service.create_dish_ingredient(session, newdish.id, key, ingredients[key])
            return Response(status_code=201)
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Can't add new Ingredient data",
            )

""" -------------------------- Ingredients -------------------------- """

@router.get('/ingredient', response_model=IngredientsDTO)
async def get_ingredient_by_id(id: int):
    """ Получение ingredient по id """
    with SessionLocal() as session:
        response = repository_service.get_ingredient_by_id(session, id)
    if response is None:
        return Response(status_code=204)
    return IngredientsDTO(name=response.name, count=response.count)

@router.delete('/ingredient', status_code=200)
async def del_ingredient_by_id(id: int):
    """ Удаление ingredient по id """
    with SessionLocal() as session:
        if repository_service.delete_ingredient_by_id(session, id):
            return Response(status_code=200)
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Can't delete Ingredient data",
            )

@router.post('/ingredient', status_code=201)
async def post_ingredient(ingredient: IngredientsDTO):
    """ Добавление ingredient """
    with SessionLocal() as session:
        if repository_service.create_ingredient(session,
                                             name = ingredient.name,
                                             count = ingredient.count):
            return Response(status_code=201)
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Can't add new Ingredient data",
            )

@router.put('/ingredient', status_code=202)
async def put_ingredient(id: int ,ingredient: IngredientsDTO):
    """ Обновить Ingredients """
    with SessionLocal() as session:
        if repository_service.uprade_ingredient_by_id(session,
                                                     id = id,
                                                     name = ingredient.name,
                                                     count = ingredient.count):
            return Response(status_code=202)
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Can't update Weather data",
            )

""" -------------------------- Storage -------------------------- """

@router.get('/storage', response_model=StorageDTO)
async def get_storage_by_id(id: int):
    """ Получение ingredient по id """
    with SessionLocal() as session:
        response = repository_service.get_storage_by_id(session, id)
    if response is None:
        return Response(status_code=204)
    return StorageDTO(ingredient_id=response.ingredient_id,
                      count=response.count,
                      expiry_date=response.expiry_date)

@router.delete('/storage', status_code=200)
async def del_storage_by_id(id: int):
    """ Удаление ingredient по id """
    with SessionLocal() as session:
        if repository_service.delete_storage_by_id(session, id):
            return Response(status_code=200)
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Can't delete Ingredient data",
            )

@router.post('/storage', status_code=201)
async def post_storage(ingredient: StorageDTO):
    """ Добавление ingredient """
    with SessionLocal() as session:
        if repository_service.create_storage(session, count=ingredient.count,
                                                 date=ingredient.expiry_date,
                                                 ingredient_id=ingredient.ingredient_id):
            repository_service.increace_ingredient_count_by_id(session, ingredient.ingredient_id, ingredient.count)
            return Response(status_code=201)
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Can't add new Ingredient data",
            )

@router.put('/storage', status_code=202)
async def put_storage_amount(id: int,ingredient: StorageDTO):
    """ Обновить Ingredients """
    with SessionLocal() as session:
        if repository_service.uprade_storage_amount_by_id(session,id=id,count=ingredient.count):
            return Response(status_code=202)
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Can't update Weather data",
            )

""" -------------------------- ORDERS_DISHES -------------------------- """

@router.get('/or_di_by_or/{id}', response_model=List[OrdersDishesDTO])
async def get_all_or_di_by_or(id: int):
    """ Получение всех записей OrderDishes по ID Order """
    or_di_data: List[OrdersDishesDTO] = []
    with SessionLocal() as session:
        result = repository_service.get_all_order_dish_by_order_id(session, id)
        for w in result:
            or_di_data.append(OrdersDishesDTO(id_order=w.id_order,
                                          id_dish=w.id_dish,
                                          amount=w.amount))
    return or_di_data

@router.get('/or_di_by_di/{id}', response_model=List[OrdersDishesDTO])
async def get_all_or_di_by_di(id: int):
    """ Получение всех записей OrderDishes по ID Dishes """
    or_di_data: List[OrdersDishesDTO] = []
    with SessionLocal() as session:
        result = repository_service.get_all_order_dish_by_dishes_id(session, id)
        for w in result:
            or_di_data.append(OrdersDishesDTO(id_order=w.id_order,
                                          id_dish=w.id_dish,
                                          amount=w.amount))
    return or_di_data

""" -------------------------- ПРИМЕРЫ -------------------------- """



# @router.get('/weatherforecast/{city_name}', response_model=List[WeatherDTO])
# async def get_all_weatherforecast_by_city_name(city_name: str):
#     """ Получение всех записей о погоде в населённом пункте """
#     return service.get_all_weather_in_city(city_name)
#
#
# @router.get('/weatherforecast', response_model=WeatherDTO)
# async def get_weatherforecast_by_city_id(city_id: int):
#     """ Получение записи о погоде в населенном пункте по идентификатору населенного пункта (необходим параметр ?city_id=) """
#     response = service.get_weather_in_city(city_id)
#     if response is None:
#         return Response(status_code=204)
#     return response
#
#
# @router.post('/weatherforecast', status_code=201)
# async def post_weatherforecast(weather: WeatherDTO):
#     """ Добавить новую запись о погоде """
#     if service.add_weather_info(weather):
#         return Response(status_code=201)
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="Can't add new Weather data",
#         )
#
#
# @router.put('/weatherforecast', status_code=202)
# async def put_weatherforecast(weather: WeatherDTO):
#     """ Обновить самую старую запись о погоде """
#     if service.update_weather_info(weather):
#         return Response(status_code=202)
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="Can't update Weather data",
#         )
#
#
# @router.delete('/weatherforecast/{city_name}', status_code=200)
# async def del_weatherforecast(city_name: str):
#     """ Удаление всех записей о погоде в населённом пункте """
#     if service.delete_weather_info_by_city_name(city_name):
#         return Response(status_code=200)
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="Can't delete Weather data",
#         )
#
#
# @router.post('/city', status_code=201)
# async def create_city(city: CityDTO) -> Response:
#     """ Добавить новый населённый пункт """
#     if service.add_city(city):
#         return Response(status_code=201)
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="Can't add new City data",
#         )
