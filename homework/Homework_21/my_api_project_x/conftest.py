import pytest
from endpoints.objects import ObjectsEndpoint


@pytest.fixture
def objects_endpoint():
    return ObjectsEndpoint()


@pytest.fixture
def create_test_object(objects_endpoint):
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
    assert response.status_code in [200, 201], f"Failed to create test object: {response.status_code} - {response.text}"
    return response.json()['id']
