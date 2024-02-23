from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec

BASE_URL = 'https://www.selenium.dev'


class BasePage:
    def __init__(self, browser, base_url=BASE_URL):
        self.browser = browser
        self.base_url = base_url

    def wait_element(self, element, time=10):
        return Wait(self.browser, time).until(ec.presence_of_element_located(element),
                                              message=f"Cant find {element}")

    def wait_elements(self, elements, time=10):
        return Wait(self.browser, time).until(ec.presence_of_all_elements_located(elements),
                                              message=f"Cant find elements {elements}")

    def visible_element(self, element: tuple, timer=10):
        return Wait(self.browser, timer).until(ec.visibility_of_element_located(element),
                                               message=f'{element} is not visible!')
