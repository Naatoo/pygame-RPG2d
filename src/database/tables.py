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


class ContainerTypeTable(Base):
    __tablename__ = 'ContainerType'

    id_container_type = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)


class ContainerTable(Base):
    __tablename__ = 'Container'

    id_container = Column(Integer, primary_key=True)
    custom_name = Column(String, nullable=True)
    capacity = Column(Integer, nullable=True)
    container_type_id = Column(Integer, ForeignKey('ContainerType.id_container_type'), nullable=False)
    container_creature_id = Column(Integer, ForeignKey('SpawnedCreature.id_spawned_creature'), nullable=True)
    x = Column(Integer, ForeignKey("Field.x"))
    y = Column(Integer, ForeignKey("Field.y"))


class ContainerSlotTable(Base):
    __tablename__ = 'ContainerSlot'

    id_container_slot = Column(Integer, primary_key=True)
    pixels_x = Column(Integer, nullable=False)
    pixels_y = Column(Integer, nullable=False)
    container_id = Column(Integer, ForeignKey('Container.id_container'), nullable=False)


class ItemTypeTable(Base):
    __tablename__ = 'ItemType'

    id_item_type = Column(String(3), primary_key=True)
    name = Column(String, nullable=False)
    consumable = Column(Boolean, nullable=False)
    special_effect = Column(String(3), nullable=True)


class ItemTable(Base):
    __tablename__ = 'Item'

    id_item = Column(Integer, primary_key=True)
    name = Column(String)
    weight = Column(Integer)
    value = Column(Integer)
    image = Column(String)
    item_type_id = Column(String(3), ForeignKey("ItemType.id_item_type"))


class BoundedItemTable(Base):
    __tablename__ = 'BoundedItem'

    id_bounded_item = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    item_id = Column(Integer, ForeignKey("Item.id_item"))
    container_slot_id = Column(Integer, ForeignKey("ContainerSlot.id_container_slot"))
