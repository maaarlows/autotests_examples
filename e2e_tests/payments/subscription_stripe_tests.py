import allure
from fixtures.fixtures import ensure_english_ui
from db.db_check import wait_until_user_is_pro

from api_methods.jwt import test_email, test_password, test_number, test_name, test_code, test_date, err_number
from selectors.auth_page import LOGIN_EMAIL, LOGIN_PASSWORD, SUBMIT_BUTTON, TRY_PRO_BUTTON, TO_BUY, PLANS
from selectors.stripe_page import CARD_NUMBER, CARD_DATE, CARD_NAME, CARD_CODE, SUBMIT_STRIPE, ERR


@allure.title('Successful stripe payment')
@allure.description('')
@allure.tag('')
@allure.severity(allure.severity_level.CRITICAL)
def test_successful_stripe_payment(page):
    with allure.step('auth user'):
        page.goto("https://thesimstree.com/auth")
        page.fill(LOGIN_EMAIL, test_email)
        page.fill(LOGIN_PASSWORD, test_password)
        page.click(SUBMIT_BUTTON)
        page.wait_for_load_state("domcontentloaded")
    with allure.step('switch lang to en'):
        ensure_english_ui(page)
    with allure.step('open stripe checkout'):
        page.click(TRY_PRO_BUTTON)
        page.wait_for_selector(PLANS)
        page.click(TO_BUY)
        page.wait_for_url("https://checkout.stripe.com/c/pay/**")
    with allure.step('fill stripe card data'):
        page.wait_for_selector(CARD_NUMBER)
        page.fill(CARD_NUMBER, test_number)
        page.fill(CARD_DATE, test_date)
        page.fill(CARD_CODE, test_code)
        page.fill(CARD_NAME, test_name)
    with allure.step('submit stripe payment'):
        page.click(SUBMIT_STRIPE)
    with allure.step("return to the sims tree"):
        page.wait_for_url("https://thesimstree.com/crafted/pages/dynasty/**")
        assert page.locator(TRY_PRO_BUTTON).count() == 0
    with allure.step('check pro status in database'):
        wait_until_user_is_pro(email=test_email)


@allure.title('Failed stripe payment')
@allure.description('')
@allure.tag('')
@allure.severity(allure.severity_level.CRITICAL)
def test_failed_stripe_payment(page):
    with allure.step('auth user'):
        page.goto("https://thesimstree.com/auth")
        page.fill(LOGIN_EMAIL, test_email)
        page.fill(LOGIN_PASSWORD, test_password)
        page.click(SUBMIT_BUTTON)
        page.wait_for_load_state("domcontentloaded")
    with allure.step('switch lang to en'):
        ensure_english_ui(page)
    with allure.step('open stripe checkout'):
        page.click(TRY_PRO_BUTTON)
        page.wait_for_selector(PLANS)
        page.click(TO_BUY)
        page.wait_for_url("https://checkout.stripe.com/c/pay/**")
    with allure.step('fill stripe card data with incorrect card'):
        page.wait_for_selector(CARD_NUMBER)
        page.fill(CARD_NUMBER, err_number)
        page.fill(CARD_DATE, test_date)
        page.fill(CARD_CODE, test_code)
        page.fill(CARD_NAME, test_name)
    with allure.step('submit stripe payment'):
        page.click(SUBMIT_STRIPE)
        page.wait_for_selector(ERR)
    with allure.step("return to the sims tree"):
        page.goto("https://thesimstree.com/")
        page.wait_for_selector(TRY_PRO_BUTTON)
        assert page.locator(TRY_PRO_BUTTON).count() == 1