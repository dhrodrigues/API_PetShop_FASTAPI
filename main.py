from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI
from datetime import datetime
from typing import Dict


app = FastAPI()

donos = []

class Dono(BaseModel):
    id: int
    nome: str
    documento: str
    dataNacimento: str
    email: str
    telefone: str




@app.get("/health")
def alive() -> Dict[str, datetime]:
    return {"timestamp": datetime.now()}

@app.post("/cadastro", response_model=bool, tags=["cadastro"])
def create_login(dono: Dono):
    donos.append(dono)   
    return True

@app.get("/accounts", response_model=list, tags=["users"])
def list_users():
    return  donos

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8085, reload=True)
    