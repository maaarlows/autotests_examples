import requests
from api_methods.config import URL


def get_person(id: int) -> requests.Response:
    response: requests.Response = requests.get(f'{URL}person/{id}')
    return response
