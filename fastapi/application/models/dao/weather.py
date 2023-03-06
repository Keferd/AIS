from sqlalchemy import Column, ForeignKey, Boolean, Integer, Numeric, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from datetime import datetime


# Объявление декларативного (описательного) метода представления БД
Base = declarative_base()


class Weather(Base):
    """ Описание сущности (таблицы) weather """
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True)      # объявление первичного ключа
    _temperature_c = Column('temperature_c', Numeric, nullable=False)       # поле не может быть пустым (NULL)
    temperature_f = Column(Numeric)
    pressure = Column(Integer)
    # связь полей type и city через внешние ключи
    type = Column(Integer, ForeignKey('weather_type.id'), nullable=False)   # объявление ограничения по внешнему ключу
    """ 
     При использовании конструкции relationship("ИМЯ_СВЯЗАННОГО_ОБЪЕКТА") по соответствующему имени атрибута можно
     будет получить свзязанный объект (в данном примере, если после SELECT мы получили объект w типа Weather, то
     связанный с ним объект объект WeatherType можно будет получить через атрибут w.weather_type, а необходимое
     значение, соответственно: w.weather_type.type). Подробнее см.: https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
    """
    weather_type = relationship('WeatherType')
    city = Column(Integer, ForeignKey('city.id'), nullable=False)
    city_name = relationship('City')
    created_on = Column(DateTime(), default=datetime.now)      # в поле автоматически генерируется метка времени при создании записи
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)    # в поле автоматически генерируется метка времени при создании записи, метка обновляется при каждой операции UPDATE

    @hybrid_property
    def temperature_c(self):
        """ Декоратор @hybrid_property позволяет добавить какую-нибудь бизнес-логику или проверку
            при установке данному полю какого-либо значения. Подробнее см.:
            https://docs.sqlalchemy.org/en/14/orm/extensions/hybrid.html#sqlalchemy.ext.hybrid.hybrid_property """
        return self._temperature_c

    @temperature_c.setter
    def temperature_c(self, temperature_c: float):
        """ При установке значения полю temperature_c будет автоматически рассчитано значение temperature_f """
        self.temperature_f = 32.0 + (temperature_c / 0.5556)
        self._temperature_c = temperature_c

    def __repr__(self):
        """ Переопределяем строковое представление объекта (см. python magic methods)"""
        return f'{self.__dict__}'


class WeatherType(Base):
    """ Тип погоды ("Ясно", "Облачно" и т.п.) """
    __tablename__ = "weather_type"

    id = Column(Integer, primary_key=True)
    type = Column(String(255), nullable=False, unique=True)      # значение этого поля не может повторяться


class City(Base):
    """ Таблица с наименованиями населённых пунктов """
    __tablename__ = "city"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
