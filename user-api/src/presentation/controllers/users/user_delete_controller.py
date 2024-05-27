from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.users.user_delete import UserDelete as UserDeleteInterface


class UserDeleteController(ControllerInterface):
    def __init__(self, use_case: UserDeleteInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.query_params["user_id"]

        response = self.__use_case.user_delete(user_id=user_id)
        return HttpResponse(status_code=200, body={"data": response})