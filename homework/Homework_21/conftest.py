import pytest
from endpoints.create_object import CreateObjectEndpoint
from endpoints.update_object import UpdateObjectEndpoint
from endpoints.patch_object import PatchObjectEndpoint
from endpoints.delete_object import DeleteObjectEndpoint


@pytest.fixture
def create_object_endpoint():
    return CreateObjectEndpoint()


@pytest.fixture
def update_object_endpoint():
    return UpdateObjectEndpoint()


@pytest.fixture
def patch_object_endpoint():
    return PatchObjectEndpoint()


@pytest.fixture
def delete_object_endpoint():
    return DeleteObjectEndpoint()


@pytest.fixture
def create_test_object(create_object_endpoint, delete_object_endpoint):
    data = {
        "name": "Test Object",
        "data": {
            "year": 2020,
            "price": 99.99,
            "CPU model": "Intel Core i5",
            "Hard disk size": "500 GB"
        }
    }
    response = create_object_endpoint.create_object(data)
    object_id = response.json().get('id')
    yield object_id
    delete_object_endpoint.delete_object(object_id)
