from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from database.base import Base


class FieldTable(Base):
    __tablename__ = 'Field'

    id = Column(Integer, primary_key=True)
    biome = Column(String(3))
    weather = Column(String(3))


class CreatureGroupTable(Base):
    __tablename__ = "CreatureGroup"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    talkative = Column(Boolean)
    trader = Column(Boolean)


class CreatureTypeTable(Base):
    __tablename__ = 'CreatureType'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    strength = Column(Integer)
    agility = Column(Integer)
    group_id = Column(Integer, ForeignKey('CreatureGroup.id'))


class SpawnedCreatureTable(Base):
    __tablename__ = 'SpawnedCreature'

    id = Column(Integer, primary_key=True)
    custom_name = Column(String, nullable=True)
    field_id = Column(Integer, ForeignKey('Field.id'))
    type_id = Column(Integer, ForeignKey('CreatureType.id'))


class ItemTable(Base):
    __tablename__ = 'Item'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    weight = Column(Integer)
    value = Column(Integer)


class BoundedItemTable(Base):
    __tablename__ = 'BoundedItems'

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("Item.id"))
    quantity = Column(Integer)
    character_id = Column(Integer, ForeignKey("SpawnedCreature.id"))
