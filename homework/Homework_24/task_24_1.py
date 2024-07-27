from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
import platform


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_add_to_cart(driver):
    driver.get("https://www.demoblaze.com/index.html")
    wait = WebDriverWait(driver, 10)

    is_mac = platform.system() == 'Darwin'

    product_link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Nokia lumia 1520")))

    action = ActionChains(driver)
    if is_mac:
        action.key_down(Keys.COMMAND).click(product_link).key_up(Keys.COMMAND).perform()
    else:
        action.key_down(Keys.CONTROL).click(product_link).key_up(Keys.CONTROL).perform()

    WebDriverWait(driver, 10).until(lambda d: len(driver.window_handles) > 1)

    driver.switch_to.window(driver.window_handles[1])

    add_to_cart_button = wait.until(ec.element_to_be_clickable((By.XPATH, '//a[text()="Add to cart"]')))
    add_to_cart_button.click()

    try:
        alert = wait.until(ec.alert_is_present())
        alert.accept()
    except Exception as e:
        print(f"No alert appeared after adding to cart. Exception: {e}")

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    cart_link = driver.find_element(By.ID, "cartur")
    cart_link.click()
    cart_items = wait.until(ec.presence_of_all_elements_located((By.XPATH, '//tbody/tr/td[2]')))
    assert any(item.text == "Nokia lumia 1520" for item in cart_items), "Товар не найден в корзине"
