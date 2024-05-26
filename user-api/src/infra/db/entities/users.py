import hashlib
from sqlalchemy import Column, Integer, String, DateTime, VARBINARY, func
from src.infra.db.settings.base import Base


class Users(Base):
    def __init__(self, name: str, cpf: str, email: str, phone_number: str):
        self.name = name
        self.cpf = hashlib.sha256(cpf.encode()).hexdigest()
        self.email = hashlib.sha256(email.encode()).hexdigest()
        self.phone_number = hashlib.sha256(phone_number.encode()).hexdigest()

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(36), unique=True)
    cpf = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone_number = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
