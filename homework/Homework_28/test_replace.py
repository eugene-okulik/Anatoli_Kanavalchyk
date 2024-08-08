import re
import json
from playwright.sync_api import Page, Route, Request


def intercept_and_modify_response(route: Route, request: Request):
    response = route.fetch()
    content_type = response.headers.get("content-type", "")

    if "application/json" in content_type or "json" in request.url:
        json_data = response.json()
        modified = False

        def modify_title(data):
            nonlocal modified
            if isinstance(data, list):
                for item in data:
                    modify_title(item)
            elif isinstance(data, dict):
                for key, value in data.items():
                    if isinstance(value, str):
                        # Заменяем только "iPhone 15 Pro", но не содержащие "Max"
                        if re.search(r'iPhone\s*15\s*Pro', value) and not re.search(r'Max', value):
                            new_value = re.sub(r'iPhone\s*15\s*Pro', 'яблокофон 15 про', value)
                            if new_value != value:
                                data[key] = new_value
                                modified = True
                    else:
                        modify_title(value)

        modify_title(json_data)

        if modified:
            print(json.dumps(json_data, indent=2, ensure_ascii=False))
            route.fulfill(
                status=response.status,
                headers=response.headers,
                body=json.dumps(json_data)
            )
        else:
            route.continue_()
    else:
        route.continue_()


def test_replace(page: Page):
    context = page.context

    context.route("**/*", intercept_and_modify_response)

    page.goto("https://www.apple.com/shop/buy-iphone")

    page.click("button:has-text('iPhone 15 Pro')")

    elements = page.query_selector_all("text='яблокофон 15 про'")

    assert elements, "No elements found with the text 'яблокофон 15 про'"

    for element in elements:
        popup_title_text = element.text_content()
        assert popup_title_text == "яблокофон 15 про", f"Expected title 'яблокофон 15 про', " \
                                                       f"but got '{popup_title_text}'"

    # Дополнительное ожидание для наглядности
    page.wait_for_timeout(10000)
