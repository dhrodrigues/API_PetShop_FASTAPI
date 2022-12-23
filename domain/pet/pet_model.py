from pydantic import BaseModel, Field
from typing import Dict, List, Optional


class Pet(BaseModel):
    id: int
    name: str=Field(..., example="João")
    raca: str=Field(..., example="Pit Bull")
    cor: str=Field(..., example="Branco")

