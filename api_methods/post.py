import requests
from api_methods.config import URL
from api_methods.jwt import JWT


def create_person(first_name: str, last_name: str) -> requests.Response:
    payload = {
        'last_name': last_name,
        'first_name': first_name
    }
    headers = {'Authorization': f'Bearer {JWT}'}
    response: requests.Response = requests.post(f'{URL}person', data=payload, headers=headers)
    return response

def create_person_without_body() -> requests.Response:
    headers = {'Authorization': f'Bearer {JWT}'}
    response: requests.Response = requests.post(f'{URL}person', headers=headers)
    return response

def create_person_without_authorization(first_name: str, last_name: str) -> requests.Response:
    payload = {
        'last_name': last_name,
        'first_name': first_name
    }
    response: requests.Response = requests.post(f'{URL}person', data=payload)
    return response
