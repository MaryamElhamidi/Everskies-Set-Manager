from Resource import Resource
class ResourceManager:
    def __init__(self):
        self.resources = []

    def create_resource(self, resource):
        self.resources.append(resource)

    def find_resource_by_key_attribute(self, set_Designer):
        return [res for res in self.resources if res.set_Designer == set_Designer]

    def find_resource_by_non_key_attribute(self, set_Name):
        return [res for res in self.resources if res.set_Name == set_Name]

    def update_resource(self, resource_id, new_set_Name):
        for res in self.resources:
            if res.id == resource_id:
                res.set_Name = new_set_Name
                break

    def delete_resource(self, resource_id):
        self.resources = [res for res in self.resources if res.id != resource_id]
