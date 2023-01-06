from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, Field


class DonoSchema(BaseModel):
    id: int
    name: str=Field(..., example="João")
    born_date: date
    email: str
    document: str
    phone_number: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class DonoSchemaCreate(BaseModel):
    name: str =Field(..., example="João")
    born_date: date=Field(..., example="01/05/1994")
    document: str
    email: str=Field(..., example="joao@gmail.com")
    phone_number: str

    class Config:
        orm_mode = True    
