import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="function", autouse=True)
def set_global_timeouts(page: Page):
    page.set_default_navigation_timeout(60000)
    page.set_default_timeout(60000)

@pytest.fixture(scope="session")
def browser_args(browser_type_launch_args):
    browser_type_launch_args["slow_mo"] = 100
    browser_type_launch_args["headless"] = True
    return browser_type_launch_args