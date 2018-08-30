from pathlib import Path
import os

MAIN_DIR = str(Path(__file__).parent.parent)
DATA_DIR = os.path.join(MAIN_DIR, "initializers/")
DATA_FILE = os.path.join(DATA_DIR, "data.json")
