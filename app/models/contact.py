from sqlalchemy import Column, Integer, String
from app.database import Base

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    user_phone = Column(String, nullable=False)
    service_name = Column(String, nullable=False)
    contact_type = Column(String)
