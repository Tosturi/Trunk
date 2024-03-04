from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, f'Url {self.browser.current_url} is not correct!'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.wait_present_element(LoginPageLocators.LOGIN_FORM), 'Login Form not found!'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.wait_present_element(LoginPageLocators.REGISTRATION_FORM), 'Registration Form not found!'


