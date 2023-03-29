from pydantic import BaseModel
from typing import (
    Deque, Dict, List, Optional, Sequence, Set, Tuple, Union
)

from datetime import datetime

class IngredientsDTO(BaseModel):
    name: str
    count: int

class IngredientDTO(BaseModel):
    count: int

class IngredientssDTO(BaseModel):
    id: int
    name: str
    count: int