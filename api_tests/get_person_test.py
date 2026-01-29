import pytest
import allure
import api_methods
from fixtures.fixtures import name_generator


PERSON_IDS = [68300, 293100, 68271, 68263, 68246]


@allure.title('Get person info by id = {person_id}')
@allure.description('')
@allure.tag('')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('person_id', PERSON_IDS)
def test_get_person_by_id(person_id):
    with allure.step(f'get {person_id} info by request'):
        get_person_response = api_methods.get.get_person(id=person_id)
        assert get_person_response.status_code == 200, f'ne 200, a {get_person_response.status_code}'
        get_person_body = get_person_response.json()
    with allure.step('check info'):
        assert get_person_body['id'] == person_id, f'person_id != {person_id}, actual {get_person_body['id']}'
        assert type(get_person_body['id']) == int, f'person_id != int'


@allure.title('Get deleted person')
@allure.description('')
@allure.tag('')
@allure.severity(allure.severity_level.CRITICAL)
def test_get_deleted_person_by_id(name_generator):
    first_name = name_generator[0]
    last_name = name_generator[1]
    with allure.step('create person request'):
        create_person_request = api_methods.post.create_person(first_name=first_name, last_name=last_name)
        assert create_person_request.status_code == 200, f'ne 200, a {create_person_request.status_code}'
        create_person_body = create_person_request.json()
    with allure.step('get person request'):
        get_person_response = api_methods.get.get_person(id=create_person_body['id'])
        assert get_person_response.status_code == 200, f'ne 200, a {get_person_response.status_code}'
    with allure.step('delete person request'):
        delete_person_request = api_methods.delete.delete_person(id=create_person_body['id'])
        assert delete_person_request.status_code == 204, f'ne 200, a {delete_person_request.status_code}'
    with allure.step('get deleted person request'):
        get_person_response = api_methods.get.get_person(id=create_person_body['id'])
        assert get_person_response.status_code == 404, f'ne 404, a {get_person_response.status_code}'