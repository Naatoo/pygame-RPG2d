from dbtools import DbTool
from initial_data import insert_initial_data
from world_map import WorldMap
from action_checker import ActionChecker


try:
    dbtool = DbTool()
    insert_initial_data()
    world_map = WorldMap()
    action_checker = ActionChecker()

    while True:
        action_checker(input("What do you want to do?"))

finally:
    DbTool().finish()
