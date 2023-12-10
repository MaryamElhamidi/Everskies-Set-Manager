# resource.py

class Resource:
    def __init__(self, id, set_Designer, set_Name):
        self.id = id
        self.set_Designer = set_Designer
        self.set_Name = set_Name

    def __str__(self):
        return f"Set ID: {self.id}, Designer: {self.set_Designer}, Set Name: {self.set_Name}"
