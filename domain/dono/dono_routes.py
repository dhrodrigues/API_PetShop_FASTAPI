from typing import List
from fastapi import Depends
from fastapi.routing import APIRouter
from config.database import get_db
from fastapi import status,HTTPException
from sqlalchemy.orm.session import Session
from domain.dono.dono_schema import DonoSchema, DonoSchemaCreate
from domain.dono import dono_service

router = APIRouter()

@router.post("/", summary="Operação responsável por criar uma nova conta.",response_model=DonoSchema)
def create_account(body: DonoSchemaCreate, db: Session = Depends(get_db)):
    return dono_service.create(db, body)

@router.get("/{id}", summary= "Operação por retornar apenas um dono", response_model=List[DonoSchema])
def get_user(id:int, db: Session = Depends(get_db)):
    return dono_service.get_dono(db, id)

@router.get("/",
            summary="Lista usuarios.",
            response_model=List[DonoSchema])
def get_users(db: Session = Depends(get_db)):
    return dono_service.get_donos(db)




#Inicio do codigo.

# @router.post("/cadastro", response_model=bool)
# def create_login(user: DonoSchemaCreate):
#     for users in donos:
#         if user.id == users:
#             raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="erro")
#     donos.append(user)   
#     return True


# @router.get("/listusers", response_model=List [DonoSchemaCreate])
# def list_users():
#     return  donos
