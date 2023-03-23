from pydantic import BaseModel
from typing import (
    Deque, Dict, List, Optional, Sequence, Set, Tuple, Union
)

from datetime import datetime

class DishesIngredientsDTO(BaseModel):
    id_dish = int
    id_ingredient = int
    count: int