import bcrypt
from sqlalchemy import Column, Integer, String, DateTime, VARBINARY, func
from src.infra.db.settings.base import Base


class Users(Base):
    def __init__(self, name: str, cpf: str, email: str, phone_number: str) -> None:
        self.name = name
        self.cpf = bcrypt.hashpw(cpf.encode("utf-8"), bcrypt.gensalt())
        self.email = bcrypt.hashpw(email.encode("utf-8"), bcrypt.gensalt())
        self.phone_number = bcrypt.hashpw(phone_number.encode("utf-8"), bcrypt.gensalt())

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(36), unique=True)
    cpf = Column(VARBINARY(100), nullable=False)
    email = Column(VARBINARY(100), nullable=False)
    phone_number = Column(VARBINARY(100), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
