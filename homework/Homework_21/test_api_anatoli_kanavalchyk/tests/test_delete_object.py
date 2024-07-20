import allure


@allure.feature('Object Management')
@allure.story('Delete Object')
@allure.title('Delete an object')
def test_delete_object(objects_endpoint, create_test_object):
    obj_id = create_test_object
    response = objects_endpoint.delete_object(obj_id)
    assert response.status_code == 200, f"Error deleting object: {response.status_code} - {response.text}"
    allure.attach(f"Response: {response.text}", name="Delete Response", attachment_type=allure.attachment_type.TEXT)
