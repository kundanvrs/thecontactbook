from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class ContactModel(Base):
    __tablename__ = "contacts"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, index=True, nullable=False)

# Pydantic Schemas for validation
class ContactSchema(BaseModel):
    name: str
    email: str
    phone: str

    class Config:
        from_attributes = True