import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animals(animals):
     """ Prints name, diet, first location and type of animals if they exist"""

     for animal in animals:
         if "name" in animal:
             print(f"Name: {animal['name']}")

         if "diet" in animal['characteristics']:
             print(f"Diet: {animal['characteristics']['diet']}")

         if "locations" in animal:
             print(f"Location: {', '.join(animal['locations'])}")

         if "type" in animal['characteristics']:
             print(f"Type: {animal['characteristics']['type']}")

         print()




animals_data = load_data('animals_data.json')
print_animals(animals_data)