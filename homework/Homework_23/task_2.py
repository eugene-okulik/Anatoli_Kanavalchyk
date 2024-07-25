from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# Для запуска в консоли pytest -s task_2.py

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def scroll_to_element(driver, by, value):
    try:
        element = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((by, value))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
    except Exception as e:
        print(f"Ошибка при прокрутке к элементу: {e}")


def click_element_with_fallback(driver, by, value):
    try:
        element = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((by, value))
        )
        element.click()
    except Exception as e:
        # Используем JavaScript для клика
        print(f"Клик через JavaScript из-за ошибки: {e}")
        element = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((by, value))
        )
        driver.execute_script("arguments[0].click();", element)


def test_input_data_press_enter_and_print(driver):
    first_name = 'Bobby'
    last_name = 'Sands'
    user_email = 'bobby_sands@example.com'
    user_number = '1234567890'
    current_address = 'NY 3rd Avenue'

    driver.get('https://demoqa.com/automation-practice-form')

    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, 'firstName'))
    ).send_keys(first_name)

    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, 'lastName'))
    ).send_keys(last_name)

    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, 'userEmail'))
    ).send_keys(user_email)

    scroll_to_element(driver, By.XPATH, "//label[contains(text(), 'Male')]")
    click_element_with_fallback(driver, By.XPATH, "//label[contains(text(), 'Male')]")

    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, 'userNumber'))
    ).send_keys(user_number)

    scroll_to_element(driver, By.ID, 'dateOfBirthInput')
    date_input = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.ID, 'dateOfBirthInput'))
    )
    date_input.click()

    scroll_to_element(driver, By.CLASS_NAME, 'react-datepicker__month-select')
    month_dropdown = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CLASS_NAME, 'react-datepicker__month-select'))
    )
    month_dropdown.click()
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "//option[text()='March']"))
    ).click()

    scroll_to_element(driver, By.CLASS_NAME, 'react-datepicker__year-select')
    year_dropdown = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CLASS_NAME, 'react-datepicker__year-select'))
    )
    year_dropdown.click()
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "//option[text()='1988']"))
    ).click()

    scroll_to_element(driver, By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='21']")
    day_to_select = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='21']"))
    )
    day_to_select.click()

    scroll_to_element(driver, By.XPATH, "//label[contains(text(), 'Sports')]")
    click_element_with_fallback(driver, By.XPATH, "//label[contains(text(), 'Sports')]")

    scroll_to_element(driver, By.ID, 'currentAddress')
    current_address_textarea = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, 'currentAddress'))
    )
    current_address_textarea.send_keys(current_address)

    scroll_to_element(driver, By.CSS_SELECTOR, "#state > div")
    state_dropdown = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "#state > div"))
    )
    state_dropdown.click()
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "//div[text()='NCR']"))
    ).click()

    scroll_to_element(driver, By.CSS_SELECTOR, "#city > div")
    city_dropdown = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "#city > div"))
    )
    city_dropdown.click()
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "//div[text()='Delhi']"))
    ).click()

    scroll_to_element(driver, By.ID, 'subjectsInput')
    subjects_input = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, 'subjectsInput'))
    )
    subjects_input.click()
    subjects_input.send_keys("Arts")
    subjects_input.send_keys(Keys.RETURN)

    scroll_to_element(driver, By.ID, 'submit')
    click_element_with_fallback(driver, By.ID, 'submit')

    result_modal = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, '.modal-content'))
    )
    print("Modal Content:\n", result_modal.text)
