import json
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from domain.dono.dono_model import Dono
from domain.pet.pet_model import Pet
from domain.pet.pet_repository import PetRepository
from domain.pet.pet_schema import PetSchema, PetSchemaCreate



def create(db: Session, body: PetSchemaCreate) -> PetSchema:
    dono_id = int(body.dono_id)
    tutor = PetRepository().filter_by_id(db, Dono, dono_id)
    if not tutor:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario não encontrado")
    peti = Pet(**body.dict())
    print(peti)
    return PetRepository().create(db, peti)


def get_pets(db: Session) -> PetSchema:
    return PetRepository().all(db, Pet)
    