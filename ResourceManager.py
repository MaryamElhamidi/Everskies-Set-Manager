from Resource import Resource
import json


class ResourceManager:
    def __init__(self):
        self.resources = []

    def create_resource(self, resource):
        self.resources.append(resource)

    def find_resource_by_key_attribute(self, set_link):
        return [res for res in self.resources if res.set_link == set_link]

    def find_resource_by_non_key_attribute(self, set_name):
        return [res for res in self.resources if res.set_name == set_name]

    def update_resource(self, resource_id, new_non_key_attribute):
        for res in self.resources:
            if res.id == resource_id:
                res.set_name = set_name
                break

    def delete_resource(self, resource_id):
        self.resources = [res for res in self.resources if res.id != resource_id]

# Data Persistence

import json

class DataPersistenceManager:
    @staticmethod
    def load_data(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return [Resource(**item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    @staticmethod
    def save_data(file_path, resources):
        data = [{'id': res.id, 'key_attribute': res.set_link, 'non_key_attribute': res.set_name}
                for res in resources]
        with open(file_path, 'w') as file:
            json.dump(data, file)
