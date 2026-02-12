from api_methods.config import url_adminer
from selectors.adminer_page import LOGIN_PASSWORD, LOGIN_BUTTON, COMMAND_BUTTON
from db.db_pass import PASSWORD

def db_connect(page):
    page.goto(url_adminer)
    page.fill(LOGIN_PASSWORD, PASSWORD)
    page.click(LOGIN_BUTTON)
    page.click(COMMAND_BUTTON)
    return page