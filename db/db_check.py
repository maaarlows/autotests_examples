import time
from datetime import date
from ui_selectors.adminer_page import TEXT_FIELD, EXECUTE_BUTTON, TABLE

def is_user_pro(page, email:str) -> bool:
    query = f"""
    SELECT subscribe_till
    FROM users
    WHERE email = '{email}'
    """
    page.click(TEXT_FIELD)
    page.fill(TEXT_FIELD, query)
    page.click(EXECUTE_BUTTON)
    page.wait_for_selector(TABLE)
    cell = page.locator("table tr td").first
    if cell.count() == 0:
        return False
    subscribe_till = cell.inner_text().strip()
    if not subscribe_till:
        return False

    today = date.today()
    expected = date(today.year + 1, today.month, today.day).isoformat()
    return subscribe_till[:10] == expected

def clear_subscription(page, email:str) -> bool:
    query_update = f"""
        UPDATE users
        SET subscribe_till = NULL
        WHERE email = '{email}'
        """
    page.click(TEXT_FIELD)
    page.fill(TEXT_FIELD, query_update)
    page.click(EXECUTE_BUTTON)
    page.click(TEXT_FIELD)
    page.fill(TEXT_FIELD, "")
    query_check = f"""
        SELECT subscribe_till
        FROM users
        WHERE email = '{email}'
        """
    page.click(TEXT_FIELD)
    page.fill(TEXT_FIELD, query_check)
    page.click(EXECUTE_BUTTON)
    page.wait_for_selector(TABLE)
    cell = page.locator("table tr td").first
    value = cell.inner_text().strip().lower()
    return value.lower() == "null"


def wait_until_user_is_pro(email, timeout=60, step=2):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if is_user_pro(email):
            return
        time.sleep(step)
    raise AssertionError(f"User {email} was not upgraded to PRO within {timeout} seconds")

def check_new_sim(first_name, last_name):
    return True
