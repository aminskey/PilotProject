import pygame
import random

from math import degrees
from vector import Vector
from variables import *

# The fish class
class Fish(pygame.sprite.Sprite):
    """
        * Constructor
        * Takes following parameters
            - (image) Image URL
            - (scale factor) Scaling Factor
            - (screen) Display image to blit
            - (pos) position on screen
            - (v) Tuple representing velocity vector
            - (loop) if the fish should loop on screen.
    """
    def __init__(self, image, sizeF, screen, pos, v=(0, 0), loop=False):
        # calling parent constructor
        super().__init__()

        # creating base image, to be used as a preserved copy of image
        self.base_image = pygame.transform.scale_by(pygame.image.load(image), sizeF)

        # The main image to be displayed
        self.image = self.base_image.copy()

        # Get bounding box object of self.image
        self.rect = self.image.get_rect()

        # positioning sprite.
        self.rect.topleft = pos

        # setting display to screen
        self.screen = screen

        # assigning velocity vector
        if v[0] != 0 and v[1] != 0:
            self.__vel = Vector(v[0] * dTime, v[1] * dTime)
        else:
            self.__vel = Vector(random.choice((-2, 2)) * dTime, random.choice((-1, 1)) * dTime)
        self.loop = loop

    # Checking for border collision and handling it
    def borderCheck(self):
        if not isInRange(self.rect.centerx, self.base_image.get_width(), 0, self.screen.get_width()):
            self.__vel = Vector(-self.__vel.x, self.__vel.y * random.randint(-3, 3) / 5)
            self.rect.centerx += self.__vel.x * 2
        if not isInRange(self.rect.centery, self.base_image.get_height(), 0, self.screen.get_height()):
            self.__vel = Vector(self.__vel.x, -self.__vel.y)
            self.rect.centery += self.__vel.y * 2

    # Update function to be run every frame.
    def update(self):
        # if not loop initiated then handle border collision
        if not self.loop:
            self.borderCheck()
        else:
            # else if loop == true, then allow panning
            if self.rect.midright[0] < 0:
                self.rect.x = self.screen.get_width()
            elif self.rect.x > self.screen.get_width():
                self.rect.x = 0

        # if the fish is moving backwards, then flip the image.
        if self.__vel.x < 0:
            tmp = pygame.transform.flip(self.base_image, False, True)
        else:
            # If not, then reflip the image
            # We do not want moonwalking fish
            tmp = self.base_image.copy()
        # rotate the image, based on the angle of the vector
        self.image = pygame.transform.rotate(tmp, -degrees(self.__vel.polar360))

        # if the fish magically disappears from the screen, then recenter it
        if self.rect.centery < 0 or self.rect.centery > self.screen.get_height():
            self.rect.centery = self.screen.get_rect().centery

        # update position of fish.
        self.rect.centerx += self.__vel.x
        self.rect.centery += self.__vel.y

    # fish.angle would give the angle of the fish correlated to the x-axis
    @property
    def angle(self):
        return self.__vel.polar360

    # return pos of fish
    @property
    def pos(self):
        return self.rect.center

    # return vel of fish
    @property
    def vel(self):
        return self.__vel
