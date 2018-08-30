from pathlib import Path
import os


MAIN_DIR = str(Path(__file__).parent.parent)
DATA_DIR = os.path.join(MAIN_DIR, "initializers/")
MAP_DATA_FILE = os.path.join(DATA_DIR, "map_data.json")
CREATURES_DATA_FILE = os.path.join(DATA_DIR, "creatures_data.json")
ITEMS_DATA_FILE = os.path.join(DATA_DIR, "items_data.json")
