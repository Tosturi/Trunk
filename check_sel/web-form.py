import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import  NoSuchElementException


browser = webdriver.Chrome()
browser.get('https://www.selenium.dev/selenium/web/web-form.html')

TEXT_INPUT = By.CSS_SELECTOR, 'input#my-text-id.form-control'
PASSWORD = By.CSS_SELECTOR, 'input.form-control'
TEXTAREA = By.CSS_SELECTOR, 'textarea.form-control'


def write_text(selector, text) -> None:
    time.sleep(2)
    try:
        element = browser.find_element(*selector)
        element.send_keys(text)
    except NoSuchElementException as e:
        print(f'{e} - Н')
    time.sleep(2)


write_text(TEXT_INPUT, "some")
browser.quit()
