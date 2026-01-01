from sqlalchemy import Column, Integer, String
from app.database import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    user_phone = Column(String)
    service_name = Column(String)
    contact_type = Column(String)
