from app.routes.admin import verify_admin
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.contact import Contact
from app.schemas.contact import ContactCreate, ContactResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ContactResponse)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

@router.get("/", response_model=list[ContactResponse])
def list_contacts(db: Session = Depends(get_db)):
    contacts = db.query(Contact).all()
    return contacts
