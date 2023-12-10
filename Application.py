from Resource import Resource  

import json

# Data Persistence

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
        data = [{'id': res.id, 'key_attribute': res.key_attribute, 'non_key_attribute': res.non_key_attribute}
                for res in resources]
        with open(file_path, 'w') as file:
            json.dump(data, file)
