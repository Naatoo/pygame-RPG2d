import pygame

from src.database.db_tool import DbTool
from src.tools.globals.singleton import Singleton
from src.events.display.sprites import ItemSprite, CreatureSprite
from src.tools.globals.constants import pixels_changer


class DisplayTool(metaclass=Singleton):

    def __init__(self):
        width = 1280
        height = 960
        self.display_window = pygame.display.set_mode((width, height))

        self.camera_x = DbTool().get_player.x
        self.camera_y = DbTool().get_player.y

        self.single_tiles = 7
        self.both_tiles = self.single_tiles * 2
        self.all_tiles = self.both_tiles + 1
        self.fields = [field for field in DbTool().get_rows_between(
            ('src.objects.fields', 'Field'), self.query_tuple('x'), self.query_tuple('y'))]
        self.field_type_image = {
            field_type.id_field_type: pygame.transform.scale2x(pygame.image.load(field_type.image)).convert()
            for field_type in DbTool().get_all_rows(('src.objects.fields', 'FieldType'))}
        self.item_type_image = {item.id_item: pygame.transform.scale2x(pygame.image.load(item.image)).convert_alpha()
                                for item in DbTool().get_all_rows(('src.objects.items', 'Item'))}
        self.creatures_images = {
            creature_type.id_creature_type: pygame.transform.scale2x(
                pygame.image.load(creature_type.image)).convert_alpha()
            for creature_type in DbTool().get_all_rows(('src.objects.creatures', 'CreatureType'))}
        self.sprite_group_items = pygame.sprite.Group()
        self.sprite_group_creatures = pygame.sprite.Group()
        self.dragged_item_group = pygame.sprite.GroupSingle()

        self.refresh()

    def refresh(self):
        for item in self.get_items():
            if item not in [sprite.obj for sprite in self.sprite_group_items.sprites()]:
                self.sprite_group_items.add(ItemSprite(item, self.item_type_image[item.item_id]))
        for sprite in self.sprite_group_items.sprites():
            if sprite.obj not in self.get_items():
                self.sprite_group_items.remove(sprite)

        for creature in self.get_creatures():
            if creature not in [sprite.obj for sprite in self.sprite_group_creatures.sprites()]:
                self.sprite_group_creatures.add(
                    CreatureSprite(creature, self.creatures_images[creature.spawned_creature_type_id]))
        for sprite in self.sprite_group_creatures.sprites():
            if sprite.obj not in self.get_creatures():
                self.sprite_group_creatures.remove(sprite)

        self.reload_background()

        self.sprite_group_creatures.update(self.fields[0])
        self.sprite_group_items.update(self.fields[0])
        # TODO remove old sprites from display
        self.sprite_group_items.draw(self.display_window)
        self.sprite_group_creatures.draw(self.display_window)
        # TODO update only specific part of display
        pygame.display.update()

    def get_items(self):
        return DbTool().get_rows_between(('src.objects.items', 'BoundedItem'),
                                         (self.fields[0].x, self.fields[-1].x),
                                         (self.fields[0].y, self.fields[-1].y))

    def get_creatures(self):
        return DbTool().get_rows_between(('src.objects.creatures', 'SpawnedCreature'),
                                         (self.fields[0].x, self.fields[-1].x),
                                         (self.fields[0].y, self.fields[-1].y))

    def reload_background(self):
        self.update_camera()
        for field in self.fields:
            self.display_window.blit(self.field_type_image[field.field_type_id],
                                     ((field.x - self.fields[0].x) * pixels_changer,
                                      (field.y - self.fields[0].y) * pixels_changer))

    def query_tuple(self, axis):
        if axis == "x":
            return self.camera_x - self.single_tiles, self.camera_x + self.single_tiles
        elif axis == "y":
            return self.camera_y - self.single_tiles, self.camera_y + self.single_tiles

    def update_camera(self):
        self.camera_x = DbTool().get_player.x
        self.camera_y = DbTool().get_player.y
        self.fields = [field for field in DbTool().get_rows_between(
            ('src.objects.fields', 'Field'), self.query_tuple('x'), self.query_tuple('y'))]

    def set_dragged_item(self, position):
        for sprite in self.sprite_group_items.sprites():
            if (sprite.obj.x, sprite.obj.y) == (self.camera_x - 7 + position[0] // 64,
                                                self.camera_y - 7 + position[1] // 64):
                self.sprite_group_items.remove(sprite)
                self.dragged_item_group.add(sprite)

    def move_dragged_item(self, position):
        self.dragged_item_group.sprite.rect.topleft = (position[0], position[1])
        self.dragged_item_group.draw(self.display_window)
        pygame.display.update()
