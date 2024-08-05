from playwright.sync_api import Page


def test_color_change(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')

    color_change_button = page.locator('button#colorChange')

    page.wait_for_selector('button#colorChange.text-danger')

    color_change_button.click()
