from Resource import Resource
class ResourceManager:
    def __init__(self):  # Constructor (Initializer) method for creating a new ResourceManager object
        self.resources = [] #Initializes an empty list to store resources

    def create_resource(self, resource): # Method for creating a new resource and adding it to the collection
        self.resources.append(resource)  # Append the given resource to the list of resources

    def find_resource_by_key_attribute(self, set_Designer): # Method for finding resources based on the key attribute (set_Designer)
        return [res for res in self.resources if res.set_Designer == set_Designer] # Returns a list of resources with the specified set_Designer

    def find_resource_by_non_key_attribute(self, set_Name): # Method for finding resources based on the non-key attribute (set_Name)
        return [res for res in self.resources if res.set_Name == set_Name] # Returns a list of resources with the specified set_Name

    def update_resource(self, resource_id, new_set_Name):  # Method for updating the information of an existing resource
        for res in self.resources: # Iterates through resources and updates the set_Name/non-key variable of the matching resource
            if res.id == resource_id:
                res.set_Name = new_set_Name
                break

    def delete_resource(self, resource_id): # Method for deleting a resource based on its unique identifier (ID)
        self.resources = [res for res in self.resources if str(res.id) != str(resource_id)] #Filters out the resource with the specified ID from the list of resources