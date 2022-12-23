from pydantic import BaseModel, Field
from typing import Dict, List, Optional


class Dono(BaseModel):
    id: int
    name: str=Field(..., example="João")
    document: str
    bornDate: str
    email: str
    phoneNumber: Optional[str]
    telefone: str
