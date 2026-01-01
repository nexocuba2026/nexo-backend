from pydantic import BaseModel

class ContactCreate(BaseModel):
    user_phone: str
    service_name: str
    contact_type: str

class ContactResponse(BaseModel):
    id: int
    user_phone: str
    service_name: str
    contact_type: str

    class Config:
        orm_mode = True
