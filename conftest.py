import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default=None,
                     help='Choose language: ru, en, ...')

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': 'language'})

@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome(options=options)
    user_language = request.config.getoption('language')

    yield browser
    print("\nquit browser..")
    browser.quit()