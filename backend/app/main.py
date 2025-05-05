from fastapi import FastAPI
from .models import Base
from .database import engine

app = FastAPI()

# Инициализация БД
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Stress Detection API"}