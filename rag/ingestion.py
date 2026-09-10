import json
import os


def load_plants(json_path):
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"Dataset not found: {json_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        plants = json.load(f)

    if not isinstance(plants, list):
        raise ValueError("enhanced_herb.json must contain a list of plants.")


    return plants

if __name__ == "__main__":
    plants = load_plants("data/enhanced_herb.json")
    print(f"Loaded {len(plants)} plants")