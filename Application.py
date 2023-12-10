from UserInterface import UserInterface
from ResourceManager import ResourceManager
from ResourceManager import DataPersistence

def main():
    ui = UserInterface()
    resource_manager = ResourceManager()
    data_persistence = DataPersistence()

    try:
        # Load existing data from a file
        resource_manager.resources = data_persistence.load_data("resources.json")
    except FileNotFoundError:
        pass

    while True:
        ui.display_menu()
        choice = ui.get_user_choice()

        if choice == 1:
            attributes = ui.get_resource_input()
            resource = resource_manager.create_resource(*attributes)
            resource_manager.resources.append(resource)
        elif choice == 2:
            set_link, non_key_attribute = ui.get_search_criteria()
            found_resources = resource_manager.search_resources(set_link, non_key_attribute)
            ui.display_resources(found_resources)
        elif choice == 3:
            resource_id = ui.get_search_criteria()[0]
            new_attributes = ui.get_resource_input()[1:]  # Exclude ID from modification
            resource_manager.update_resource(resource_id, *new_attributes)
        elif choice == 4:
            resource_id = ui.get_search_criteria()[0]
            resource_manager.delete_resource(resource_id)
        elif choice == 5:
            # Save data before exiting
            data_persistence.save_data("resources.json", resource_manager.resources)
            break
        else:
            ui.display_error("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
