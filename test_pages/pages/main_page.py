from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    # LINK = "http://selenium1py.pythonanywhere.com/"

    def go_to_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.INCORRECT_LOGIN_LINK), "Login link is not presented"
