from fastapi import FastAPI
from .models import Base
from .database import engine

app = FastAPI()

# Создаем таблицы при старте приложения
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Таблицы успешно созданы!"}