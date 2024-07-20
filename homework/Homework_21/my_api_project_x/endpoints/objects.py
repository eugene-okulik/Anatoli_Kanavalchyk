from endpoints.base_endpoint import BaseEndpoint


class ObjectsEndpoint(BaseEndpoint):
    def create_object(self, data):
        headers = {'Content-Type': 'application/json'}
        return self.post('', data, headers)

    def update_object(self, obj_id, data):
        headers = {'Content-Type': 'application/json'}
        return self.put(f"/{obj_id}", data, headers)

    def patch_object(self, obj_id, data):
        headers = {'Content-Type': 'application/json'}
        return self.patch(f"/{obj_id}", data, headers)

    def delete_object(self, obj_id):
        headers = {'Content-Type': 'application/json'}
        return self.delete(f"/{obj_id}", headers)
