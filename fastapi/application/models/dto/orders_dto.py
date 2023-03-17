from pydantic import BaseModel
from typing import (
    Deque, Dict, List, Optional, Sequence, Set, Tuple, Union
)

from datetime import datetime


class OrdersDTO(BaseModel):
    dishes: Dict[int, int] = None
