class Resource:
    def __init__(self, id, set_link, set_name):
        self.id = id
        self.set_link = set_link #Key Attribute
        self.set_name = set_name #Non-Key attribute

    def __str__(self):
        return f"ID: {self.id}, Set ID: {self.set_link}, Set Name: {self.set_name}"

