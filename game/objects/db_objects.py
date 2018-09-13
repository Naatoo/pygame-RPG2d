from database.tables import FieldTypeTable, FieldTable, ItemTable, BoundedItemTable, CreatureGroupTable,\
    CreatureTypeTable, SpawnedCreatureTable, ContainerTypeTable, ContainerTable
from database.dbtools import DbTool


class FieldType(FieldTypeTable):

    def __repr__(self):
        fmt = "FieldType(id={}, name={], sign={}, accessible={}"
        return fmt.format(self.id_field_type, self.name, self.sign, self.accessible)


class Field(FieldTable):

    def __repr__(self):
        fmt = "Field(id={}, type_name={})"
        return fmt.format(self.id_field, self.type.name)

    @property
    def type(self):
        return DbTool().get_one_row(FieldType, FieldType.id_field_type, self.field_type_id)


class CreatureGroup(CreatureGroupTable):

    def __repr__(self):
        fmt = 'CreatureGroup(id={}, name={}, talkative={}, trader={}'
        return fmt.format(self.id_creature_group, self.name, self.talkative, self.trader)


class CreatureType(CreatureTypeTable):

    def __repr__(self):
        fmt = 'CreatureType(id={}, name={}, strength={}, agility={}, type_name={}'
        return fmt.format(self.id_creature_type, self.name, self.strength, self.agility, self.group.name)

    @property
    def group(self):
        return DbTool().get_one_row(CreatureGroup, CreatureGroup.id_creature_group, self.type_id)


class SpawnedCreature(SpawnedCreatureTable):

    def __repr__(self):
        fmt = "SpawnedCreature(id={}, name={}, field_id={})"
        return fmt.format(self.id_spawned_creature, self.name if self.name is not None else self.type.name, self.spawned_creature_field_id)

    def __str__(self):
        fmt = '{} stands on field {}'
        return fmt.format(self.name if self.name is not None else self.type.name, self.spawned_creature_field_id)

    def __len__(self):
        return len(self.equipment)

    def __bool__(self):
        return True if bool(self.equipment) else False

    def __contains__(self, elem):
        if isinstance(elem, str):
            return True if elem in self.get_items_names() else False
        elif isinstance(elem, Item):
            return True if elem.name in self.get_items_names() else False
        else:
            raise TypeError("Checked element must be str or Item")

    def __abs__(self):
        return sum([item.weight * item. quantity for item in self.equipment])

    def get_items_names(self):
        return [item.name for item in self.equipment]

    @property
    def equipment(self):
        return DbTool().get_all_rows(BoundedItem, BoundedItem.spawned_creature_id, self.id_spawned_creature)

    @property
    def type(self):
        return DbTool().get_one_row(CreatureType, CreatureType.id_creature_type, self.spawned_creature_type_id)


class Item(ItemTable):

    def __repr__(self):
        fmt = 'Item(id={}, name={}, weight={}, value ={}'
        return fmt.format(self.id_item, self.name, self.weight, self.value)

    def __str__(self):
        fmt = '{} weights {} and has the value of {}'
        return fmt.format(self.name, self.weight, self.value)


class BoundedItem(BoundedItemTable):

    def __repr__(self):
        fmt = 'Item(name={}, quantity={})'
        return fmt.format(self.name, self.quantity)

    def get_this_item(self):
        return DbTool().get_one_row(Item, Item.id_item, self.item_id)

    @property
    def name(self):
        return self.get_this_item().name

    @property
    def weight(self):
        return self.get_this_item().weight


class ContainerType(ContainerTypeTable):

    def __repr__(self):
        fmt = 'ContainerType(id={}, name={}, capacity={})'
        return fmt.format(self.id_container_type, self.name, self.capacity)


class Container(ContainerTable):

    def __repr__(self):
        fmt = 'Container(id={}, name={})'
        return fmt.format(self.id_container, self.name)
