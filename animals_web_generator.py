import json


def load_data(file_path):
    """Load a JSON file."""

    with open(file_path, "r") as handle:
        return json.load(handle)


def get_skin_types(data):
    """Return all available skin types."""

    skin_types = set()

    for animal_obj in data:
        characteristics = animal_obj.get("characteristics", {})

        if "skin_type" in characteristics:
            skin_types.add(characteristics["skin_type"])

    return sorted(skin_types)


def serialize_animal(animal_obj):
    """Serialize one animal into HTML."""

    output = ""

    output += '<li class="cards__item">\n'

    if "name" in animal_obj:
        output += (
            f'  <div class="card__title">'
            f'{animal_obj["name"]}</div>\n'
        )

    output += '  <div class="card__text">\n'
    output += "    <ul>\n"

    characteristics = animal_obj.get("characteristics", {})

    if "diet" in characteristics:
        output += (
            f'      <li><strong>Diet:</strong> '
            f'{characteristics["diet"]}</li>\n'
        )

    if "locations" in animal_obj:
        output += (
            f'      <li><strong>Location:</strong> '
            f'{", ".join(animal_obj["locations"])}</li>\n'
        )

    if "type" in characteristics:
        output += (
            f'      <li><strong>Type:</strong> '
            f'{characteristics["type"]}</li>\n'
        )

    output += "    </ul>\n"
    output += "  </div>\n"
    output += "</li>\n"

    return output


def generate_animals_html(data, selected_skin_type):
    """Generate HTML for animals with selected skin type."""

    output = ""

    for animal_obj in data:
        characteristics = animal_obj.get("characteristics", {})
        skin_type = characteristics.get("skin_type", "")

        if skin_type.lower() == selected_skin_type.lower():
            output += serialize_animal(animal_obj)

    return output


def main():
    """Generate animals.html from template and JSON data."""

    data = load_data("animals_data.json")

    skin_types = get_skin_types(data)

    print("Available skin types:")
    for skin_type in skin_types:
        print(f"- {skin_type}")

    selected_skin_type = input("\nPlease enter a skin type: ").strip()

    animals_html = generate_animals_html(data, selected_skin_type)

    with open("animals_template.html", "r") as handle:
        html_template = handle.read()

    final_html = html_template.replace(
        "__REPLACE_ANIMALS_INFO__",
        animals_html
    )

    with open("animals.html", "w") as handle:
        handle.write(final_html)

    print("Website created successfully!")


if __name__ == "__main__":
    main()