from pydantic import BaseModel
from typing import (
    Deque, Dict, List, Optional, Sequence, Set, Tuple, Union
)

from datetime import datetime

class DishesDTO(BaseModel):
    name: str
    ingredients: Dict[int, int] = None
