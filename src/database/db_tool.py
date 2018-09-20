import os
import importlib

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.database.base import Base
from src.tools.globals.singleton import Singleton
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import and_


class DbTool(metaclass=Singleton):

    def __init__(self):
        db_name = 'game.db'
        if os.path.isfile(db_name):
            os.remove(db_name)
        self.engine = create_engine('sqlite:///{}'.format(db_name), echo=False)
        self.session = Session(self.engine)
        Base.metadata.create_all(self.engine)

    def get_all_rows(self, data: tuple) -> list:
        module, table_name = data
        table = getattr(importlib.import_module(module), table_name)
        return self.session.query(table)

    def get_rows_where(self, data: tuple, second_column: int or str or bool, equal: bool=True):
        module, table_name, col = data
        table = getattr(importlib.import_module(module), table_name)
        first_column = getattr(table, col)
        return self.session.query(table).filter(first_column == second_column).all() if equal \
            else self.session.query(table).filter(first_column != second_column).all()

    def get_one_row_where(self, data: tuple, second_to_eq):
        module, table_name, col = data
        table = getattr(importlib.import_module(module), table_name)
        result = self.session.query(table).filter(getattr(table, col) == second_to_eq)
        try:
            return result.one()
        except NoResultFound:
            return None

    def get_one_row_where_two_conditions(self, data: tuple, second_column: tuple):
        module, table_name, (col_x, col_y) = data
        table = getattr(importlib.import_module(module), table_name)
        first_col_x = getattr(table, col_x)
        first_col_y = getattr(table, col_y)
        return self.session.query(table).filter(and_(first_col_x == second_column[0],
                                                     first_col_y == second_column[1])).one()

    def insert_row(self, row):
        self.session.add(row)

    def finish(self):
        self.session.commit()
        self.session.close()

    @property
    def get_player(self):
        return self.get_one_row_where(('src.objects.creatures', 'SpawnedCreature', 'id_spawned_creature'), 0)
