from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError


def user_create_validator(request: any):
    body_validator = Validator(
        {
            "name": {"type": "string", "required": True, "empty": False},
            "cpf": {"type": "string", "required": True, "empty": False},
            "email": {"type": "string", "required": True, "empty": False},
            "phone_number": {"type": "string", "required": True, "empty": False}
        }
    )

    response = body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)