import pytest
from selene.support.shared import browser, config

@pytest.fixture(autouse = True)
def browser_window():
    config.timeout = 5
    config.window_width = 1280
    config.window_height = 720
    config.base_url = 'https://google.com'
    yield
    browser.quit()
