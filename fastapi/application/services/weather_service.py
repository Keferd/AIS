from typing import Optional, List
from application.config import SessionLocal
from application.models.dao import Weather
from application.models.dto import WeatherDTO, CityDTO
import application.services.repository_service as repository_service


"""

    Данный модуль содержит программный слой с реализацией дополнительной бизнес-логики, 
    выполняемой перед или после выполнения операций над хранилищем данных (repository), 
    например: маппинг атрибутов из DAO в DTO, применение дополнительных функций к атрибутам DTO.
    
    ВАЖНО! Реализация данного слоя приведена в качестве демонстрации полной структуры RESTful веб-сервиса.
           В небольших проектах данный слой может быть избыточен, в таком случае, из контроллера ваших маршрутов 
           (Router в FastAPI или View в Django) можно напрямую работать с функциями хранилища данных (repository_service).

"""


class WeatherService:

    def get_weather_in_city(self, city_id: int) -> Optional[WeatherDTO]:
        result = None
        with SessionLocal() as session:     # конструкция with позволяет автоматически завершить сессию после выхода из блока
            result = repository_service.get_weather_by_city_id(session, city_id)
        if result is not None:
            return self.map_weather_data_to_dto(result)
        return result

    def get_all_weather_in_city(self, city_name: str) -> List[WeatherDTO]:
        weather_data: List[WeatherDTO] = []
        with SessionLocal() as session:
            result = repository_service.get_weather_by_city_name(session, city_name.upper())
            for w in result:
                weather_data.append(self.map_weather_data_to_dto(w))
        return weather_data

    def add_weather_info(self, weather: WeatherDTO) -> bool:
        with SessionLocal() as session:
            return repository_service.create_weather(session,
                                                     temp_c=weather.temperature_c,
                                                     pressure=weather.pressure,
                                                     city_id=weather.city_id,
                                                     weather_type=weather.weather_type)

    def update_weather_info(self, weather: WeatherDTO) -> bool:
        with SessionLocal() as session:
            return repository_service.update_weather_temp_and_pressure(session,
                                                                       temp_c=weather.temperature_c,
                                                                       pressure=weather.pressure,
                                                                       city_id=weather.city_id)

    def delete_weather_info_by_city_name(self, city_name: str) -> bool:
        with SessionLocal() as session:
            return repository_service.delete_weather_by_city_name(session, city_name.upper())

    def add_city(self, city: CityDTO) -> bool:
        if city.name != "":
            with SessionLocal() as session:
                return repository_service.add_city(session, city_name=city.name.upper())
        return False

    def map_weather_data_to_dto(self, weather_dao: Weather):
        """ Метод для конвертирования (маппинга) Weather DAO в WeatherDTO """
        return WeatherDTO(temperature_c=weather_dao.temperature_c,
                          temperature_f=weather_dao.temperature_f,
                          pressure=weather_dao.pressure,
                          city_id=weather_dao.city,
                          weather_type=weather_dao.type,
                          updated_on=weather_dao.updated_on)
