from create_tables import FieldTable, ItemTable, EquipmentTable, CharacterTable
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


class Equipment(EquipmentTable):

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

    def __abs__(self):
        return sum([item.weight for item in self.items])

    def __str__(self):
        fmt = 'Equipment with id {} and capacity {}/{}'
        return fmt.format(self.id, abs(self), self.capacity)

    @property
    def items(self):
        return DbTool().get_all_rows(Item, Item.equipment_id, self.id)

    def get_items_names(self):
        return [item.name for item in self.items]


class Character(CharacterTable):

    def __repr__(self):
        fmt = "Character(id={}, name={}, field_id={})"
        return fmt.format(self.id, self.name, self.field_id)

    def __str__(self):
        fmt = '{} stands on field {}'
        return fmt.format(self.name, self.field_id)

    @property
    def equipment(self):
        return DbTool().get_one_row(Equipment, Equipment.character_id, self.id)

    def move(self, direction):
        fields_changer = {"N": -20, "S": 20, "W": -1, "E": 1}
        if self.field_id + fields_changer[direction] in self.check_possibility_to_move():
            self.field_id += fields_changer[direction]

    def check_possibility_to_move(self):
        forbidden_id_dict = {range(1, 21): - 20, range(1, 382, 20): - 1, range(381, 401): 20, range(20, 401, 20): 1}
        return [self.field_id + id_changer for forbidden_fields, id_changer in forbidden_id_dict.items()
                if self.field_id not in forbidden_fields]


class WorldMap:
    def __init__(self):
        self.size = 20
        self.__fields = DbTool().get_all_rows(Field)
        print(list(self.__fields))

    def __getitem__(self, item):
        return self.__fields[item - 1]

    def __setitem__(self, key, value, asd):
        pass

    def __format__(self, format_spec='c'):

        if format_spec in "tc":
            list_to_format = ['{} ' if field.id % self.size != 0 else '{}\n' for field in self.__fields]
            joined_list = "".join(list_to_format)
            if format_spec == "t":
                return joined_list.format(*(field.biome for field in self.__fields))
            elif format_spec == "c":
                return joined_list.format(*(field.biome if field.id not in self.player_id
                                            else "X" for field in self.__fields))
        elif format_spec == "i":
            list_to_format = ['{}' + " " * round(1 / (len(str(field.id)) / 3)) if field.id % self.size != 0
                              else '{}\n' for field in self.__fields]
            joined_list = "".join(list_to_format)
            return joined_list.format(*(field.id for field in self.__fields))

    def __repr__(self):
        return format(self, "t")

    @property
    def player_id(self):
        return [character.field_id for character in DbTool().get_all_rows(Character)]
