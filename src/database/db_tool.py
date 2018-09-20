import os
import importlib

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.database.base import Base
from src.tools.globals.singleton import Singleton
from sqlalchemy.orm.exc import NoResultFound


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

    def insert_row(self, row):
        self.session.add(row)

    def finish(self):
        self.session.commit()
        self.session.close()

    @property
    def get_player(self):
        return self.get_one_row_where(('src.objects.creatures', 'SpawnedCreature', 'id_spawned_creature'), 0)