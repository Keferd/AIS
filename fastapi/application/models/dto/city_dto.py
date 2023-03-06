from pydantic import BaseModel


class CityDTO(BaseModel):
    """ DTO для добавления нового населённого пункта """
    name: str
