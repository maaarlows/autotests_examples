import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="function", autouse=True)
def set_global_timeouts(page: Page):
    page.set_default_navigation_timeout(60000)
    page.set_default_timeout(60000)