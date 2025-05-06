from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Формат подключения: postgresql://user:password@host/dbname
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:littleeov@localhost/stress_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()