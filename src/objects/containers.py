from src.database.dbtools import DbTool
from src.database.tables import ContainerSlotTable


class ContainerSlot(ContainerSlotTable):

    def __repr__(self):
        if self.item is not None:
            fmt = 'Container(id_slot={}, item={}, container_id={})'
            return fmt.format(self.id_container_slot, self.item.name, self.container_id)
        else:
            fmt = 'Empty Container(id_slot={}, container_id={})'
            return fmt.format(self.id_container_slot, self.container_id)

    @property
    def item(self):
        return DbTool().get_one_row(('src.objects.items', 'BoundedItem', 'container_slot_id'), self.id_container_slot)
