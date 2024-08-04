from playwright.sync_api import sync_playwright, expect


def test_new_tab_interaction(browser_name):
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

        page.goto('https://www.qa-practice.com/elements/new_tab/button')

        button = page.locator('#new-page-button')
        button.click()

        new_tab = context.wait_for_event('page')

        expect(new_tab.locator('#result-text')).to_have_text('I am a new page in a new tab')

        expect(button).to_be_enabled()

        new_tab.close()
        page.close()
        context.close()
        browser.close()


for browser_type in ['chromium', 'firefox', 'webkit']:
    test_new_tab_interaction(browser_type)
