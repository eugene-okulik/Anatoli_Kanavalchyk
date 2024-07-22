import allure
from helpers import assert_status_code


@allure.feature('Object Management')
@allure.story('Patch Object')
@allure.title('Patch an existing object')
def test_patch_object(patch_object_endpoint, create_test_object):
    obj_id = create_test_object
    data = {
        "name": "Patched Test Object",
        "price": 299.99
    }
    response = patch_object_endpoint.patch_object(obj_id, data)
    assert_status_code(response, 200)
