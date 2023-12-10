class Resource:
    def __init__(self, id, set_link, non_key_attribute):
        self.id = id
        self.set_link = set_link #Key Attribute
        self.non_key_attribute = non_key_attribute

    def __str__(self):
        return f"ID: {self.id}, Key Attribute: {self.set_link}, Non-Key Attribute: {self.non_key_attribute}"

