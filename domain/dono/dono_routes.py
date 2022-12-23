from fastapi import APIRouter, status,HTTPException
from domain.dono.dono_schema import DonoSchema, DonoSchemaCreate
from typing import List

router = APIRouter()
donos = []

@router.post("/cadastro", response_model=bool)
def create_login(dono: DonoSchema):
    donos.append(dono)   
    return True


@router.get("/{id}", response_model=List [DonoSchema])
def list_users(id: int):
    return  donos


