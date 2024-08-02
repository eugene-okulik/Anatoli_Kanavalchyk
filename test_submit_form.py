import pytest
from playwright.sync_api import sync_playwright, Page, expect


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        context = browser.new_context(viewport=None)
        page = context.new_page()
        page.set_viewport_size({"width": 1920, "height": 1080})
        yield page
        page.close()
        context.close()
        browser.close()


def type_with_delay(page: Page, selector: str, text: str, delay: int = 100):
    page.type(selector, text, delay=delay)
    expect(page.locator(selector)).to_have_value(text)


def test_fill_form(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")

    type_with_delay(page, '#firstName', 'John')
    type_with_delay(page, '#lastName', 'Doe')
    type_with_delay(page, '#userEmail', 'john.doe@example.com')

    page.click('label[for="gender-radio-1"]')
    expect(page.locator('#gender-radio-1')).to_be_checked()

    type_with_delay(page, '#userNumber', '1234567890')

    page.click('#dateOfBirthInput')
    page.select_option('.react-datepicker__month-select', '6')
    page.select_option('.react-datepicker__year-select', '1988')
    page.click('.react-datepicker__day--005')
    expect(page.locator('#dateOfBirthInput')).to_have_value('05 Jul 1988')

    type_with_delay(page, '#subjectsInput', 'Maths')
    page.keyboard.press('Enter')
    expect(page.locator('.subjects-auto-complete__multi-value__label')).to_have_text('Maths')

    page.click('label[for="hobbies-checkbox-2"]')
    expect(page.locator('#hobbies-checkbox-2')).to_be_checked()

    type_with_delay(page, '#currentAddress', '123 Main St, Anytown, USA')

    page.click('#state')
    page.click('div[id^=react-select-3-option-0]')
    expect(page.locator('#state .css-1uccc91-singleValue')).to_have_text('NCR')

    page.click('#city')
    page.click('div[id^=react-select-4-option-0]')
    expect(page.locator('#city .css-1uccc91-singleValue')).to_have_text('Delhi')

    page.click('#submit')

    page.wait_for_selector('#example-modal-sizes-title-lg')
    page.click('#closeLargeModal')
