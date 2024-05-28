from orders.settings import USERS_URL
from typing import Dict
import requests


def get_data(endpoint) -> requests.Response:
    try:
        response = requests.get(f"{USERS_URL}{endpoint}")
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as exception:
        print(f'[ERROR]: USERS API: {endpoint} - {str(error)}')
        return requests.Response()
