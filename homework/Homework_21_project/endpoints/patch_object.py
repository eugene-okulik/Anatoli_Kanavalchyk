from endpoints.base_endpoint import BaseEndpoint


class PatchObjectEndpoint(BaseEndpoint):
    def patch_object(self, obj_id, data):
        headers = {'Content-Type': 'application/json'}
        return self.patch(f"/{obj_id}", data, headers)
