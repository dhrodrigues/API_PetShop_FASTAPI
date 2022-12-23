from fastapi import FastAPI
from domain.dono import dono_routes
from domain.pet import pet_routes



def setup_routes(app: FastAPI):
    app.include_router(dono_routes.router,tags=["Cadastro Dono"], prefix="/cadastro_Dono")
    app.include_router(pet_routes.router,tags=["Cadastro Pet"], prefix="/cadastro_pet")