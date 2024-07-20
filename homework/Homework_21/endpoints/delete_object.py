from endpoints.base_endpoint import BaseEndpoint


class DeleteObjectEndpoint(BaseEndpoint):
    def delete_object(self, obj_id):
        headers = {'Content-Type': 'application/json'}
        return self.delete(f"/{obj_id}", headers)
