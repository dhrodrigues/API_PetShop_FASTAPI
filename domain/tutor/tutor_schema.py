from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, Field


class TutorSchema(BaseModel):
    id: int
    name: str=Field(..., example="Diego")
    born_date: date
    email: str
    document: str
    phone_number: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class TutorSchemaCreate(BaseModel):
    name: str =Field(..., example="João")
    born_date: date=Field(..., example="AAAA-MM-DD")
    document: str
    email: str=Field(..., example="joao@gmail.com")
    phone_number: str

    class Config:
        orm_mode = True    
