from Resource import Resource  

import json

class DataPersistenceManager:
    @staticmethod
    def load_data(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return [Resource(id=item.get('id', ''), set_Designer=item.get('set_Designer', ''), set_Name=item.get('set_Name', ''))
                        for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    @staticmethod
    def save_data(file_path, resources):
        data = [{'id': res.id, 'set_Designer': res.set_Designer, 'set_Name': res.set_Name}
                for res in resources]
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
