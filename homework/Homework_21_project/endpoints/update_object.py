from endpoints.base_endpoint import BaseEndpoint


class UpdateObjectEndpoint(BaseEndpoint):
    def update_object(self, obj_id, data):
        headers = {'Content-Type': 'application/json'}
        return self.put(f"/{obj_id}", data, headers)
