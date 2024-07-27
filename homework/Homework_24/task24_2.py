import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_add_to_compare(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    wait = WebDriverWait(driver, 15)

    first_product = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".product-item")))
    ActionChains(driver).move_to_element(first_product).perform()

    add_to_compare = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".action.tocompare")))
    add_to_compare.click()

    message_locator = (By.CSS_SELECTOR, "div[data-bind*='prepareMessageForHtml']")
    wait.until(ec.text_to_be_present_in_element(message_locator, "You added product"))

    compare_products_link = wait.until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, ".item.link.compare .counter.qty")))

    quantity_text = compare_products_link.text.strip()
    assert quantity_text == "1 item", f"Ожидался '1 item', но получили '{quantity_text}'."
