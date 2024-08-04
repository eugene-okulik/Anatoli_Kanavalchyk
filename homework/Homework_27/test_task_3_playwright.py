from playwright.sync_api import sync_playwright


def test_color_change(browser_name):
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

        page.goto('https://demoqa.com/dynamic-properties')

        color_change_button = page.locator('button#colorChange')

        page.wait_for_selector('button#colorChange.text-danger')

        color_change_button.click()

        browser.close()


for browser_type in ['chromium', 'firefox', 'webkit']:
    test_color_change(browser_type)
