from pydantic import BaseModel
from typing import (
    Deque, Dict, List, Optional, Sequence, Set, Tuple, Union
)

class NewOrdersDTO(BaseModel):
    dishes: Dict[int, int] = None
