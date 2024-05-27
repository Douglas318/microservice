from typing import Dict
from src.domain.use_cases.users.user_delete import UserDelete as UserDeleteInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users
from src.errors.types import HttpBadRequestError


class UserDelete(UserDeleteInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def user_delete(self, user_id: int) -> Dict:
        user = self.__search_user(user_id=user_id)
        delete = self.__delete(user=user)
        response = self.__format_response()
        return response

    def __search_user(self, user_id: int) -> Users:
        user = self.__users_repository.select_user(user_id=user_id)
        if user is None:
            raise HttpBadRequestError("Usuario não encontrado")
        return user

    def __delete(self, user: Users) -> None:
        user = self.__users_repository.delete_user(user.id)

    @classmethod
    def __format_response(cls) -> Dict:
        response = {
            "type": "Users",
            "message": "Usuario apagado com sucesso!",
        }

        return response