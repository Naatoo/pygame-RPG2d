from src.database.dbtools import DbTool
from src.database.tables import CreatureGroupTable, CreatureTypeTable, SpawnedCreatureTable


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
        return DbTool().get_one_row(('src.objects.creatures', 'CreatureGroup', 'id_creature_group'), self.type_id)


class SpawnedCreature(SpawnedCreatureTable):

    def __repr__(self):
        fmt = "SpawnedCreature(id={}, name={}, x={}, y={})"
        return fmt.format(self.id_spawned_creature, self.name if self.name is not None else self.type.name,
                          self.x, self.y)

    def __str__(self):
        fmt = '{} stands on field {},{}'
        return fmt.format(self.custom_name if self.custom_name is not None else self.type.name, self.x, self.y)

    @property
    def type(self):
        return DbTool().get_one_row(('src.objects.creatures', 'CreatureType', 'id_creature_type'),
                                    self.spawned_creature_type_id)