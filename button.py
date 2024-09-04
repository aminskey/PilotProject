# More to come
import pygame

from pygame.locals import *
from variables import *

class Button(pygame.sprite.Sprite):
    def __init__(self, image, size, msgObj):
        super().__init__()
        tmp = pygame.image.load(image)
        self.base_image = pygame.transform.scale(tmp, size)
        self.h_image = pygame.transform.scale(pygame.image.load("assets/buttons/buttonDemo2.png"), size)
        self.image = self.base_image.copy()
        self.rect = self.image.get_rect()
        self.__msgObj = msgObj

        self.__msgObj.rect.center = (self.image.get_width()//2, self.image.get_height()//2)
        self.base_image.blit(self.__msgObj.image, self.__msgObj.rect)
        self.h_image.blit(self.__msgObj.image, self.__msgObj.rect)

    def update(self, *args, **kwargs):
        if isInBounds(pygame.mouse.get_pos(), 0, self.rect.topleft, self.rect.bottomright):
            self.image = self.h_image.copy()
        else:
            self.image = self.base_image.copy()