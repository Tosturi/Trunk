import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec


class TestLanguages:

    BUY_BUTTON = By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket'

    def test_buy_button(self, browser):
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        button = Wait(browser, timeout=10).until(ec.visibility_of_element_located(self.BUY_BUTTON))
        time.sleep(30)
        assert button is not None
