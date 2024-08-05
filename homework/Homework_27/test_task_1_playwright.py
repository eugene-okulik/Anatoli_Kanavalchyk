from playwright.sync_api import Page, expect


def test_alert_confirm(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")

    def handle_dialog(dialog):
        dialog.accept()

    page.on('dialog', handle_dialog)

    page.click('a.a-button')

    expect(page.locator('#result-text')).to_have_text('Ok')
    expect(page.locator('#result')).to_be_visible()
