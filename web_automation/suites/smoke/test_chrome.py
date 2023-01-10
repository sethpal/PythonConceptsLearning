from web_automation.core_libs.browsers.Chrome import Chrome
import pytest

@pytest.fixture()
def test_browser(self):
        browser = Chrome()
        print(browser.getBrowserDriver())