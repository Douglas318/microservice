from src.infra.db.repositories.users_repository import UsersRepository
from src.data.use_cases.users.user_create import UserCreate
from src.presentation.controllers.users.user_create_controller import UserCreateController


def user_create_composer():
    repository = UsersRepository()
    use_case = UserCreate(repository)
    controller = UserCreateController(use_case)

    return controller.handle