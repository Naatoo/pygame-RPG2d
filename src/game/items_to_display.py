import pygame

from src.database.dbtools import DbTool
from src.game.display import Display


def tiles():
    field_types = {field_type.name: pygame.image.load(field_type.image)
                   for field_type in DbTool().get_full_rows(('src.objects.fields', 'FieldType'))}
    fields = DbTool().get_full_rows(('src.objects.fields', 'Field'))
    for field in fields:
        blit(field_types[field.type.name], (field.y * 32, field.x * 32))


def player_icon():
    image = pygame.image.load('elf.png')
    player = DbTool().get_player
    blit(image, (player.x * 32, player.y * 32))


def blit(image: str, coordinates: tuple):
    Display().get_display_window().blit(image, coordinates)
