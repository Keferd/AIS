from application.config import SessionLocal
from application.services.repository_service import *
import random


""" Данный скрипт заполняет БД тестовыми данными """


CITY = ['UFA', 'MOSCOW', 'SAINT-PETERSBURG']

WEATHER_TYPE = ['CLEAN', 'CLOUDY', 'RAIN']


def populate_city(db: Session) -> None:
    for city_name in CITY:
        add_city(db, city_name)


def populate_weather_type(db: Session) -> None:
    for weather_type_name in WEATHER_TYPE:
        add_weather_type(db, weather_type_name)


if __name__ == "__main__":
    with SessionLocal() as session:
        populate_city(session)
        populate_weather_type(session)
        create_weather(session, temp_c=random.uniform(20.0, 29.9), pressure=random.randint(735, 755), city_id=1, weather_type=1)
