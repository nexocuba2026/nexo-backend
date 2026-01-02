from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceResponse
from app.routes.admin import verify_admin

router = APIRouter()

# Dependencia de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# LISTAR SERVICIOS (PUBLICO)
@router.get("/", response_model=list[ServiceResponse])
def list_services(db: Session = Depends(get_db)):
    services = db.query(Service).all()
    return services


# CREAR SERVICIO (SOLO ADMIN)
@router.post("/", response_model=ServiceResponse)
def create_service(
    service: ServiceCreate,
    x_admin_key: str = Header(...),
    db: Session = Depends(get_db),
):
    verify_admin(x_admin_key)

    db_service = Service(
        name=service.name,
        description=service.description,
        category=service.category
    )

    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service


# OBTENER SERVICIO POR ID (PUBLICO)
@router.get("/{service_id}", response_model=ServiceResponse)
def get_service(service_id: int, db: Session = Depends(get_db)):
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return service
