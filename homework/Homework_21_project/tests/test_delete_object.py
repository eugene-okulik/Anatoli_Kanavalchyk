import allure
from helpers import assert_status_code


@allure.feature('Object Management')
@allure.story('Delete Object')
@allure.title('Delete an object')
def test_delete_object(delete_object_endpoint, create_test_object):
    obj_id = create_test_object
    response = delete_object_endpoint.delete_object(obj_id)
    assert_status_code(response, 200)
