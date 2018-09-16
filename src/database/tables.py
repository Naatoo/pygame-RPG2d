from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from src.database.base import Base


class FieldTypeTable(Base):
    __tablename__ = 'FieldType'

    id_field_type = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String)
    accessible = Column(Boolean)


class FieldTable(Base):
    __tablename__ = 'Field'

    id_field = Column(Integer, primary_key=True)
    x = Column(Integer)
    y = Column(Integer)
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
    image = Column(String)
    strength = Column(Integer)
    agility = Column(Integer)
    creature_group_id = Column(Integer, ForeignKey('CreatureGroup.id_creature_group'))


class SpawnedCreatureTable(Base):
    __tablename__ = 'SpawnedCreature'

    id_spawned_creature = Column(Integer, primary_key=True)
    custom_name = Column(String, nullable=True)
    x = Column(Integer, ForeignKey('Field.x'))
    y = Column(Integer, ForeignKey('Field.y'))
    spawned_creature_type_id = Column(Integer, ForeignKey('CreatureType.id_creature_type'))


class ContainerSlotTable(Base):
    __tablename__ = 'ContainerSlot'

    id_container_slot = Column(Integer, primary_key=True)
    pixels_x = Column(Integer, nullable=False)
    pixels_y = Column(Integer, nullable=False)
    container_id = Column(Integer, ForeignKey('BoundedItem.id_bounded_item'), nullable=False)


class ItemTypeTable(Base):
    __tablename__ = 'ItemType'

    id_item_type = Column(String(3), primary_key=True)
    name = Column(String, nullable=False)
    consumable = Column(Boolean, nullable=False)
    container = Column(Boolean, nullable=False)
    special_effect = Column(String(3), nullable=True)


class ItemTable(Base):
    __tablename__ = 'Item'

    id_item = Column(Integer, primary_key=True)
    name = Column(String)
    weight = Column(Integer)
    value = Column(Integer)
    image = Column(String)
    slots = Column(Integer, nullable=True)
    item_type_id = Column(String(3), ForeignKey("ItemType.id_item_type"))


class BoundedItemTable(Base):
    __tablename__ = 'BoundedItem'

    id_bounded_item = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("Item.id_item"))
    quantity = Column(Integer)
    field_id = Column(Integer, ForeignKey("Field.id_field"), nullable=True)
    creature_id = Column(Integer, ForeignKey("SpawnedCreature.id_spawned_creature"), nullable=True)
    container_id = Column(Integer, ForeignKey("BoundedItem.id_bounded_item"), nullable=True)
    container_slot_id = Column(Integer, ForeignKey("ContainerSlot.id_container_slot"), nullable=True)
