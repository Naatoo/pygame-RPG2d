import os
import importlib

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.database.base import Base
from src.tools.globals.singleton import Singleton
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import and_, tuple_


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

    def get_element_in_coordinates(self, data: tuple, x: int, y: int):
        module, table_name = data
        table = getattr(importlib.import_module(module), table_name)
        first_col_x = getattr(table, 'x')
        first_col_y = getattr(table, 'y')
        try:
            return self.session.query(table).filter(and_(first_col_x == x, first_col_y == y)).one()
        except NoResultFound:
            return None

    def get_rows_where_coordinates_in(self, data: tuple, x_tuple: tuple, y_tuple: tuple):
        module, table_name = data
        table = getattr(importlib.import_module(module), table_name)
        first_col_x = getattr(table, 'x')
        first_col_y = getattr(table, 'y')
        return self.session.query(table).filter(tuple_(first_col_x, first_col_y).in_([x_tuple, y_tuple])).all()

    def get_rows_between(self, data: tuple, x_range: tuple, y_range: tuple):
        module, table_name = data
        table = getattr(importlib.import_module(module), table_name)
        return self.session.query(table).filter(and_(getattr(table, "x").between(x_range[0], x_range[1]),
                                                     getattr(table, "y").between(y_range[0], y_range[1]))).all()

    def update_row(self, data: tuple, second_to_eq, columns_to_update: dict):
        module, table_name, col = data
        table = getattr(importlib.import_module(module), table_name)
        return self.session.query(table).filter(getattr(table, col) == second_to_eq).update(columns_to_update)

    def insert_row(self, row):
        self.session.add(row)

    def finish(self):
        self.session.commit()
        self.session.close()

    @property
    def get_player(self):
        return self.get_one_row_where(('src.objects.creatures', 'SpawnedCreature', 'id_spawned_creature'), 0)
