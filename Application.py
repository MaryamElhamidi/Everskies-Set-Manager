from Resource import Resource  

import json # Importing the JSON module for working with JSON data

class DataPersistenceManager:
    @staticmethod
    def load_data(file_path): #Loads data from a JSON file
        try:# Try to open the specified file for reading
            with open(file_path, 'r') as file:   # Load JSON data from the file and create Resource objects          

                data = json.load(file)
                return [Resource(id=item.get('id', ''), set_Designer=item.get('set_Designer', ''), set_Name=item.get('set_Name', ''))
                        for item in data]
        except (json.JSONDecodeError, FileNotFoundError): # Handle exceptions (file not found or JSON decoding error) by returning an empty list
            return []

    @staticmethod
    def save_data(file_path, resources):  # Saves data to a JSON file
        data = [{'id': res.id, 'set_Designer': res.set_Designer, 'set_Name': res.set_Name} # Converts Resource class obtained from the User Interaction objects to a JSON-compatible format
                for res in resources]
        with open(file_path, 'w') as file: # Opens the specified file for writing and save the JSON data
            json.dump(data, file, indent=2) # Saves the data to the file in JSON format with an indentation of 2 spaces

