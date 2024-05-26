from abc import ABC, abstractmethod
from typing import Dict


class UserCreate(ABC):
    @abstractmethod
    def user_create(self, name: str, cpf: str, email: str, phone_number: str) -> Dict:
        pass
