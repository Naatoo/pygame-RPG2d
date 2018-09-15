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


def blit(image: str, coordinates: tuple):
    Display().get_display_window().blit(image, coordinates)
