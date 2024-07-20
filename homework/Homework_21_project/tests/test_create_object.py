import allure
from helpers import assert_status_code, get_object_id_from_response


@allure.feature('Object Management')
@allure.story('Create Object')
@allure.title('Create a new object')
def test_create_object(create_object_endpoint):
    data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = create_object_endpoint.create_object(data)

    assert_status_code(response, 200)
    object_id = get_object_id_from_response(response)
    assert object_id is not None, "Object ID should not be None"
