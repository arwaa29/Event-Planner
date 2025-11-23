from pydantic import BaseModel
from typing import Optional

class SearchFilters(BaseModel):
    title: Optional[str]
    date: Optional[str]
    description: Optional[str]
    role: Optional[str]

    model_config = {
    "from_attributes": True
    }