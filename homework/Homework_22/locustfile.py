from locust import HttpUser, task, between


class APIUser(HttpUser):
    wait_time = between(1, 2.5)
    base_url = "https://api.restful-api.dev/objects"
    object_id = None

    @task(1)
    def create_object(self):
        data = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
        response = self.client.post(self.base_url, json=data, headers={'Content-Type': 'application/json'})
        if response.status_code in [200, 201]:
            self.object_id = response.json().get('id')
            print(f"Object created: {self.object_id}")
        else:
            print(f"Failed to create object: {response.status_code} - {response.text}")

    @task(2)
    def get_objects(self):
        response = self.client.get(self.base_url)
        if response.status_code == 200:
            print(f"Objects fetched: {response.json()}")
        else:
            print(f"Failed to fetch objects: {response.status_code} - {response.text}")

    @task(1)
    def update_object(self):
        if self.object_id:
            data = {
                "name": "Apple MacBook Pro 16",
                "data": {
                    "year": 2024,
                    "price": 4000,
                    "CPU model": "Intel Core A9",
                    "Hard disk size": "2 TB",
                    "color": "silver"
                }
            }
            response = self.client.put(f"{self.base_url}/{self.object_id}", json=data,
                                       headers={'Content-Type': 'application/json'})
            if response.status_code == 200:
                print(f"Object updated: {response.json()}")
            else:
                print(f"Failed to update object: {response.status_code} - {response.text}")

    @task(1)
    def patch_object(self):
        if self.object_id:
            data = {"name": "Apple MacBook Pro 20"}
            response = self.client.patch(f"{self.base_url}/{self.object_id}", json=data,
                                         headers={'Content-Type': 'application/json'})
            if response.status_code == 200:
                print(f"Object patched: {response.json()}")
            else:
                print(f"Failed to patch object: {response.status_code} - {response.text}")

    @task(1)
    def delete_object(self):
        if self.object_id:
            response = self.client.delete(f"{self.base_url}/{self.object_id}",
                                          headers={'Content-Type': 'application/json'})
            if response.status_code == 200:
                print("Object deleted")
                self.object_id = None
            else:
                print(f"Failed to delete object: {response.status_code} - {response.text}")
