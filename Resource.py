class Resource:
    def __init__(self, id, set_link, set_name):
        self.id = id
        self.set_link = set_link #Key Attribute
        self.set_name = set_name #Non-Key attribute

    def __str__(self):
        return f"ID: {self.id}, Key Attribute: {self.set_link}, Non-Key Attribute: {self.set_name}"

