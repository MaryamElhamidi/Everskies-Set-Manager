from Resource import Resource  #Importing the Resource class to obtain information about the objects in order to successfully persist all data into an appropriate text file.

import json # Importing the JSON module for working with JSON data

class DataPersistenceManager:
    """
    This static method is associated with the class itself (not an instance of the class) and is used
    to read data from a specified JSON file. It takes a file path as a parameter and returns a list of
    Resource objects created from the loaded JSON data. If the file is not found or there is a JSON 
    decoding error, an empty list is returned.
    """
    @staticmethod
    def load_data(file_path): #Loads data from a JSON file
        try:# Try to open the specified file for reading
            with open(file_path, 'r') as file:   # Load JSON data from the file and create Resource objects          

                data = json.load(file)
                return [Resource(id=item.get('id', ''), set_Designer=item.get('set_Designer', ''), set_Name=item.get('set_Name', ''))
                        for item in data]
        except (json.JSONDecodeError, FileNotFoundError): # Handle exceptions (file not found or JSON decoding error) by returning an empty list
            return []
    """
    This static method is associated with the class itself (not an instance of the class) and is used
    to write data to a specified JSON file. It takes a file path and a list of Resource objects as
    parameters, converts the data into JSON format, and writes it to the file. The 'indent=2' argument 
    adds indentation for better readability in the saved JSON file.
    """
    @staticmethod
    def save_data(file_path, resources):  # Saves data to a JSON file
        data = [{'id': res.id, 'set_Designer': res.set_Designer, 'set_Name': res.set_Name} # Converts Resource class obtained from the User Interaction objects to a JSON-compatible format
                for res in resources]
        with open(file_path, 'w') as file: # Opens the specified file for writing and save the JSON data
            json.dump(data, file, indent=2) # Saves the data to the file in JSON format with an indentation of 2 spaces