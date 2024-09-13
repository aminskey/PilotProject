import pygame
import random

from math import degrees
from vector import Vector
from variables import *
from pygame.locals import *

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
        
        #strength of border avoidance

        self.__p = 4

        #distance at which borders are detected

        self.__vision = 100

        self.__maxSpeed = 6

        # assigning velocity vector
        if v[0] != 0 and v[1] != 0:
            self.__vel = Vector(v[0] * dTime, v[1] * dTime)
        else:
            self.__vel = Vector(random.choice((-2, 2)) * dTime, random.choice((-1, 1)) * dTime)
        self.loop = loop

    # Checking for border collision and handling it
    # def borderCheck(self, bounds):
    #     if not isInRange(self.rect.centerx, self.base_image.get_width(), bounds.x, bounds.topright[0]):
    #         self.__vel = Vector(-self.__vel.x + (1 - (self.rect.centerx/self.__vision))*self.__p, self.__vel.y * random.randint(-3, 3) / 5)
    #         self.rect.centerx += self.__vel.x * 2
    #     if not isInRange(self.rect.centery, self.base_image.get_height(), bounds.y, bounds.bottomright[1]):
    #         if(self.rect.centery < self.screen.get_height()/2):
    #             self.__vel = Vector(self.__vel.x, self.__vel.y - (1 - (self.rect.centery-bounds.y/self.__vision))*self.__p)
    #         elif(self.rect.centery > self.screen.get_height()/2):
    #             self.__vel = Vector(self.__vel.x, self.__vel.y + (1 - (self.rect.centery-bounds.bottomright[1]/self.__vision))*self.__p)
    #         self.rect.centery += self.__vel.y * 2
    # def borderCheck2(self, bounds):
    def screenConfinementX2(self, bounds):
        if ((self.rect.centerx < self.__vision + bounds.x + 100)):
            return Vector(self.__vel.x  + (1 - ((self.rect.centerx-100)/self.__vision))*self.__p, self.__vel.y)
        elif (self.rect.centerx > bounds.bottomright[0]-self.__vision):
            return Vector(self.__vel.x - (1 - ((self.rect.centerx-bounds.bottomright[0])/self.__vision))*self.__p, self.__vel.y)
        else:
            return self.__vel
    def screenConfinementY2(self, bounds):
        if ((self.rect.centery < self.__vision + bounds.y)):
            return Vector(self.__vel.x, self.__vel.y - (1 - (self.rect.centery/self.__vision))*self.__p)
        elif (self.rect.centery > bounds.bottomright[1]-self.__vision):
            return Vector(self.__vel.x, self.__vel.y - (1 - ((self.rect.centery-bounds.bottomright[1])/self.__vision))*self.__p)
        else:
            return self.__vel
    # Update function to be run every frame.
    def update(self, bounds):
        # if not loop initiated then handle border collision
        if not self.loop:
            self.__vel.x = self.screenConfinementX2(bounds).x
            self.__vel.y = self.screenConfinementY2(bounds).y
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
            # If not, then use base image
            # We do not want moonwalking fish
            tmp = self.base_image.copy()
        # rotate the image, based on the angle of the vector
        self.image = pygame.transform.rotate(tmp, -degrees(self.__vel.polar360))

        # if the fish magically disappears from the screen, then recenter it
        if not isInBounds(self.rect.center, 0, (0, 0), self.screen.get_size()):
            self.rect.center = self.screen.get_rect().center

        # update position of fish.
        
        self.__vel = self.__vel/self.__vel.getLength()*self.__maxSpeed
        self.rect.centerx += self.__vel.x
        self.rect.centery += self.__vel.y
    def draw(self):
        # draws fish to screen
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
    #make the fish react to mouse
    def attract(self):
        self.__vel = self.__vel + ((Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])) - Vector(self.rect.centerx, self.rect.centery))*0.004
    def avoid(self):
        self.__vel = self.__vel + (Vector(self.rect.centerx, self.rect.centery) - (Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])))*0.03
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
    #set vel of fish
    @vel.setter
    def vel(self, vel):
        self.__vel = vel
