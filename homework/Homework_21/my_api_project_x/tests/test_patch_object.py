import allure


@allure.feature('Object Management')
@allure.story('Patch Object')
@allure.title('Partially update an object')
def test_patch_object(objects_endpoint, create_test_object):
    obj_id = create_test_object
    data = {
        "id": obj_id,
        "name": "Apple MacBook Pro 20"
    }
    response = objects_endpoint.patch_object(obj_id, data)
    assert response.status_code == 200, f"Error patching object: {response.status_code} - {response.text}"
    allure.attach(f"Response: {response.json()}", name="Patch Response", attachment_type=allure.attachment_type.JSON)
