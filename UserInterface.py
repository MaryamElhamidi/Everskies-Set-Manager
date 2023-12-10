from Resource import Resource
from ResourceManager import ResourceManager
from ResourceManager import DataPersistenceManager

class UI:
    def __init__(self):
        self.resource_manager = ResourceManager()
        self.data_persistence_manager = DataPersistenceManager()

    def menu(self):
        print("1. Create")
        print("2. Read (Search)")
        print("3. Edit")
        print("4. Delete")
        print("0. Exit")

    def run(self):
        file_path = 'data.json'
        self.resource_manager.resources = self.data_persistence_manager.load_data(file_path)

        while True:
            try:
                self.menu()
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    self.create_resource()
                elif choice == 2:
                    self.search_resource()
                elif choice == 3:
                    self.edit_resource()
                elif choice == 4:
                    self.delete_resource()
                elif choice == 0:
                    self.data_persistence_manager.save_data(file_path, self.resource_manager.resources)
                    break
                else:
                    print("Invalid choice. Please try again.")

            except Exception as e:
                print(f"An error occurred: {e}")

    def create_resource(self):
        id = len(self.resource_manager.resources) + 1
        set_link = input("Enter Key Attribute: ")
        non_key_attribute = input("Enter Non-Key Attribute: ")

        resource = Resource(id, set_link, non_key_attribute)
        self.resource_manager.create_resource(resource)
        print("Resource created successfully.")

    def search_resource(self):
        set_link = input("Enter Key Attribute to search: ")
        non_key_attribute = input("Enter Non-Key Attribute to search: ")

        found_resources = []
        if set_link:
            found_resources.extend(self.resource_manager.find_resource_by_key_attribute(set_link))
        if non_key_attribute:
            found_resources.extend(self.resource_manager.find_resource_by_non_key_attribute(non_key_attribute))

        if found_resources:
            for res in found_resources:
                print(res)
        else:
            print("No matching resources found.")

    def edit_resource(self):
        resource_id = int(input("Enter the ID of the resource to edit: "))
        new_non_key_attribute = input("Enter the new Non-Key Attribute: ")

        self.resource_manager.update_resource(resource_id, new_non_key_attribute)
        print("Resource updated successfully.")

    def delete_resource(self):
        resource_id = int(input("Enter the ID of the resource to delete: "))
        self.resource_manager.delete_resource(resource_id)
        print("Resource deleted successfully.")

if __name__ == "__main__":
    ui = UI()
    ui.run()
