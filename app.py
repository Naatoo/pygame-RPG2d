from src.database.db_tool import DbTool
from src.database.initial_data_insertion import load_initial_data
from src.game.main import game_loop

try:
    dbtool = DbTool()
    load_initial_data()
    game_loop()

finally:
    DbTool().finish()
