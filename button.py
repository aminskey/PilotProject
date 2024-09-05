# More to come
import pygame
import json

from pygame.locals import *
from variables import *

class Button(pygame.sprite.Sprite):
    def __init__(self, image, size):
        super().__init__()
        tmp = pygame.image.load(image)
        #self.__data = json.load(jdata)
        self.base_image = pygame.transform.scale(tmp, size)
        self.h_image = pygame.transform.scale(pygame.image.load("assets/buttons/Marine life button 2.png"), size)
        self.image = self.base_image.copy()
        self.rect = self.image.get_rect()
        self.__activated = False

    def addText(self, msgObj, pos):
        msgObj.rect.center = pos
        self.base_image.blit(msgObj.image, msgObj.rect)
        self.h_image.blit(msgObj.image, msgObj.rect)

    def update(self, *args, **kwargs):
        if isInBounds(pygame.mouse.get_pos(), 0, self.rect.topleft, self.rect.bottomright):
            self.image = self.h_image.copy()
            if pygame.mouse.get_pressed()[0]:
                self.__activated = True
            else:
                self.__activated = False
        else:
            self.image = self.base_image.copy()

    @property
    def activated(self):
        return self.__activated