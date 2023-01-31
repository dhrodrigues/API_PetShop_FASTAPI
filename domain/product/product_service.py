import json
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from domain.product.product_model import Product
from domain.pet.pet_model import Pet
from domain.product.product_repository import ProductRepository
from domain.product.product_schema import ProductSchema, ProductSchemaCreate



def create(db: Session, body: ProductSchemaCreate) -> ProductSchema:
    pet_id = int(body.pet_id)
    tutor = ProductRepository().filter_by_id(db, Pet, pet_id)
    if not tutor:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tutor não encontrado")
    service = Product(**body.dict())
    print(service)
    return ProductRepository().create(db, service)


def get_products(db: Session) -> ProductSchema:
    return ProductRepository().all(db, Product)
    