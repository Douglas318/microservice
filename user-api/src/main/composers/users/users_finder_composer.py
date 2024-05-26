from src.infra.db.repositories.users_repository import UsersRepository
from src.data.use_cases.users.users_finder import UsersFinder
from src.presentation.controllers.users.users_finder_controller import UsersFinderController


def users_finder_composer():
    repository = UsersRepository()
    use_case = UsersFinder(repository)
    controller = UsersFinderController(use_case)

    return controller.handle