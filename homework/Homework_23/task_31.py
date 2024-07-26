from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest


# Для запуска в консоли pytest -s task_31.py

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_select_data_and_press_submit(driver):
    language_to_select = 'Python'
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    wait = WebDriverWait(driver, 10)
    select_element = wait.until(ec.element_to_be_clickable((By.ID, 'id_choose_language')))
    select_element.click()
    option = wait.until(ec.element_to_be_clickable((By.XPATH, f"//option[text()='{language_to_select}']")))
    option.click()

    submit_button = wait.until(ec.element_to_be_clickable((By.ID, 'submit-id-submit')))
    submit_button.click()

    result_text = wait.until(ec.visibility_of_element_located((By.ID, 'result-text')))
    assert result_text.text == language_to_select, f"Ожидался язык '{language_to_select}', " \
                                                   f"но был найден '{result_text.text}'"
