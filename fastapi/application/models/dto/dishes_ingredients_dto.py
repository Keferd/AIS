from pydantic import BaseModel
from typing import (
    Deque, Dict, List, Optional, Sequence, Set, Tuple, Union
)

from datetime import datetime

class DishesIngredientsDTO(BaseModel):
    dish_id = int
    ingredient_id = int
    amount: int