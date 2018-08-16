from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager
from map import Map


engine = create_engine('sqlite:///:memory:', echo=False)
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)


class Field(Base):

    __tablename__ = 'Field'

    id = Column(Integer, primary_key=True)
    biome = Column(String(3))
    weather = Column(String(3))

    def __repr__(self):
        fmt = "Field(id={}, biome={}, weather={})"
        return fmt.format(self.id, self.biome, self.weather)


class Item(Base):
    __tablename__ = 'Item'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    weight = Column(Integer)
    value = Column(Integer)
    equipment_id = Column(Integer, ForeignKey('Equipment.id'))

    def __repr__(self):
        fmt = 'Item(id={}, name={}, weight={}, value ={}'
        return fmt.format(self.id, self.name, self.weight, self.value)


class Equipment(Base):

    __tablename__ = 'Equipment'

    id = Column(Integer, primary_key=True)
    capacity = Column(Integer)
    character_id = Column(Integer, ForeignKey("Character.id"))

    def __repr__(self):
        fmt = 'Equipment(id={}, capacity={}, character_id={})'
        return fmt.format(self.id, self.capacity, self.character_id)

    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return True if bool(self.items) else False

    def __contains__(self, elem):
        if isinstance(elem, str):
            return True if elem in [item.name for item in self.items] else False
        elif isinstance(elem, Item):
            return True if elem.name in self.get_items_names() else False
        else:
            raise TypeError("Checked element must be str or Item")

    @property
    def items(self):
        return DbTools.get_all_rows(Item, Item.equipment_id, self.id)

    def get_items_names(self):
        return [item.name for item in self.items]


class Character(Base):

    __tablename__ = 'Character'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    field_id = Column(Integer, ForeignKey('Field.id'))

    def __repr__(self):
        fmt = "Character(id={}, name={}, field_id={})"
        return fmt.format(self.id, self.name, self.field_id)

    def move(self, direction):
        fields_changer = {"N": -20, "S": 20, "W": -1, "E": 1}
        if self.field_id + fields_changer[direction] in self.check_possibility_to_move():
            self.field_id += fields_changer[direction]

    def check_possibility_to_move(self):
        pos = []
        if self.field_id not in range(1, 21):
            pos.append(self.id - 20)
        if self.id not in range(1, 382, 20):
            pos.append(self.id - 1)
        if self.id not in range(381, 401):
            pos.append(self.id + 20)
        if self.id not in range(20, 401, 20):
            pos.append(self.id + 1)
        return pos


class DbTools:

    @staticmethod
    def get_all_rows(table_name, first_to_eq, second_to_eq):
        return session.query(table_name).filter(first_to_eq == second_to_eq).all()


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


with session_scope() as session:

    Base.metadata.create_all(engine)

    map = Map(session, Field)
    map.insert_data(session, Field)

    player1 = Character(name="Player", field_id=12)
    session.add(player1)

    eq1 = Equipment(capacity=250, character_id=1)
    session.add(eq1)

    for name, weight, value in zip(["Apple", "Potato", "Watermelon"], [3, 2, 8], [5, 3, 12]):
        session.add(Item(name=name, weight=weight, value=value, equipment_id=1))
    session.add(Item(name='Onion', weight=2, value=5, equipment_id=2))

    session.commit()
