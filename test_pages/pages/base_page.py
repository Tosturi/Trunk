from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def wait_present_element(self, element, timer=10):
        try:
            result = Wait(self.browser, timer).until(ec.presence_of_element_located(element),
                                                     message=f'Element {element} is not present')
        except TimeoutException as e:
            return e
        return result

    def open(self):
        self.browser.get(self.url)
