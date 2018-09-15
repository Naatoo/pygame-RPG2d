from src.database.dbtools import DbTool


class WorldMap:
    def __init__(self):
        self.size = 20
        self.__fields = DbTool().get_full_rows(('src.objects.fields', 'Field'))

    def __getitem__(self, item):
        return self.__fields[item - 1]

    def __setitem__(self, key, value, asd):
        pass

    def __format__(self, format_spec='c'):
        if format_spec in "tc":
            list_to_format = ['{} ' if field.id_field % self.size != 0 else '{}\n' for field in self.__fields]
            joined_list = "".join(list_to_format)
            if format_spec == "t":
                return joined_list.format(*(field.type.sign for field in self.__fields))
            elif format_spec == "c":
                return joined_list.format(*(field.type.sign if field.id_field != self.player_field_id
                                            else "X" for field in self.__fields))
        elif format_spec == "i":
            list_to_format = ['{}' + " " * round(1 / (len(str(field.id_field)) / 3)) if field.id_field % self.size != 0
                              else '{}\n' for field in self.__fields]
            joined_list = "".join(list_to_format)
            return joined_list.format(*(field.id_field for field in self.__fields))

    def __repr__(self):
        return format(self, "c")

    @property
    def creature_field_id(self):
        return [character.spawned_creature_field_id for character in
                DbTool().get_full_rows(('src.objects.creatures', 'SpawnedCreature'))]

    @property
    def player_field_id(self):
        return DbTool().get_one_row(('src.objects.creatures', 'SpawnedCreature', 'id_spawned_creature'), 0)\
            .spawned_creature_field_id
