import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    slowmo = 500
    headless = False
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, slow_mo=slowmo)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(60000)
        page.set_default_navigation_timeout(60000)
        yield page
        context.close()
        browser.close()