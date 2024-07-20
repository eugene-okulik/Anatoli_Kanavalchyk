import requests


class BaseEndpoint:
    base_url = "https://api.restful-api.dev/objects"

    def post(self, endpoint, data, headers):
        return requests.post(f"{self.base_url}{endpoint}", json=data, headers=headers)

    def put(self, endpoint, data, headers):
        return requests.put(f"{self.base_url}{endpoint}", json=data, headers=headers)

    def patch(self, endpoint, data, headers):
        return requests.patch(f"{self.base_url}{endpoint}", json=data, headers=headers)

    def delete(self, endpoint, headers):
        return requests.delete(f"{self.base_url}{endpoint}", headers=headers)
