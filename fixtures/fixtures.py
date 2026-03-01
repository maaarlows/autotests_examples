import pytest
import random
import string

from selectors.auth_page import LANG_BUTTON, ENG_LOCATOR, RU_LOCATOR


@pytest.fixture
def name_generator():
    length = 8
    first_name = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    last_name = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return first_name, last_name

def is_english_ui(page) -> bool:
    text = page.locator(f"{LANG_BUTTON} span.text-muted").inner_text().strip()
    return text.upper() == "EN"

def ensure_english_ui(page):
    if is_english_ui(page):
        return
    page.click(LANG_BUTTON)
    page.click(ENG_LOCATOR)
    if is_english_ui(page):
        return

def is_russian_ui(page) -> bool:
    text = page.locator(f"{LANG_BUTTON} span.text-muted").inner_text().strip()
    return text.upper() == "RU"

def ensure_russian_ui(page):
    if is_russian_ui(page):
        return
    page.click(LANG_BUTTON)
    page.click(RU_LOCATOR)
    if is_russian_ui(page):
        return