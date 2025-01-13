import allure
import api_methods
from fixtures.fixtures import name_generator


@allure.title('Create person')
@allure.description('')
@allure.tag('')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_person(name_generator):
    first_name = name_generator[0]
    last_name = name_generator[1]
    with allure.step('create person request'):
        create_person_request = api_methods.post.create_person(first_name=first_name, last_name=last_name)
        assert create_person_request.status_code == 200, f'ne 200, a {create_person_request.status_code}'
        create_person_body = create_person_request.json()
    with allure.step('check info'):
        assert create_person_body['first_name'] == first_name, f'first_name != {first_name}, actual {create_person_body['first_name']}'
        assert create_person_body['last_name'] == last_name, f'last_name != {last_name}, actual {create_person_body['last_name']}'


@allure.title('Create person without authorization')
@allure.description('')
@allure.tag('')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_person_without_authorization(name_generator):
    first_name = name_generator[0]
    last_name = name_generator[1]
    with allure.step('create person without authorization'):
        create_person_without_authorization = api_methods.post.create_person_without_authorization(first_name=first_name, last_name=last_name)
        assert create_person_without_authorization.status_code == 401, f'ne 401, a {create_person_without_authorization.status_code}'


@allure.title('Create person without body')
@allure.description('')
@allure.tag('')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_person_without_body():
    with allure.step('create person without body request'):
        create_person_without_body_request = api_methods.post.create_person_without_body()
        assert create_person_without_body_request.status_code == 400, f'ne 400, a {create_person_without_body_request.status_code}'
