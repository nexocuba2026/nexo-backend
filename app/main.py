from fastapi import FastAPI
from app.database import engine
from app.models.user import User
from app.models.service import Service
from app.models.contact import Contact
from app.models.category import Category
from app.routes import services, contacts, admin, auth

app = FastAPI(title="neXo Cuba API")

# Crear tablas
User.metadata.create_all(bind=engine)
Service.metadata.create_all(bind=engine)
Contact.metadata.create_all(bind=engine)
Category.metadata.create_all(bind=engine)

# Registrar routers
app.include_router(services.router, prefix="/services", tags=["services"])
app.include_router(contacts.router, prefix="/contacts", tags=["contacts"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
def root():
    return {"mensaje": "API neXo Cuba funcionando correctamente"}
