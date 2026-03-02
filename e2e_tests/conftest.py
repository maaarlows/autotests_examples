import pytest

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(100000)
    page.set_default_navigation_timeout(100000)
    yield page
    context.close()
