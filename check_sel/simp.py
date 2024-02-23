from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import time
import math


link = "http://suninjuly.github.io/explicit_wait2.html"


browser = webdriver.Chrome()

PRICE = By.CSS_SELECTOR, 'h5#price'
BUTTON = By.CSS_SELECTOR, 'button#book'
VALUE = By.CSS_SELECTOR, 'span#input_value'
ANSWER = By.CSS_SELECTOR, 'input#answer'
SUBMIT = By.CSS_SELECTOR, 'button#solve'


def wait_price(element: tuple, timer=12):
    """Данная функция заменяет find_element и если не находит, то ждет его появления 10 сек.
       Если элемент не будет найден за указанное время, то программа упадет как TimeoutException
    """
    return Wait(browser, timer).until(ec.text_to_be_present_in_element(element, text_='$100'),
                                      )


def wait_element(element: tuple, timer=10):
    return Wait(browser, timer).until(ec.presence_of_element_located(element),
                                      message=f'Cant find element {element}!')


try:
    browser.get(link)
    price = wait_price(PRICE)

    book = wait_element(BUTTON)
    book.click()

    x = wait_element(VALUE).text
    answer = wait_element(ANSWER)
    submit = wait_element(SUBMIT)

    answer.send_keys(str(math.log(abs(12*math.sin(int(x))))))
    submit.click()

except TimeoutException as error:
    print(error)

finally:
    time.sleep(7)
    browser.quit()
