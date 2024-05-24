from datetime import datetime


class Users:
    def __init__(self, id: int, name: str, cpf: str, email: str, phone_number: str, created_at: datetime, updated_at: datetime) -> None:

        self.id = id
        self.name = name
        self.cpf = cpf
        self.email = email
        self.phone_number = phone_number
        self.created_at = created_at
        self.updated_at = updated_at
