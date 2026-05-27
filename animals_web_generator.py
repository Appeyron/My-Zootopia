import json


def load_data(file_path):
    """Load a JSON file."""

    with open(file_path, "r") as handle:
        return json.load(handle)


def generate_animals_html(data):
    """Generate HTML for all animals."""

    output = ""  # define an empty string

    for animal_data in data:

        # append information to each string
        output += '<li class="cards__item">\n'

        if "name" in animal_data:
            output += (
                f"Name: "
                f"{animal_data['name']}<br/>\n"
            )

        if "diet" in animal_data["characteristics"]:
            output += (
                f"Diet: "
                f"{animal_data['characteristics']['diet']}<br/>\n"
            )

        if "locations" in animal_data:
            output += (
                f"Location: "
                f"{', '.join(animal_data['locations'])}<br/>\n"
            )

        if "type" in animal_data["characteristics"]:
            output += (
                f"Type: "
                f"{animal_data['characteristics']['type']}<br/>\n"
            )

        output += "</li>\n"

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


if __name__ == "__main__":
    main()