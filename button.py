import pygame
import json

from variables import *

class Button(pygame.sprite.Sprite):
    def __init__(self, size, image="assets/buttons/btn_spritesheet.png", jdata="assets/buttons/btn_spritesheet.json"):
        super().__init__()
        tmp = pygame.image.load(image)
        with open(jdata, "rb") as j:
            self.__data = json.load(j)
            j.close()

        self.base_image = pygame.transform.scale(self.crop(tmp.copy(), "normal"), size)
        self.h_image = pygame.transform.scale(self.crop(tmp.copy(), "hover"), size)
        self.image = self.base_image.copy()
        self.rect = self.image.get_rect()
        self.__activated = False
        self.fun = None

    def crop(self, tmp, header):
        x, y, w, h = self.__data["frames"][header]["frame"].values()
        r = pygame.Rect(x, y, w, h)
        img = tmp.subsurface(r)
        img.set_colorkey(BLACK)

        return img

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

    def deactivate(self):
        self.__activated = False