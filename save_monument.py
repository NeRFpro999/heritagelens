import json
from monument import Monument

# Create a Monument instance
monument = Monument(
    name="Eiffel Tower",
    country="France",
    year_built=1889,
    image_path="images/eiffel_tower.jpg",
    description="Iconic iron lattice tower in Paris"
)

# Convert to dictionary and save as JSON
with open("monument.json", "w") as f:
    json.dump(monument.to_dict(), f, indent=4)

print("Monument saved to monument.json")