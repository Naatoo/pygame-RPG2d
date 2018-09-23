import pygame

from src.database.db_tool import DbTool
from src.tools.globals.singleton import Singleton


class DisplayTool(metaclass=Singleton):

    def __init__(self):
        width = 1280
        height = 800
        self.display_window = pygame.display.set_mode((width, height))
        self.tiles_images = {field_type.name: pygame.image.load(field_type.image)
                             for field_type in DbTool().get_all_rows(('src.objects.fields', 'FieldType'))}
        self.creatures_images = {creature_type.name: pygame.image.load(creature_type.image)
                                 for creature_type in DbTool().get_all_rows(('src.objects.creatures', 'CreatureType'))}
        self.items_images = {item.name: pygame.image.load(item.image)
                             for item in DbTool().get_all_rows(('src.objects.items', 'Item'))}
        self.fields = DbTool().get_all_rows(('src.objects.fields', 'Field'))
        self.creatures = DbTool().get_all_rows(('src.objects.creatures', 'SpawnedCreature'))
        self.tiles_items = DbTool().get_rows_where(("src.objects.items", "BoundedItem", "field_id"), None, equal=False)
        self.player_eq_items = DbTool().get_rows_where(('src.objects.containers', 'ContainerSlot', 'container_id'), 1)

    def startup_display(self):
        self.display_tiles()
        self.display_creatures()
        self.display_tiles_items()
        self.display_player_eq_tile()
        self.display_eq_items()

    def blit_image(self, image: str, coordinates: tuple):
        self.display_window.blit(image, coordinates)

    def display_tiles(self):
        for field in self.fields:
            self.blit_image(self.tiles_images[field.type.name], (field.y * 32, field.x * 32))

    def display_creatures(self, refresh=False):
        if refresh:
            self.creatures = DbTool().get_all_rows(('src.objects.creatures', 'SpawnedCreature'))
        for creature in self.creatures:
            self.blit_image(self.creatures_images[creature.type.name], (creature.x * 32, creature.y * 32))

    def display_tiles_items(self, refresh=False):
        if refresh:
            self.tiles_items = DbTool().get_rows_where(
                ("src.objects.items", "BoundedItem", "field_id"), None, equal=False)
        for element in self.tiles_items:
            field = DbTool().get_one_row_where(("src.objects.fields", "Field", "id_field"), element.field_id)
            self.blit_image(self.items_images[element.item.name], (field.x * 32, field.y * 32))

    def display_player_eq_tile(self):
        self.display_window.blit(pygame.image.load('src/resources/image/ui/eq.png'), (640, 120))

    def display_eq_items(self, refresh=False):
        if refresh:
            self.player_eq_items = DbTool().get_rows_where(
                ('src.objects.containers', 'ContainerSlot', 'container_id'), 1)
        eq_x_offset = 640
        eq_y_offset = 120
        for container_slot in self.player_eq_items:
            element = container_slot.item
            if element is not None:
                self.blit_image(pygame.image.load(element.item.image),
                                (container_slot.pixels_x + eq_x_offset, container_slot.pixels_y + eq_y_offset))
            else:
                continue

    def update_one_tile(self, coordinates):
        field = DbTool().get_one_row_where_two_conditions(('src.objects.fields', 'Field', ('x', 'y')), coordinates)
        image = DbTool().get_one_row_where(
            ('src.objects.fields', 'FieldType', 'id_field_type'), field.field_type_id).image
        self.blit_image(pygame.image.load(image), (field.x * 32, field.y * 32))
