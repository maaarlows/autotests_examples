import allure

from db.db_check import is_user_pro, clear_subscription
from db.db_conn import db_connect
from fixtures.fixtures import ensure_russian_ui
from api_methods.config import url_auth, url_tbank, url_main_page

from api_methods.jwt import test_email, test_password, test_number_tbank, test_code_tbank, test_date_tbank, err_number_tbank
from selectors.auth_page import LOGIN_EMAIL, LOGIN_PASSWORD, SUBMIT_BUTTON, TRY_PRO_BUTTON, TO_BUY, PLANS
from selectors.tbank_page import CARD_NUMBER, CARD_DATE, CARD_CODE, SUBMIT_TBANK, ERR, SAVE_CARD


@allure.title('Successful tbank payment')
@allure.description('')
@allure.tag('')
@allure.severity(allure.severity_level.CRITICAL)
def test_successful_tbank_payment(page):
    with allure.step('auth user'):
        page.goto(url_auth)
        page.fill(LOGIN_EMAIL, test_email)
        page.fill(LOGIN_PASSWORD, test_password)
        page.click(SUBMIT_BUTTON)
        page.wait_for_load_state("domcontentloaded")
    with allure.step('switch lang to ru'):
        page.wait_for_timeout(3000)
        ensure_russian_ui(page)
    with allure.step('open tbank checkout'):
        page.click(TRY_PRO_BUTTON)
        page.wait_for_selector(PLANS)
        page.click(TO_BUY)
        page.wait_for_url(url_tbank)
    with allure.step('fill tbank card data'):
        page.wait_for_selector(CARD_NUMBER)
        page.click(CARD_NUMBER)
        page.fill(CARD_NUMBER, test_number_tbank)
        page.fill(CARD_DATE, test_date_tbank)
        page.fill(CARD_CODE, test_code_tbank)
        page.click(SAVE_CARD)
    with allure.step('submit tbank payment'):
        page.click(SUBMIT_TBANK)
    with allure.step("return to the sims tree"):
        page.wait_for_url(url_main_page)
        assert page.locator(TRY_PRO_BUTTON).count() == 0
    with allure.step('check pro status in database'):
        db_page = db_connect(page)
        assert is_user_pro(db_page, test_email) is True
    with allure.step('clear subscription'):
        assert clear_subscription(db_page,test_email) is True

@allure.title('Failed tbank payment')
@allure.description('')
@allure.tag('')
@allure.severity(allure.severity_level.CRITICAL)
def test_failed_tbank_payment(page):
    with allure.step('auth user'):
        page.goto(url_auth)
        page.fill(LOGIN_EMAIL, test_email)
        page.fill(LOGIN_PASSWORD, test_password)
        page.click(SUBMIT_BUTTON)
        page.wait_for_load_state("domcontentloaded")
    with allure.step('switch lang to ru'):
        page.wait_for_timeout(3000)
        ensure_russian_ui(page)
    with allure.step('open tbank checkout'):
        page.click(TRY_PRO_BUTTON)
        page.wait_for_selector(PLANS)
        page.click(TO_BUY)
        page.wait_for_url(url_tbank)
    with allure.step('fill tbank card data with incorrect card'):
        page.wait_for_selector(CARD_NUMBER)
        page.fill(CARD_NUMBER, err_number_tbank)
        page.fill(CARD_DATE, test_date_tbank)
        page.fill(CARD_CODE, test_code_tbank)
        page.click(SAVE_CARD)
    with allure.step('submit tbank payment'):
        page.click(SUBMIT_TBANK)
        page.wait_for_selector(ERR)
    with allure.step("return to the sims tree"):
        page.goto(url_main_page)
        page.wait_for_selector(TRY_PRO_BUTTON)
        assert page.locator(TRY_PRO_BUTTON).count() == 1