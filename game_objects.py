from create_tables import FieldTable, ItemTable, BoundedItemTable, CharacterTable
from dbtools import DbTool


class Field(FieldTable):

    def __repr__(self):
        fmt = "Field(id={}, biome={}, weather={})"
        return fmt.format(self.id, self.biome, self.weather)


class Item(ItemTable):

    def __repr__(self):
        fmt = 'Item(id={}, name={}, weight={}, value ={}'
        return fmt.format(self.id, self.name, self.weight, self.value)

    def __str__(self):
        fmt = '{} weights {} and has the value of {}'
        return fmt.format(self.name, self.weight, self.value)


class BoundedItem(BoundedItemTable):

    def __repr__(self):
        fmt = 'Item(name={}, quantity={})'
        return fmt.format(self.name, self.quantity)

    def get_this_item(self):
        return DbTool().get_one_row(Item, Item.id, self.item_id)

    @property
    def name(self):
        return self.get_this_item().name

    @property
    def weight(self):
        return self.get_this_item().weight


class Character(CharacterTable):

    def __repr__(self):
        fmt = "Character(id={}, name={}, field_id={})"
        return fmt.format(self.id, self.name, self.field_id)

    def __str__(self):
        fmt = '{} stands on field {}'
        return fmt.format(self.name, self.field_id)

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
        return DbTool().get_all_rows(BoundedItem, BoundedItem.character_id, self.id)

    def move(self, direction):
        fields_changer = {"N": -20, "S": 20, "W": -1, "E": 1}
        if self.field_id + fields_changer[direction] in self.check_possibility_to_move():
            self.field_id += fields_changer[direction]

    def check_possibility_to_move(self):
        forbidden_id_dict = {range(1, 21): - 20, range(1, 382, 20): - 1, range(381, 401): 20, range(20, 401, 20): 1}
        return [self.field_id + id_changer for forbidden_fields, id_changer in forbidden_id_dict.items()
                if self.field_id not in forbidden_fields]
