from typing import Dict, List
from src.domain.use_cases.users.users_finder import UsersFinder as UsersFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users
from src.errors.types import HttpBadRequestError


class UsersFinder(UsersFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def listing(self) -> Dict:
        users = self.__search_users()
        response = self.__format_response(user=users)
        return response

    def __search_users(self) -> List[Users]:
        users = self.__users_repository.select_users()
        if users:
            return users
        raise HttpBadRequestError("Usuarios não encontrados")

    @classmethod
    def __format_response(cls, users: Users) -> Dict:
        response = {
            "type": "Users",
            "message": "Usuarios encontrados com sucesso!",
            "users": users,
        }

        return response