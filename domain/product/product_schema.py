from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from domain.pet.pet_schema import PetSchema


class ProductSchema(BaseModel):
    id: int
    serviço: str=Field(..., example="Billy")
    data: str=Field(..., example="YYYY-MM-DD")
    Pet: Optional[PetSchema]    
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True


class ProductSchemaCreate(BaseModel):
    serviço: str=Field(..., example="Billy")
    data: str=Field(..., example="YYYY-MM-DD")
    pet_id: int=Field(..., example=1)


    class Config:
        orm_mode = True    
        
        
