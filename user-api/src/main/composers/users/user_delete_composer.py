from src.infra.db.repositories.users_repository import UsersRepository
from src.data.use_cases.users.user_delete import UserDelete
from src.presentation.controllers.users.user_delete_controller import UserDeleteController


def user_delete_composer():
    repository = UsersRepository()
    use_case = UserDelete(repository)
    controller = UserDeleteController(use_case)

    return controller.handle