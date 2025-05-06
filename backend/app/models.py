from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    full_name = Column(String)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Связи
    company = relationship("Company", back_populates="users")
    diagnoses = relationship("Diagnosis", back_populates="user")

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    tax_id = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Связи
    users = relationship("User", back_populates="company")
    stats = relationship("CompanyStats", back_populates="company")

class Diagnosis(Base):
    __tablename__ = "diagnoses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    input_text = Column(String)
    stress_probability = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Связи
    user = relationship("User", back_populates="diagnoses")

class CompanyStats(Base):
    __tablename__ = "company_stats"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    stat_date = Column(DateTime)
    avg_stress = Column(Float)
    total_diagnoses = Column(Integer)

    # Связи
    company = relationship("Company", back_populates="stats")