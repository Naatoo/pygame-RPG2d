from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base


class FieldTable(Base):
    __tablename__ = 'Field'

    id = Column(Integer, primary_key=True)
    biome = Column(String(3))
    weather = Column(String(3))


class ItemTable(Base):
    __tablename__ = 'Item'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    weight = Column(Integer)
    value = Column(Integer)
    equipment_id = Column(Integer, ForeignKey('Equipment.id'))


class EquipmentTable(Base):
    __tablename__ = 'Equipment'

    id = Column(Integer, primary_key=True)
    capacity = Column(Integer)
    character_id = Column(Integer, ForeignKey("Character.id"))


class CharacterTable(Base):
    __tablename__ = 'Character'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    field_id = Column(Integer, ForeignKey('Field.id'))
