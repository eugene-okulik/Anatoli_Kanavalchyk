from endpoints.base_endpoint import BaseEndpoint


class CreateObjectEndpoint(BaseEndpoint):
    def create_object(self, data):
        headers = {'Content-Type': 'application/json'}
        return self.post('', data, headers)
