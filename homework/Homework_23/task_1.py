from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest


# Для запуска в консоли pytest -s task_1.py

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_input_data_and_press_enter(driver):
    input_data = 'Test_text-123'
    driver.get('https://www.qa-practice.com/elements/input/simple')

    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.RETURN)

    wait = WebDriverWait(driver, 5)
    result_text = wait.until(ec.visibility_of_element_located((By.ID, 'result')))

    print(result_text.text)
