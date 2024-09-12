import pygame
import random

from math import degrees, sin
from vector import Vector
from variables import *
from simpleImage import SimpleImage
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
        self.flock = None

        # assigning velocity vector
        if v[0] != 0 and v[1] != 0:
            self.__vel = Vector(v[0] * dTime, v[1] * dTime)
        else:
            self.__vel = Vector(random.choice((-2, 2)) * dTime, random.choice((-1, 1)) * dTime)
        self.loop = loop

    # Checking for border collision and handling it
    def borderCheck(self, bounds):
        if not isInRange(self.rect.centerx, self.base_image.get_width(), bounds.x, bounds.topright[0]):
            self.__vel.x += 1 - (self.rect.centerx / 300)
            self.rect.centerx += self.__vel.x * 2
        if not isInRange(self.rect.centery, self.base_image.get_height(), bounds.y, bounds.bottomright[1]):
            self.__vel.y += 1 - (self.rect.centery / 300)
            self.rect.centery += self.__vel.y * 2

    # Update function to be run every frame.
    def update(self, bounds):
        # if not loop initiated then handle border collision
        if not self.loop:
            self.borderCheck(bounds)
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
        #self.rect.centerx += self.__vel.x * dTime
        #self.rect.centery += self.__vel.y * dTime
        addVec(self.rect, self.__vel * dTime)
    def draw(self):
        # draws fish to screen
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
    # fish.angle would give the angle of the fish correlated to the x-axis
    @property
    def angle(self):
        return self.__vel.polar360

    # return pos of fish
    @property
    def pos(self):
        return Vector(self.rect.x, self.rect.y)

    # return vel of fish
    @property
    def vel(self):
        return self.__vel

class Garbage(SimpleImage):
    def __init__(self, type, scale, image=None, canKill=True):
        if isinstance(image, str):
            super().__init__(image)
        else:
            super().__init__(f"assets/trash/{type}.png")
        self.base_image = pygame.transform.scale_by(self.base_image, scale)
        self.image = self.base_image.copy()
        self.rect = self.image.get_rect()
        self.canKill = canKill

        self.__vel = Vector(random.randint(-10,10)/20, -random.randint(1, 5)/10)

    def seperation(self, grp: pygame.sprite.Group,  rad: int, factor: float):
        sep_vector = Vector(0, 0)
        count = 0

        for t in grp.sprites():
            if t != self:
                if 0 < (gap := dist(t.rect, self.rect)) < rad:
                    tmp = self.pos - t.pos
                    tmp /= tmp.length
                    tmp /= gap
                    sep_vector += tmp
                    count += 1

        if count > 0:
            sep_vector /= count
        return sep_vector * factor

    def update(self, bounds):
        if not isInRange(self.rect.centery, 0, bounds.y, bounds.midbottom[1]):
            if self.__vel.y < 1:
                self.__vel.y += 0.25
        else:
            if self.__vel.y > -1:
                self.__vel.y -= 0.25

        if not isInRange(self.rect.centerx, -self.image.get_width(), bounds.x, bounds.topright[0]):
            self.kill()

        if self.canKill:
            if fish := pygame.sprite.spritecollideany(self, fishGrp):
                fish.kill()
                fish.flock.fishies.remove(fish)
                tmp = Garbage(None, 0.125, "assets/misc/Fisk_Skelet.png", canKill=False)
                tmp.__vel = fish.vel
                tmp.__vel.y = -1
                tmp.rect.center = fish.rect.center
                trashGrp.add(tmp)
                #self.kill()

        self.__vel += self.seperation(trashGrp, 100, 1)
        addVec(self.rect, self.__vel)