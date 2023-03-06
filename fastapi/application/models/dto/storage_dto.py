from pydantic import BaseModel
from typing import (
    Deque, Dict, List, Optional, Sequence, Set, Tuple, Union
)

from datetime import datetime

class StorageDTO(BaseModel):
    batch_number: int
    count: int
    expiry_date: datetime