import json


def load_data(file_path):
    """Load a JSON file."""

    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serialize one animal into HTML."""

    output = ""

    output += '<li class="cards__item">\n'

    if "name" in animal_obj:
        output += (
            f'<div class="card__title">'
            f'{animal_obj["name"]}'
            f'</div>\n'
        )

    output += '<p class="card__text">\n'

    if "diet" in animal_obj["characteristics"]:
        output += (
            f'<strong>Diet:</strong> '
            f'{animal_obj["characteristics"]["diet"]}<br/>\n'
        )

    if "locations" in animal_obj:
        output += (
            f'<strong>Location:</strong> '
            f'{", ".join(animal_obj["locations"])}<br/>\n'
        )

    if "type" in animal_obj["characteristics"]:
        output += (
            f'<strong>Type:</strong> '
            f'{animal_obj["characteristics"]["type"]}<br/>\n'
        )

    output += "</p>\n"
    output += "</li>\n"

    return output


def generate_animals_html(data):
    """Generate HTML for all animals."""

    output = ""

    for animal_data in data:
        output += serialize_animal(animal_data)

    return output


def main():
    """Generate animals.html from template and JSON data."""

    data = load_data("animals_data.json")

    animals_html = generate_animals_html(data)

    with open("animals_template.html", "r") as handle:
        html_template = handle.read()

    final_html = html_template.replace(
        "__REPLACE_ANIMALS_INFO__",
        animals_html
    )

    with open("animals.html", "w") as handle:
        handle.write(final_html)


if __name__ == "__main__":
    main()