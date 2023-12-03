from Resource import Resource
import json


class ResourceManager:
    def __init__(self):
        self.resources = []


    def create_resource(self, id, attribute1, attribute2): # Creates a new resource object
        resource = Resource(id, attribute1, attribute2)
        return resource
    

    def search_resources(self, key_attribute, non_key_attribute): # Search for resources based on key and non-key attributes
        found_resources = []
        for resource in self.resources:
            if getattr(resource, key_attribute, None) == non_key_attribute:
                found_resources.append(resource)
        return found_resources

    def update_resource(self, resource_id, new_attribute1, new_attribute2):# Update the attributes of a resource

        for resource in self.resources:
            if resource.id == resource_id:
                resource.attribute1 = new_attribute1
                resource.attribute2 = new_attribute2

    def delete_resource(self, resource_id): # Delete a resource based on its ID
        self.resources = [resource for resource in self.resources if resource.id != resource_id]

# Data Persistence

class DataPersistence:
    def load_data(self, filename): # Load data from a file (JSON or CSV)
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return [Resource(**item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []        

    def save_data(self, filename, data): # Save data to a file (JSON or CSV)
        with open(filename, 'w') as file:
            serialized_data = [{'id': resource.id, 'attribute1': resource.attribute1, 'attribute2': resource.attribute2}
                               for resource in data]
            json.dump(serialized_data, file, indent=2)
