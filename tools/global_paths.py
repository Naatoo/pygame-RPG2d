from pathlib import Path
import os


MAIN_DIR = str(Path(__file__).parent.parent)
DATA_DIR = os.path.join(MAIN_DIR, "initializers/")

CONTAINERS_DATA_DIR = os.path.join(DATA_DIR, "containers_data/")
MAP_DATA_DIR = os.path.join(DATA_DIR, "map_data/")

MAP_DATA_FILE = os.path.join(MAP_DATA_DIR, "map_data.json")
CREATURES_DATA_FILE = os.path.join(DATA_DIR, "creatures_data.json")
ITEMS_DATA_FILE = os.path.join(DATA_DIR, "items_data.json")

CONTAINERS_TYPES_DATA_FILE = os.path.join(CONTAINERS_DATA_DIR, "containers_types_data.json")
CREATURES_CONTAINERS_DATA_FILE = os.path.join(CONTAINERS_DATA_DIR, "creatures_containers_data.json")
FIELD_CONTAINERS_DATA_FILE = os.path.join(CONTAINERS_DATA_DIR, "field_containers_data.json")
STATIC_CONTAINERS_DATA_FILE = os.path.join(CONTAINERS_DATA_DIR, "static_containers_data.json")
