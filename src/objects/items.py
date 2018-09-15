from src.database.dbtools import DbTool
from src.database.tables import ItemTypeTable, ItemTable, BoundedItemTable


class ItemType(ItemTypeTable):

    def __repr__(self):
        fmt = 'ItemType(id={}, name={], consumable={}, special_effect={}'
        return fmt.format(self.id_item_type, self.name, self.consumable, self.special_effect)


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
        return DbTool().get_one_row(('src.objects.items', 'Item', 'id_item'), self.item_id)

    @property
    def name(self):
        return self.get_this_item().name

    @property
    def weight(self):
        return self.get_this_item().weight

    @property
    def item(self):
        return self.get_this_item()
