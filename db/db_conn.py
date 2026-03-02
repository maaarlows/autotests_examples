from api_methods.config import url_adminer
from ui_selectors.adminer_page import LOGIN_PASSWORD, LOGIN_BUTTON, COMMAND_BUTTON
from db.db_pass import PASSWORD

def db_connect(page):
    page.goto(url_adminer, wait_until="load")
    page.fill(LOGIN_PASSWORD, PASSWORD)
    page.click(LOGIN_BUTTON)
    page.click(COMMAND_BUTTON)
    return page