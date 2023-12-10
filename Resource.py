class Resource:# Constructor (Initializer) method for creating a new Resource object
    def __init__(self, id, set_Designer, set_Name):  # Assign values to the attributes of the Resource object
        self.id = id  # Unique identifier for the resource
        self.set_Designer = set_Designer #This is the KEY ATTRIBUTE. It is the designer information for the resource.
        self.set_Name = set_Name # This is the NON-key ATTRIBUTE. It is the set name information for the resource.

    def __str__(self):   # String representation method for the Resource object
        return f"Set ID: {self.id}, Designer: {self.set_Designer}, Set Name: {self.set_Name}"
        # Returns a formatted string representing the Resource object

