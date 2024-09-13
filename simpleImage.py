import pygame

from math import sin
from variables import *
from vector import Vector


class SimpleImage(pygame.sprite.Sprite):
    def __init__(self, imageURL, size=-1):
        super().__init__()
        self.base_image = pygame.image.load(imageURL)
        if isinstance(size, tuple):
            self.base_image = pygame.transform.scale(self.base_image, size)
        self.rect = self.base_image.get_rect()

        self.image = self.base_image.copy()

    @property
    def pos(self):
        return Vector(self.rect.x, self.rect.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def update(self):
        self.image = self.base_image.copy()

class Water(SimpleImage):
    def __init__(self, size=-1):
        super().__init__("assets/backgrounds/InGame/Vand.png", size)
        self.count = 0
        self.overlay = self.base_image.copy()
        self.overlay.set_alpha(100)

    def update(self, point):
        super().update()
        h = sin(self.count*0.025) * 10
        self.rect.midbottom = point
        self.rect.y += h * dTime
        self.count += 1