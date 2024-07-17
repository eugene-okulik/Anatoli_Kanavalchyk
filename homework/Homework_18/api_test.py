import requests


def post_a_post():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )

    assert response.status_code in [200, 201], f"Ошибка при создании объекта: {response.status_code} - {response.text}"
    response_data = response.json()
    new_object_id = response_data.get('id')
    print(f"Созданный объект имеет ID: {new_object_id}")
    return new_object_id


def put_a_post(obj_id):
    body = {
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

    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'https://api.restful-api.dev/objects/{obj_id}',
        json=body,
        headers=headers
    )

    print(response)
    print(response.json())
    assert response.status_code == 200, f"Ошибка при обновлении объекта: {response.status_code} - {response.text}"


def patch_a_post(obj_id):
    body = {
        "id": obj_id,
        "name": "Apple MacBook Pro 20"
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{obj_id}',
        json=body,
        headers=headers
    )

    print(response)
    print(response.json())
    assert response.status_code == 200, f"Ошибка при частичном обновлении объекта:" \
                                        f" {response.status_code} - {response.text}"


def delete_a_post(obj_id):
    headers = {'Content-Type': 'application/json'}
    response = requests.delete(
        f'https://api.restful-api.dev/objects/{obj_id}',
        headers=headers
    )

    print(response)
    if response.status_code == 200:
        print("Объект успешно удален")
    else:
        print(f"Ошибка при удалении объекта: {response.status_code} - {response.text}")
    assert response.status_code == 200, f"Ошибка при удалении объекта: {response.status_code} - {response.text}"


created_object_id = post_a_post()

if created_object_id:
    put_a_post(created_object_id)
    patch_a_post(created_object_id)
    delete_a_post(created_object_id)
