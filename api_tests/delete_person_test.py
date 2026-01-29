import allure
import api_methods
from fixtures.fixtures import name_generator


@allure.title('Delete person')
@allure.description('')
@allure.tag('')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_person(name_generator):
    first_name = name_generator[0]
    last_name = name_generator[1]
    with allure.step('create person request'):
        create_person_request = api_methods.post.create_person(first_name=first_name, last_name=last_name)
        assert create_person_request.status_code == 200, f'ne 200, a {create_person_request.status_code}'
        create_person_body = create_person_request.json()
    with allure.step('delete person request'):
        delete_person_request = api_methods.delete.delete_person(id=create_person_body['id'])
        assert delete_person_request.status_code == 204, f'ne 200, a {delete_person_request.status_code}'


@allure.title('Delete person without authorization')
@allure.description('')
@allure.tag('')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_person_without_authorization(name_generator):
    first_name = name_generator[0]
    last_name = name_generator[1]
    with allure.step('create person request'):
        create_person_request = api_methods.post.create_person(first_name=first_name, last_name=last_name)
        assert create_person_request.status_code == 200, f'ne 200, a {create_person_request.status_code}'
        create_person_body = create_person_request.json()
    with allure.step('delete person request'):
        delete_person_without_authorization_request = api_methods.delete.delete_person_without_authorization(id=create_person_body['id'])
        assert delete_person_without_authorization_request.status_code == 401, f'ne 200, a {delete_person_without_authorization_request.status_code}'
