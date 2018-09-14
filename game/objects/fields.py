from database.dbtools import DbTool
from database.tables import FieldTypeTable, FieldTable


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
        return DbTool().get_one_row(('game.objects.fields', 'FieldType', 'id_field_type'), self.field_type_id)
