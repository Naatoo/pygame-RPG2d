import pygame

from src.tools.globals.constants import pixels_changer


class ItemSprite(pygame.sprite.Sprite):

    def __init__(self, obj, image):
        pygame.sprite.Sprite.__init__(self)
        self.obj = obj
        self.image = image
        self.rect = self.image.get_rect()

    def update(self, top_left_corner):
        self.rect.topleft = ((self.obj.x - top_left_corner.x) * pixels_changer, (self.obj.y - top_left_corner.y) * pixels_changer)


class CreatureSprite(pygame.sprite.Sprite):

    def __init__(self, obj, image):
        pygame.sprite.Sprite.__init__(self)
        self.obj = obj
        self.image = image
        self.rect = self.image.get_rect()

    def update(self, top_left_corner):
        self.rect.topleft = ((self.obj.x - top_left_corner.x) * pixels_changer, (self.obj.y - top_left_corner.y) * pixels_changer)