import os
import importlib

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from src.database.base import Base
from src.tools.globals.singleton import Singleton


class DbTool(metaclass=Singleton):

    def __init__(self):
        db_name = 'game.db'
        if os.path.isfile(db_name):
            os.remove(db_name)
        self.engine = create_engine('sqlite:///{}'.format(db_name), echo=False)
        self.session = Session(self.engine)
        Base.metadata.create_all(self.engine)

    def get_full_rows(self, data: tuple):
        module, table_name = data
        table = getattr(importlib.import_module(module), table_name)
        return self.session.query(table)

    def get_all_rows(self, data: tuple, second_to_eq=None):
        module, table_name, col = data
        table = getattr(importlib.import_module(module), table_name)
        return self.session.query(table).filter(getattr(table, col) == second_to_eq).all()

    def get_one_row(self, data: tuple, second_to_eq):
        module, table_name, col = data
        table = getattr(importlib.import_module(module), table_name)
        try:
            return self.session.query(table).filter(getattr(table, col) == second_to_eq).one()
        except NoResultFound:
            pass

    def get_one_column(self, column_name):
        return self.session.query(column_name)

    def insert_row(self, row):
        self.session.add(row)

    def insert_many_rows(self, rows: list):
        for row in rows:
            self.session.add(row)

    def update_row(self, table_column_name: Base, equal_to_this: str or int, record: str, new_value: str or int):
        self.session.query().filter(table_column_name == equal_to_this).update({record: new_value})

    def finish(self):
        self.session.commit()
        self.session.close()

    @property
    def get_player(self):
        return self.get_one_row(('src.objects.creatures', 'SpawnedCreature', 'id_spawned_creature'), 0)
