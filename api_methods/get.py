import requests


URL: str = 'https://app.thesimstree.com/api/'


def get_person(id: int) -> requests.Response:
    response: requests.Response = requests.get(f'{URL}person/{id}')
    return response
