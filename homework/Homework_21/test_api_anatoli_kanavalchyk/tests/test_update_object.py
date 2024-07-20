import allure


@allure.feature('Object Management')
@allure.story('Update Object')
@allure.title('Update an object')
def test_update_object(objects_endpoint, create_test_object):
    obj_id = create_test_object
    data = {
        "id": obj_id,
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2024,
            "price": 4000,
            "CPU model": "Intel Core A9",
            "Hard disk size": "2 TB",
            "color": "silver"
        }
    }
    response = objects_endpoint.update_object(obj_id, data)
    assert response.status_code == 200, f"Error updating object: {response.status_code} - {response.text}"
    allure.attach(f"Response: {response.json()}", name="Update Response", attachment_type=allure.attachment_type.JSON)
