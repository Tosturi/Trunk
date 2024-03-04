from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def wait_present_element(self, element, timer=10):
        try:
            Wait(self.browser, timer).until(ec.presence_of_element_located(element),
                                            message=f'Element {element} is not present')
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, selector):
        try:
            self.browser.find_element(how, selector)
        except NoSuchElementException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)
