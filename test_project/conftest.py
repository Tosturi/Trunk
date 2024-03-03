from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FFOptions
import pytest


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='en-gb',
                     help='Choose correct language, for example - en-gb')


@pytest.fixture(scope='class')
def browser(request):
    """Создание браузера согласно заданным параметрам"""
    browser_name = request.config.getoption('browser_name')
    user_languages = request.config.getoption('language')
    match browser_name:
        case 'chrome':
            print('\nstart chrome browser for test...')
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': user_languages})
            browser = webdriver.Chrome(options=options)
        case 'firefox':
            print('\nstart firefox browser for test...')
            options = FFOptions()
            options.set_preference('intl.accept_languages', user_languages)
            browser = webdriver.Firefox(options=options)
        case _:
            raise pytest.UsageError('--browser_name should be chrome or firefox')
    browser.implicitly_wait(12)
    print('\n Start! \n')
    yield browser
    print('\n End! \n')
    browser.quit()
