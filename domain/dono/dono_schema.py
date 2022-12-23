from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, Field


class DonoSchema(BaseModel):
    id: int
    name: str=Field(..., example="João")
    document: str
    bornDate: str
    email: str
    phoneNumber: Optional[str]
    telefone: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True


class DonoSchemaCreate(BaseModel):
    name: str
    document: str
    email: str
    phone_number: str

    class Config:
        orm_mode = True    