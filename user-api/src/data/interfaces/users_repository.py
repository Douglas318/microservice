from abc import ABC, abstractmethod
from src.domain.models.users import Users
from typing import List


class UsersRepositoryInterface(ABC):
    @abstractmethod
    def select_users(self) -> List[Users]:
        pass

    @abstractmethod
    def select_user(self, user_id: int) -> Users | None:
        pass

    @abstractmethod
    def create_user(self, name: str, cpf: str, email: str, phone_number: str) -> None:
        pass

    @abstractmethod
    def update_user(self, user_id: int, email: str, phone_number: str) -> None:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        pass

    @abstractmethod
    def get_user_by_cpf(self, cpf: str) -> bool:
        pass