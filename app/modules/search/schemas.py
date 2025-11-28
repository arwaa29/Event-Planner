from pydantic import BaseModel
from typing import Optional

class EventSearch(BaseModel):
    keyword: Optional[str] = None
    date: Optional[str] = None
    role: Optional[str] = None
