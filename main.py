from dbtools import DbTool
from initial_data import insert_initial_data
from world_map import WorldMap


try:
    dbtool = DbTool()
    insert_initial_data()
    world_map = WorldMap()


finally:
    DbTool().finish()
