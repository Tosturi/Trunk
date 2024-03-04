from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = By.CSS_SELECTOR, "#login_link"
    INCORRECT_LOGIN_LINK = By.CSS_SELECTOR, "#login_link_invalid"


class LoginPageLocators:
    LOGIN_FORM = By.CSS_SELECTOR, 'form#login_form.well'
    REGISTRATION_FORM = By.CSS_SELECTOR, 'form#register_form.well'
