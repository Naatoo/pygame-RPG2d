import pygame

from src.database.dbtools import DbTool
from src.game.display import Display


def display_tiles():
    field_types = {field_type.name: pygame.image.load(field_type.image)
                   for field_type in DbTool().get_full_rows(('src.objects.fields', 'FieldType'))}
    fields = DbTool().get_full_rows(('src.objects.fields', 'Field'))
    for field in fields:
        blit(field_types[field.type.name], (field.y * 32, field.x * 32))


def display_creatures():
    for creature in DbTool().get_full_rows(('src.objects.creatures', 'SpawnedCreature')):
        blit(pygame.image.load(creature.type.image), (creature.x * 32, creature.y * 32))


def display_player_eq_tile():
    Display().get_display_window().blit(pygame.image.load('src/resources/image/ui/eq.png'), (640, 120))


def display_eq_items():
    eq_x_offset = 640
    eq_y_offset = 120
    for container_slot in DbTool().get_all_rows(('src.objects.containers', 'ContainerSlot', 'container_id'), 0):
        element = DbTool().get_one_row(('src.objects.items', 'BoundedItem', 'container_slot_id'),
                                       container_slot.id_container_slot)
        if element is not None:
            blit(pygame.image.load(element.item.image),
                 (container_slot.pixels_x + eq_x_offset, container_slot.pixels_y + eq_y_offset))
        else:
            continue


def blit(image: str, coordinates: tuple):
    Display().get_display_window().blit(image, coordinates)
