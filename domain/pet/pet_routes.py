from typing import List
from fastapi import Depends
from fastapi.routing import APIRouter
from config.database import get_db
from fastapi import status,HTTPException
from sqlalchemy.orm.session import Session
from domain.pet.pet_schema import PetSchema, PetSchemaCreate
from domain.pet import pet_service

router = APIRouter()

@router.get("/",
            summary="Operação responsável por retornar todos os animais cadastrados.",
            response_model=List[PetSchema])
def get_pets(db: Session = Depends(get_db)):
    return pet_service.get_pets(db)

@router.post("/",
             summary="Operação responsável por cadastrar novos pets.",
             response_model=PetSchema)
def create_pet(body: PetSchemaCreate, db: Session = Depends(get_db)):
    return pet_service.create(db, body)
