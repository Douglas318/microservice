from typing import Dict
from src.domain.use_cases.users.user_create import UserCreate as UserCreateInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.errors.types import HttpConflictError


class UserCreate(UserCreateInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def user_create(self, name: str, cpf: str, email: str, phone_number: str) -> Dict:
        self.__validate_user(cpf=cpf)
        self.__create_user(name=name, cpf=cpf, email=email, phone_number=phone_number)
        response = self.__format_response()
        return response

    def __validate_user(self, cpf: str) -> None:
        user = self.__users_repository.get_user_by_cpf(cpf=cpf)
        if user: raise HttpConflictError("O usuario informado já existe")

    def __create_user(self, name: str, cpf: str, email: str, phone_number: str) -> None:
        self.__users_repository.create_user(
            name=name,
            cpf=cpf,
            email=email,
            phone_number=phone_number
        )

    @classmethod
    def __format_response(cls) -> Dict:
        response = {
            "type": "Users",
            "message": "Usuario criado com sucesso"
        }

        return response
