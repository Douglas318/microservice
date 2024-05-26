from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.users.users_finder import UsersFinder as UsersFinderInterface


class UsersFinderController(ControllerInterface):
    def __init__(self, use_case: UsersFinderInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        response = self.__use_case.users_finder()
        return HttpResponse(status_code=200, body={"data": response})
