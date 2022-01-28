from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Язык браузера")



@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()