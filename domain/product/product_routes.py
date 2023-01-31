from typing import List
from fastapi import Depends
from fastapi.routing import APIRouter
from config.database import get_db
from fastapi import status,HTTPException
from sqlalchemy.orm.session import Session
from domain.product.product_schema import ProductSchema, ProductSchemaCreate
from domain.product import product_service

router = APIRouter()

@router.get("/",
            summary="Operação tutor por retornar todos os animais cadastrados.",
            response_model=List[ProductSchema])
def get_products(db: Session = Depends(get_db)):
    return product_service.get_products(db)

@router.post("/",
             summary="Operação responsável por cadastrar novos pets.",
             response_model=ProductSchema)
def create_pet(body: ProductSchemaCreate, db: Session = Depends(get_db)):
    return product_service.create(db, body)