from fastapi import Header, HTTPException

ADMIN_KEY = "NEXO_ADMIN_123"

def verify_admin(x_admin_key: str):
    if x_admin_key != ADMIN_KEY:
        raise HTTPException(status_code=403, detail="Acceso denegado")
