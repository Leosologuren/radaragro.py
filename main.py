# FastAPI app entry point
from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "API do Radar Agro Online"}