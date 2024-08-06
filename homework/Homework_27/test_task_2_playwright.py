from playwright.sync_api import Page, expect


def test_new_tab_interaction(page: Page):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')

    button = page.locator('#new-page-button')
    button.click()

    new_tab = page.context.wait_for_event('page')

    expect(new_tab.locator('#result-text')).to_have_text('I am a new page in a new tab')

    expect(button).to_be_enabled()

    new_tab.close()
