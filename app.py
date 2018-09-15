from src.database.dbtools import DbTool
from src.database.initial_data_insertion import load_initial_data
from src.objects.world_map import WorldMap
from src.operations.input_checker import ActionChecker
from src.game.main import game_loop

try:
    dbtool = DbTool()
    load_initial_data()
    world_map = WorldMap()
    action_checker = ActionChecker()
    game_loop()

finally:
    DbTool().finish()
