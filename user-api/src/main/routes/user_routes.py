from flask import Blueprint, request, jsonify

from src.main.adapters.request_adapter import request_adapter
from src.errors.error_handler import handle_errors
from src.main.composers.users.user_finder_composer import user_finder_composer
from src.main.composers.users.users_finder_composer import users_finder_composer
from src.main.composers.users.user_create_composer import user_create_composer
from src.main.composers.users.user_delete_composer import user_delete_composer


from src.validators.users.user_finder_validator import user_finder_validator
from src.validators.users.user_create_validator import user_create_validator

users_route_bp = Blueprint("users_route", __name__, url_prefix="/users")

@users_route_bp.route("", methods=['GET'])
def list_users():
    http_response = None
    try:
        http_response = request_adapter(request, users_finder_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    return jsonify(http_response.body), http_response.status_code

@users_route_bp.route("/display", methods=['GET'])
def display():
    http_response = None
    try:
        user_finder_validator(request)
        http_response = request_adapter(request, user_finder_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    return jsonify(http_response.body), http_response.status_code


@users_route_bp.route("/create/", methods=["POST"])
def create():
    http_response = None
    try:
        user_create_validator(request)
        http_response = request_adapter(request, user_create_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    return jsonify(http_response.body), http_response.status_code


@users_route_bp.route("/delete", methods=['DELETE'])
def delete():
    http_response = None
    try:
        user_finder_validator(request)
        http_response = request_adapter(request, user_delete_composer())
    except Exception as exception:
        http_response = handle_errors(exception)
    return jsonify(http_response.body), http_response.status_code