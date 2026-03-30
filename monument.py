import json
import os

class Monument:
    def __init__(self, name, country, year_built, image_paths, description=""):
        self.name = name
        self.country = country
        self.year_built = year_built
        self.image_paths = image_paths  # List of image file paths
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "country": self.country,
            "year_built": self.year_built,
            "image_paths": self.image_paths,
            "description": self.description
        }

    def save_to_json(self):
        # Create output directory for the monument
        output_dir = os.path.join("outputs", self.name.replace(" ", "_"))
        os.makedirs(output_dir, exist_ok=True)
        json_path = os.path.join(output_dir, "monument.json")
        with open(json_path, "w") as f:
            json.dump(self.to_dict(), f, indent=4)
        return output_dir

    def __repr__(self):
        return f"Monument({self.name}, {self.country}, {self.year_built})"


# Test it
if __name__ == "__main__":
    m = Monument("Colosseum", "Italy", 80, ["images/colosseum1.jpg", "images/colosseum2.jpg"], "Ancient Roman amphitheatre")
    print(m)
    print(m.to_dict())
    m.save_to_json()