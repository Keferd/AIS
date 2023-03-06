from pydantic import BaseModel
from typing import (
    Deque, Dict, List, Optional, Sequence, Set, Tuple, Union
)

from datetime import datetime


class WeatherDTO(BaseModel):
    """ DTO для добавления, обновления и получения информации о погоде.
        Если данные, передаваемые клиенту сильно отличаются от данных,
        которые принимает REST API сервера, необходимо разделять DTO
        для запросов и ответов, например, WeatherRequestDTO, WeatherResponseDTO """
    temperature_c: float
    temperature_f: Optional[float]      # объявление необязательного поля (may be None)
    pressure: int
    city_id: Optional[int]
    weather_type: Optional[int]
    updated_on: Optional[datetime]
