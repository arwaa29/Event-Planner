from typing import Literal
from pydantic import BaseModel

class UpdateStatus(BaseModel):
        event_id: str
        status: Literal["Going", "Maybe", "Not Going"]