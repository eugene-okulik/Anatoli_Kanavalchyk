from playwright.sync_api import sync_playwright, expect


def test_alert_confirm(browser_name):
    with sync_playwright() as p:
        if browser_name == 'chromium':
            browser = p.chromium.launch()
        elif browser_name == 'firefox':
            browser = p.firefox.launch()
        elif browser_name == 'webkit':
            browser = p.webkit.launch()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.qa-practice.com/elements/alert/confirm")

        def handle_dialog(dialog):
            dialog.accept()

        page.on('dialog', handle_dialog)

        page.click('a.a-button')

        expect(page.locator('#result-text')).to_have_text('Ok')
        expect(page.locator('#result')).to_be_visible()

        page.close()
        context.close()
        browser.close()


for browser_type in ['chromium', 'firefox', 'webkit']:
    test_alert_confirm(browser_type)
