from src.database.dbtools import DbTool
from src.database.tables import ContainerTypeTable, ContainerTable, ContainerSlotTable
from src.objects.items import Item


class ContainerType(ContainerTypeTable):

    def __repr__(self):
        fmt = 'ContainerType(id={}, name={}, capacity={})'
        return fmt.format(self.id_container_type, self.name, self.capacity)


class Container(ContainerTable):

    def __repr__(self):
        fmt = 'Container(id={}, name={})'
        return fmt.format(self.id_container, self.custom_name)

    def __str__(self):
        return self.custom_name if self.custom_name is not None else self.type.name

    def __len__(self):
        return len(self.content)

    def __bool__(self):
        return True if bool(self.content) else False

    def __abs__(self):
        return sum([item.weight * item.quantity for item in self.content])

    def __contains__(self, elem):
        items_names = [item.name for item in self.equipment]
        if isinstance(elem, str):
            return True if elem in items_names else False
        elif isinstance(elem, Item):
            return True if elem.name in items_names else False
        else:
            raise TypeError("Checked element must be str or Item")

    @property
    def content(self):
        return [item for item in DbTool().get_all_rows(
            ('src.objects.items', 'BoundedItem', 'container_id'), self.id_container)]

    @property
    def type(self):
        return DbTool().get_one_row(('src.objects.containers', 'ContainerType', 'id_container_type'),
                                    self.container_type_id)


class ContainerSlot(ContainerSlotTable):

    def __repr__(self):
        fmt = 'Container(id_slot={}, item={}, container_id={})'
        return fmt.format(self.id_container_slot, self.item.name, self.container_id)

    @property
    def item(self):
        return DbTool().get_one_row(('src.objects.items', 'BoundedItem', 'container_slot_id'), self.id_container_slot)
