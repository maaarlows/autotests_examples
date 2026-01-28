import allure
from playwright.sync_api import expect

from fixtures.fixtures import name_generator
from db.db_check import check_new_sim
from api_methods.jwt import test_email, test_password
from selectors.auth_page import LOGIN_EMAIL, LOGIN_PASSWORD, SUBMIT_BUTTON
from selectors.navigation import MY_SIMS_BUTTON
from selectors.my_sims_page import ADD_BUTTON, ADD_SIM_HEADER, FIRST_NAME_INPUT, LAST_NAME_INPUT, SAVE_BUTTON, PERSONS

@allure.title('Successful sim creation')
@allure.description('')
@allure.tag('')
@allure.severity(allure.severity_level.CRITICAL)
def test_successful_sim_creation(page, name_generator):
    with allure.step('auth user'):
        page.goto("https://thesimstree.com/auth")
        page.fill(LOGIN_EMAIL, test_email)
        page.fill(LOGIN_PASSWORD, test_password)
        page.click(SUBMIT_BUTTON)
        page.wait_for_load_state("domcontentloaded")
    with allure.step('open my sims page'):
        page.click(MY_SIMS_BUTTON)
        page.wait_for_load_state("domcontentloaded")
    with allure.step('create a sim'):
        page.click(ADD_BUTTON)
        page.wait_for_selector(ADD_SIM_HEADER)
        first_name = name_generator[0]
        last_name = name_generator[1]
        page.fill(FIRST_NAME_INPUT, first_name)
        page.fill(LAST_NAME_INPUT, last_name)
        page.click(SAVE_BUTTON)
    with allure.step('check new sim'):
        expect(page.locator(PERSONS).get_by_text(f"{first_name} {last_name}")).to_be_visible()
    with allure.step('check new sim in db'):
        assert check_new_sim(first_name= first_name, last_name= last_name)
