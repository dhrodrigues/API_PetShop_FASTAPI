import uvicorn
from typing import Dict
from fastapi import FastAPI
from config.routes import setup_routes


app = FastAPI()
setup_routes(app)

@app.get("/")
def root() -> str:
    return "Welcome to New Life Bank"

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=20050, reload=True)
    