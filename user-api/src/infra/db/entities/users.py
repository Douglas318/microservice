import bcrypt
from sqlalchemy import Column, Integer, String, DateTime, VARBINARY, func
from src.infra.db.settings.base import Base


class Users(Base):
    def __init__(self, name: str, cpf: str, email: str, phone_number: str) -> None:
        self.name = name
        self.cpf = cpf
        self.email = email
        self.phone_number = phone_number

    @property
    def cpf(self) -> str:
        return self.__decrypt(self._cpf)

    @cpf.setter
    def cpf(self, value: str) -> None:
        self._cpf = self.__encrypt(value)

    @property
    def email(self) -> str:
        return self.__decrypt(self._email)

    @email.setter
    def email(self, value: str) -> None:
        self._email = self.__encrypt(value)

    @property
    def phone_number(self) -> str:
        return self.__decrypt(self._phone_number)

    @phone_number.setter
    def phone_number(self, value: str) -> None:
        self._phone_number = self.__encrypt(value)

    @staticmethod
    def __encrypt(value: str) -> bytes:
        return bcrypt.hashpw(value.encode("utf-8"), bcrypt.gensalt())

    @staticmethod
    def __decrypt(value: bytes) -> str:
        return value.decode("utf-8")

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(36), unique=True)
    _cpf = Column("cpf", VARBINARY(100), nullable=False)
    _email = Column("email", VARBINARY(100), nullable=False)
    _phone_number = Column("phone_number", VARBINARY(100), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
