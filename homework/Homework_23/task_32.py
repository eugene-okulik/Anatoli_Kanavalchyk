from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest

# Для запуска в консоли pytest -s task_32.py


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_dynamic_loading(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    wait = WebDriverWait(driver, 10)
    start_button = wait.until(ec.element_to_be_clickable((By.XPATH, '//button[text()="Start"]')))
    start_button.click()

    hello_world_text = wait.until(ec.visibility_of_element_located((By.XPATH, '//h4[text()="Hello World!"]')))

    assert hello_world_text.text == "Hello World!", \
        f"Ожидался текст 'Hello World!', но был найден '{hello_world_text.text}'"
