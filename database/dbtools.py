from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database.base import Base
import os


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DbTool(metaclass=Singleton):

    def __init__(self):
        db_name = 'game.db'
        if os.path.isfile(db_name):
            os.remove(db_name)
        self.engine = create_engine('sqlite:///{}'.format(db_name), echo=False)
        self.session = Session(self.engine)
        Base.metadata.create_all(self.engine)

    def get_all_rows(self, table_name, first_to_eq=None, second_to_eq=None):
        return self.session.query(table_name).filter(first_to_eq == second_to_eq).all() if first_to_eq is not None \
            else self.session.query(table_name)

    def get_one_row(self, table_name, first_to_eq, second_to_eq):
        return self.session.query(table_name).filter(first_to_eq == second_to_eq).one()

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
