from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()

accounts = []

class Dono(BaseModel):
    id: int
    nome: str
    documento: str
    dataNacimento: str
    email: str
    telefone: str

class Pet2(BaseModel):
    id: int
    nome: str
    documento: str
    dataNacimento: str
    email: str
    telefone: str


@app.get("/home")
def home():
    return("Bem vindo a PETSHOP DH")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8085, reload=True)
    