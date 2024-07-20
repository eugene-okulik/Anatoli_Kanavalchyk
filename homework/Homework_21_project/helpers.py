def get_object_id_from_response(response):
    return response.json().get('id')


def assert_status_code(response, expected_status_code):
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, " \
                                                         f"but got {response.status_code}: {response.text}"
