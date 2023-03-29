from pydantic import BaseModel
from typing import (
    Deque, Dict, List, Optional, Sequence, Set, Tuple, Union
)

from datetime import datetime

class StorageDTO(BaseModel):
    count: int
    expiry_date: datetime
    ingredient_id: int

class StoragesDTO(BaseModel):
    id: int
    count: int
    date: datetime
    id_ingredient: int