from pydantic import BaseModel
from typing import (
    Deque, Dict, List, Optional, Sequence, Set, Tuple, Union
)

from datetime import datetime

class OrdersDishesDTO(BaseModel):
    id_order: int
    id_dish: int
    amount: int