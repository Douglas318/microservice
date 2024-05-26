from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.users.user_create import UserCreate as UserCreateInterface


class UserCreateController(ControllerInterface):
    def __init__(self, use_case: UserCreateInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.body["name"] 
        cpf = http_request.body["cpf"]
        email = http_request.body["email"]
        phone_number = http_request.body["phone_number"]

        response = self.__use_case.user_create(
            name=name,
            cpf=cpf,
            email=email,
            phone_number=phone_number
        )
        return HttpResponse(status_code=200, body={"data": response})