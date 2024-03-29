from fastapi import FastAPI
from domain.tutor import tutor_routes
from domain.pet import pet_routes
#from domain.product import product_routes


def setup_routes(app: FastAPI):
    app.include_router(tutor_routes.router,tags=["Cadastro Dono"], prefix="/cadastro_dono")
    app.include_router(pet_routes.router,tags=["Cadastro Pet"], prefix="/cadastro_pet")
    #app.include_router(product_routes.router,tags=["Solicitar Serviços"], prefix="/serviços")