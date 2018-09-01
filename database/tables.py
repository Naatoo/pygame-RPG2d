from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from database.base import Base


class FieldTypeTable(Base):
    __tablename__ = 'FieldType'

    id_field_type = Column(Integer, primary_key=True)
    name = Column(String)
    sign = Column(String(1))
    accessible = Column(Boolean)


class FieldTable(Base):
    __tablename__ = 'Field'

    id_field = Column(Integer, primary_key=True)
    field_type_id = Column(Integer, ForeignKey('FieldType.id_field_type'))


class CreatureGroupTable(Base):
    __tablename__ = "CreatureGroup"

    id_creature_group = Column(Integer, primary_key=True)
    name = Column(String)
    talkative = Column(Boolean)
    trader = Column(Boolean)


class CreatureTypeTable(Base):
    __tablename__ = 'CreatureType'

    id_creature_type = Column(Integer, primary_key=True)
    name = Column(String)
    strength = Column(Integer)
    agility = Column(Integer)
    creature_group_id = Column(Integer, ForeignKey('CreatureGroup.id_creature_group'))


class SpawnedCreatureTable(Base):
    __tablename__ = 'SpawnedCreature'

    id_spawned_creature = Column(Integer, primary_key=True)
    custom_name = Column(String, nullable=True)
    spawned_creature_field_id = Column(Integer, ForeignKey('Field.id_field'))
    spawned_creature_type_id = Column(Integer, ForeignKey('CreatureType.id_creature_type'))


class ItemTable(Base):
    __tablename__ = 'Item'

    id_item = Column(Integer, primary_key=True)
    name = Column(String)
    weight = Column(Integer)
    value = Column(Integer)


class BoundedItemTable(Base):
    __tablename__ = 'BoundedItems'

    id_bounded_item = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    item_id = Column(Integer, ForeignKey("Item.id_item"))
    spawned_creature_id = Column(Integer, ForeignKey("SpawnedCreature.id_spawned_creature"))
