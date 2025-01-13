import pytest
import allure
import api_methods


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