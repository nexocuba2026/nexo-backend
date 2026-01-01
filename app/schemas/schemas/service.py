from pydantic import BaseModel

class ServiceCreate(BaseModel):
    name: str
    description: str
    category: str

class ServiceResponse(BaseModel):
    id: int
    name: str
    description: str
    category: str

    class Config:
        orm_mode = True
