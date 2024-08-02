import pytest
from playwright.sync_api import sync_playwright, Page, expect


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:

        browser = p.chromium.launch(channel="chrome", headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


def test_form_authentication(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    # sleep(3)
    page.get_by_role('link', name='Form Authentication').click()
    # sleep(3)
    page.get_by_role('textbox', name='username').fill('tomsmith')
    # sleep(3)
    page.get_by_role('textbox', name='password').fill('SuperSecretPassword!')
    # sleep(3)
    page.get_by_role('button', name='Login').click()
    # sleep(3)
    expect(page.locator('div.flash.success')).to_be_visible()
    # sleep(3)
