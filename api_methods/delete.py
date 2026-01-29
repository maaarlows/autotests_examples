import requests
from api_methods.config import URL
from api_methods.jwt import JWT


def delete_person(id: int) -> requests.Response:
    headers = {'Authorization': f'Bearer {JWT}'}
    response: requests.Response = requests.delete(f'{URL}person/{id}', headers=headers)
    return response

def delete_person_without_authorization(id: int) -> requests.Response:
    response: requests.Response = requests.delete(f'{URL}person/{id}')
    return response
