# Imports the ResourceManager, DataPersistenceManager, and Resource classes from their respective modules
from Resource import Resource
from ResourceManager import ResourceManager
from Application import DataPersistenceManager

class UI:
    def __init__(self): # Constructor (Initializer) method for creating a new UI object
        self.resource_manager = ResourceManager() # Initializes an instance of ResourceManager
        self.data_persistence_manager = DataPersistenceManager()   # Initializes an instance of DataPersistenceManager

    def menu(self): # Method to display the menu options
        print('┌── ⋆⋅☆⋅⋆ ──┐')
        print('✰ Welcome to Everskies Set Creation Centre ✰')
        print('Everskies.com is a dress up site with a major focus on creativity. \nThrough this program you will have the opportunity to create a set, and acess it which users will have access to.\nPlease follow the menu instructions.')
        print('Before you continue, please note that Everskies has case sensitive set rules.')
        print('└── ⋆⋅☆⋅⋆ ──┘')

        print("1. Create")
        print("2. Read (Search)")
        print("3. Edit")
        print("4. Delete")
        print("0. Exit")

    def run(self):
        file_path = 'data.json' # Specifies the file path for data persistence
        self.resource_manager.resources = self.data_persistence_manager.load_data(file_path) #Loads existing data from the file into the resource manager

        while True:
            try:
                self.menu() # Display the menu and get the user's choice
                choice = int(input("Enter your choice ₍ ᐢ.ˬ.ᐢ₎: ")) #Prompt User
                # Execute the corresponding action based on the user's choice
                if choice == 1: # User chooses to create a resource
                    self.create_resource()
                elif choice == 2: # User chooses to search for resources
                    self.search_resource()
                elif choice == 3: # User chooses to edit an existing resource
                    self.edit_resource()
                elif choice == 4: # User chooses to delete an existing resource
                    self.delete_resource()
                elif choice == 0: # User chooses to exit, save the data, and break out of the loop
                    self.data_persistence_manager.save_data(file_path, self.resource_manager.resources)
                    break
                else: # Displays an error message for an invalid choice
                    print("Invalid choice. Please try again.") 

            except Exception as e: # Handle exceptions and display an error message
                print(f"An error occurred: {e}")

    def create_resource(self):  #Method for creating a new resource
        id = input("Enter the set ID: ") #Prompts the user to enter the set ID
        set_Designer = input("Enter Designer Name: ") #Prompts the user to enter the  designer name
        set_Name = input("Enter Set Name: ") #Prompts the user to enter the set name

        resource = Resource(id, set_Designer, set_Name) # Create a new Resource object with the provided ID, set_Designer, and set_Name
        self.resource_manager.create_resource(resource) # Add the new resource to the resource manager
        print("Resource created successfully.")

    def search_resource(self):     # Method for searching for resources based on key and non-key attributes
        set_Designer = input("Enter Key Attribute to search (The Designer Name): ")
        set_Name = input("Enter Non-Key Attribute to search (The Set Name): ") 

        found_resources = [] # Initialize an empty list to store resources found based on user search criteria
        # Search for resources based on key and non-key attributes
        if set_Designer: # Check if a key attribute (set_Designer) is provided for searching
            found_resources.extend(self.resource_manager.find_resource_by_key_attribute(set_Designer)) # Extend the list of found_resources with resources matching the set_Designer
        if set_Name: # Check if a non-key attribute (set_Name) is provided for searching
            found_resources.extend(self.resource_manager.find_resource_by_non_key_attribute(set_Name))  # Extend the list of found_resources with resources matching the set_Name
        
        
        # Displays the found resources or a message if none are found
        if found_resources:
            for res in found_resources:
                print(res)
        else:
            print("No matching resources found. Please check your capitlization and spelling or create a new set.")

    def edit_resource(self): # Method for editing an existing resource
        resource_id = input("Enter the ID of the resource to edit: ")  # Prompt the user to enter the ID of the resource to edit
        new_set_Name = input("Enter the new Name: ") # Prompt the user to enter the new value for the Set Name

        resource_id = str(resource_id)  # Convert the resource_id to a string

        found = False  # Initialize a variable to track if the resource is found
        for res in self.resource_manager.resources: # Iterate through the resources to find the one with the specified ID
            if res.id == resource_id:  # Check if the current resource has the specified ID
                res.set_Name = new_set_Name  # Update the Set Name of the found resource with the new value
                found = True # Set found to True to indicate that the resource has been found and updated
                print("Resource updated successfully.") # Display a success message indicating that the resource has been updated
                break # Exit the loop once the resource is found and updated

        if not found: # Check if the resource was not found
            print("Resource not found.") # Display a message indicating that the resource was not found
            
    def delete_resource(self):     # Method for deleting an existing resource
        resource_id = input("Enter the ID of the resource to delete: ") # Prompt the user to enter the ID of the resource to delete
        self.resource_manager.delete_resource(str(resource_id)) # Call the delete_resource method of the resource_manager to delete the resource by ID
        print("Resource deleted successfully.") # Display a success message indicating that the resource has been deleted

if __name__ == "__main__": # Check if the script is being run as the main program (not imported as a module)
    ui = UI() # Creates an instance of the UI class and runs the UI
    ui.run()
