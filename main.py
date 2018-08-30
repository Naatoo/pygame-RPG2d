from database.dbtools import DbTool
from initializers.initial_data_insertion import load_initial_data
from game.objects.world_map import WorldMap
from game.operations.input_checker import ActionChecker


try:
    dbtool = DbTool()
    load_initial_data()
    world_map = WorldMap()
    action_checker = ActionChecker()

    while True:
        print(world_map)
        action_checker(input("What do you want to do?"))

finally:
    DbTool().finish()
