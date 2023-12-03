class UserInterface:
    def display_menu(self):
        print("1. Create\n2. Read (Search)\n3. Edit\n4. Delete\n5. Exit") # Display menu options
        

    def get_user_choice(self):
        return int(input("Enter your choice: ")) # Get user input for menu choice

    def get_resource_input(self):
        id = int(input("Enter ID: ")) # Gets user input for their iD
        attribute1 = input("Enter Attribute 1: ") # Get user input for resource attributes
        attribute2 = input("Enter Attribute 2: ")
        return id, attribute1, attribute2 

    def display_resources(self, resources):
        if resources: # Display list of resources
            for resource in resources:
                print(resource)
        else:
            print("No matching resources found.")

    def get_search_criteria(self):
        resource_id = int(input("Enter resource ID: ")) # Get user input for search criteria
        return resource_id

    def display_error(self, message):
        print(f"Error: {message}") # Display error messages