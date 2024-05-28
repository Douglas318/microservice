from typing import Dict
from src.domain.use_cases.users.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users
from src.errors.types import HttpBadRequestError


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository
    
    def user_finder(self, user_id: int) -> Dict:
        user = self.__search_user(user_id=user_id)
        response = self.__format_response(user=user)
        return response

    def __search_user(self, user_id: int) -> Users:
        user = self.__users_repository.select_user(user_id=user_id)
        if user is None:
            raise HttpBadRequestError("Usuario não encontrado")
        return user
        

    @classmethod
    def __format_response(cls, user: Users) -> Dict:
        user_values = {
            "name": user.name,
            "cpf": user.cpf,
            "email": user.email,
            "phone_number": user.phone_number
        }
        response = {
            "type": "Users",
            "message": "Usuario encontrado com sucesso!",
            "user": user_values,
        }

        return response