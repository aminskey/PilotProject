import pygame
import random

from math import degrees
from vector import Vector
from variables import *

class Fish(pygame.sprite.Sprite):
    def __init__(self, image, sizeF, screen, pos, v=(0, 0), loop=False):
        super().__init__()
        self.base_image = pygame.transform.scale_by(pygame.image.load(image), sizeF)
        self.image = self.base_image.copy()

        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.screen = screen

        if v[0] != 0 and v[1] != 0:
            self.__vel = Vector(v[0] * dTime, v[1] * dTime)
        else:
            self.__vel = Vector(random.randint(-3, 3) * dTime, random.randint(-3, 3) * dTime)
        self.loop = loop

    def borderCheck(self):
        if not isInRange(self.rect.centerx, self.base_image.get_width(), 0, self.screen.get_width()):
            self.__vel = Vector(-self.__vel.x, self.__vel.y * random.randint(-3, 3) / 5)
            self.rect.centerx += self.__vel.x * 2
        if not isInRange(self.rect.centery, self.base_image.get_height(), 0, self.screen.get_height()):
            self.__vel = Vector(self.__vel.x, -self.__vel.y)
            self.rect.centery += self.__vel.y * 2

    def update(self):
        if not self.loop:
            self.borderCheck()
        else:
            if self.rect.midright[0] < 0:
                self.rect.x = self.screen.get_width()
            elif self.rect.x > self.screen.get_width():
                self.rect.x = 0

        if self.__vel.x < 0:
            tmp = pygame.transform.flip(self.base_image, False, True)
        else:
            tmp = self.base_image.copy()
        self.image = pygame.transform.rotate(tmp, -degrees(self.__vel.polar360))

        if self.rect.centery < 0 or self.rect.centery > self.screen.get_height():
            self.rect.centery = self.screen.get_rect().centery

        self.rect.centerx += self.__vel.x
        self.rect.centery += self.__vel.y

    @property
    def angle(self):
        return self.__vel.polar360

    @property
    def pos(self):
        return self.rect.center

    @property
    def vel(self):
        return self.__vel
