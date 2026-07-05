from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List

from app.database import init_db, get_db
from app.models import ContactModel, ContactSchema

app = FastAPI(title="The Contact Book API")

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/api/contacts", response_model=ContactSchema)
def create_contact(contact: ContactSchema, db: Session = Depends(get_db)):
    # Check if contact email already exists
    existing = db.query(ContactModel).filter(ContactModel.email == contact.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
        
    db_contact = ContactModel(name=contact.name, email=contact.email, phone=contact.phone)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

@app.get("/api/contacts", response_model=List[ContactSchema])
def read_contacts(db: Session = Depends(get_db)):
    return db.query(ContactModel).all()

# Serve static frontend UI files
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def read_root():
    return FileResponse("frontend/index.html")