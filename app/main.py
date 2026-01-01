from fastapi import FastAPI
from app.database import engine
from app.models import User, Service, Contact, Category

app = FastAPI(title="neXo Cuba API")

# Crear las tablas en la base de datos
User.metadata.create_all(bind=engine)
Service.metadata.create_all(bind=engine)
Contact.metadata.create_all(bind=engine)
Category.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"mensaje": "API neXo Cuba funcionando correctamente"}
