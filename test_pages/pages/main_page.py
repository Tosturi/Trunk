from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):

    # LINK = "http://selenium1py.pythonanywhere.com/"
    LOGIN_BUTTON = By.CSS_SELECTOR, "#login_link"

    def go_to_page(self):
        login_link = self.wait_present_element(self.LOGIN_BUTTON)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
