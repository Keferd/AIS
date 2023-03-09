from pydantic import BaseModel
from typing import (
    Deque, Dict, List, Optional, Sequence, Set, Tuple, Union
)

from datetime import date

class StorageDTO(BaseModel):
    count: int
    expiry_date: date
    id_ingredient: int