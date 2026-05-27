import json


def load_data(file_path):
    """Load a JSON file."""

    with open(file_path, "r") as handle:
        return json.load(handle)


def generate_animals_html(data):
    """Generate HTML for all animals."""

    output = ""

    for animal_data in data:

        if "name" in animal_data:
            output += f"Name: {animal_data['name']} "

        if "diet" in animal_data["characteristics"]:
            output += (
                f"Diet: "
                f"{animal_data['characteristics']['diet']} "
            )

        if "locations" in animal_data:
            output += (
                f"Location: "
                f"{', '.join(animal_data['locations'])} "
            )

        if "type" in animal_data["characteristics"]:
            output += (
                f"Type: "
                f"{animal_data['characteristics']['type']}"
            )

        output += "\n</li>\n"

    return output


def main():
    """Generate animals.html from template and JSON data."""

    data = load_data("animals_data.json")

    output = generate_animals_html(data)

    with open("animals_template.html", "r") as handle:
        html_template = handle.read()

    final_html = html_template.replace(
        "__REPLACE_ANIMALS_INFO__",
        output
    )

    with open("animals.html", "w") as handle:
        handle.write(final_html)

    print(output)


if __name__ == "__main__":
    main()