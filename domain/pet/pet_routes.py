from fastapi import APIRouter, status,HTTPException
from domain.pet.pet_model import Pet

router = APIRouter()
pet = []


@router.post("/cadastro", response_model=bool)
def create_login(dono: Pet):
    pet.append(dono)   
    return True

@router.get("/accounts", response_model=list)
def list_users():
    return  pet
