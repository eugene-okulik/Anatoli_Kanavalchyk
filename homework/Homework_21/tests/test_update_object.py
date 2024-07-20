import allure
from helpers import assert_status_code


@allure.feature('Object Management')
@allure.story('Update Object')
@allure.title('Update an existing object')
def test_update_object(update_object_endpoint, create_test_object):
    obj_id = create_test_object
    data = {
        "name": "Updated Test Object",
        "data": {
            "year": 2021,
            "price": 199.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "1 TB"
        }
    }
    response = update_object_endpoint.update_object(obj_id, data)
    assert_status_code(response, 200)
