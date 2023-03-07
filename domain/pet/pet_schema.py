from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from domain.tutor.tutor_schema import TutorSchema


class PetSchema(BaseModel):
    id: int
    name: str=Field(..., example="Billy")
    raca: str=Field(..., example="Pit Bull")
    cor: str=Field(..., example="Branco")
    tutor: Optional[TutorSchema]
    destination_pet: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True


class PetSchemaCreate(BaseModel):
    name: str=Field(..., example="Billy")
    raca: str=Field(..., example="Pit Bull")
    cor: str=Field(..., example="Branco")
    tutor_id: int=Field(..., example=1)
    destination_pet: str=Field(..., example="diego@gmail.com")

    class Config:
        orm_mode = True    
        
        
