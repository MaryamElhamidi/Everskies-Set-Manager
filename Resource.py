class Resource:
    def __init__(self, id, attribute1, attribute2):
        self.id = id
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def __str__(self):
        return f"{self.id}: {self.attribute1}, {self.attribute2}"
