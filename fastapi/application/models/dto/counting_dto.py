from pydantic import BaseModel
from typing import (
    Deque, Dict, List, Optional, Sequence, Set, Tuple, Union
)

class CountingDTO(BaseModel):
    ingredient_id: int
    delivery_count: int