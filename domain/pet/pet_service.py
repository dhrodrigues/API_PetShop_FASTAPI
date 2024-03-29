import json
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from domain.tutor.tutor_model import Tutor
from domain.pet.pet_model import Pet
from domain.pet.pet_repository import PetRepository
from domain.pet.pet_schema import PetSchema, PetSchemaCreate



def create(db: Session, body: PetSchemaCreate) -> PetSchema:
    tutor_id = int(body.tutor_id)
    tutor = PetRepository().filter_by_id(db, Tutor, tutor_id)
    if not tutor:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tutor não encontrado")
    pet = Pet(**body.dict())
    print(pet)
    return PetRepository().create(db, pet)


def get_pets(db: Session) -> PetSchema:
    return PetRepository().all(db, Pet)
    
def get_dono(db: Session, id: int) -> PetSchema:
    return PetRepository().filter_by_id(db, Tutor, id)  