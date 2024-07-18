import pytest
import requests


@pytest.fixture
def setup_object():
    headers = {'Content-Type': 'application/json'}
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers)
    assert response.status_code in [200, 201], f"Error creating object: {response.status_code} - {response.text}"
    object_id = response.json()['id']
    yield object_id  # Provide the object ID to the test
    # Teardown: Delete the created object
    requests.delete(f'https://api.restful-api.dev/objects/{object_id}', headers=headers)


def pytest_configure():
    print("Start testing")


def pytest_unconfigure():
    print("Testing completed")


# Print messages before and after each test
@pytest.fixture(autouse=True)
def print_before_and_after():
    print("before test")
    yield
    print("after test")


@pytest.mark.parametrize("name, year, price, cpu_model, hdd_size", [
    ("Dell XPS 15", 2023, 2500.0, "Intel Core i7", "512 GB"),
    ("HP Spectre x360", 2024, 2200.0, "Intel Core i5", "1 TB"),
    ("Lenovo ThinkPad X1 Carbon", 2022, 1800.0, "Intel Core i7", "256 GB")
])
def test_create_object(name, year, price, cpu_model, hdd_size):
    headers = {'Content-Type': 'application/json'}
    body = {
        "name": name,
        "data": {
            "year": year,
            "price": price,
            "CPU model": cpu_model,
            "Hard disk size": hdd_size
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers)
    assert response.status_code in [200, 201], f"Error creating object: {response.status_code} - {response.text}"
    print(f"Created object ID: {response.json()['id']}")


@pytest.mark.medium
def test_update_object(setup_object):
    headers = {'Content-Type': 'application/json'}
    body = {
        "id": setup_object,
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2024,
            "price": 4000,
            "CPU model": "Intel Core A9",
            "Hard disk size": "2 TB",
            "color": "silver"
        }
    }
    response = requests.put(f'https://api.restful-api.dev/objects/{setup_object}', json=body, headers=headers)
    assert response.status_code == 200, f"Error updating object: {response.status_code} - {response.text}"
    print("Object updated successfully")


@pytest.mark.critical
def test_patch_object(setup_object):
    headers = {'Content-Type': 'application/json'}
    body = {
        "id": setup_object,
        "name": "Apple MacBook Pro 20"
    }
    response = requests.patch(f'https://api.restful-api.dev/objects/{setup_object}', json=body, headers=headers)
    assert response.status_code == 200, f"Error partially updating object: {response.status_code} - {response.text}"
    print("Object partially updated successfully")


def test_delete_object(setup_object):
    headers = {'Content-Type': 'application/json'}
    response = requests.delete(f'https://api.restful-api.dev/objects/{setup_object}', headers=headers)
    assert response.status_code == 200, f"Error deleting object: {response.status_code} - {response.text}"
    print("Object deleted successfully")
