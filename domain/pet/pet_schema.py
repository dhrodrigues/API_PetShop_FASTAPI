from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, Field


class PetSchema(BaseModel):
    id: int
    name: str=Field(..., example="João")
    raca: str=Field(..., example="Pit Bull")
    cor: str=Field(..., example="Branco")
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True


class PetSchemaCreate(BaseModel):
    name: str
    document: str
    email: str
    phone_number: str

    class Config:
        orm_mode = True    