from __future__ import annotations
from typing import Optional, List
from pydantic import BaseModel

class User(BaseModel):
    user_id: Optional[str] = None
    name: Optional[str] = None
    password: Optional[str] = None
    age: Optional[int] = None
    sex: Optional[str] = None
    interest_list: Optional[List[str]] = None
