import allure


@allure.feature('Object Management')
@allure.story('Create Object')
@allure.title('Create a new object')
def test_create_object(objects_endpoint):
    data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = objects_endpoint.create_object(data)
    assert response.status_code in [200, 201], f"Error creating object: {response.status_code} - {response.text}"
    object_id = response.json().get('id')
    assert object_id, "No ID returned for created object"
    allure.attach(str(object_id), name='Created Object ID', attachment_type=allure.attachment_type.TEXT)
