import random
import pygame

from vector import Vector
from pygame.locals import *
from math import degrees
from os import listdir

FPS = 60
stdFPS = 45

dTime = stdFPS/FPS

GREEN = (0, 0, 255)
BROWN = (139, 69, 19)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

fishGrp = pygame.sprite.Group()
bubbleGrp = pygame.sprite.Group()
frontBub = pygame.sprite.Group()
backBub = pygame.sprite.Group()

screen = pygame.display.set_mode((1200, 800), SCALED | FULLSCREEN)
pygame.display.set_caption("Fish - Testing Vectors")

clock = pygame.time.Clock()

class Bubble(pygame.sprite.Sprite):
    def __init__(self, pos, sizeF=1):
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load("assets/misc/bubble.png"), sizeF)
        self.rect = self.image.get_rect()

        self.rect.topleft = pos
    def update(self, win=screen):
        if self.rect.midbottom[1] > 0:
            self.rect.y -= 1
        else:
            self.rect.y = win.get_height()
            self.rect.x = random.randint(0, win.get_width())

class Fish(pygame.sprite.Sprite):
    def __init__(self, image, sizeF, pos, vx=3, vy=2):
        super().__init__()
        self.base_image = pygame.transform.scale_by(pygame.image.load(image), sizeF)
        self.image = self.base_image.copy()

        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        self.__vel = Vector(vx * dTime, vy * dTime)

    def update(self):
        if not isInRange(self.rect.centerx, self.base_image.get_width(), 0, screen.get_width()):
            self.__vel = Vector(-self.__vel.x, self.__vel.y * random.randint(-3, 3) / 5)
        if not isInRange(self.rect.centery, self.base_image.get_height(), 0, screen.get_height()):
            self.__vel = Vector(self.__vel.x, -self.__vel.y)

        if self.__vel.x < 0:
            tmp = pygame.transform.flip(self.base_image, False, True)
        else:
            tmp = self.base_image.copy()
        self.image = pygame.transform.rotate(tmp, -degrees(self.__vel.polar360))

        if self.rect.centery < 0 or self.rect.centery > screen.get_height():
            self.rect.centery = screen.get_rect().centery

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

def isInRange(x, offset, min, max):
    return (x - offset) > min and (x + offset) < max


def isInBounds(pos, offset, minPoint, maxPoint):
    return isInRange(pos[0], offset, minPoint[0], maxPoint[0]) and isInRange(pos[1], offset, minPoint[1], maxPoint[1])


def main():
    for i in range(10):
        f = random.choice(listdir("assets/fish/"))
        tmp = Fish(f"assets/fish/{f}",
                   random.randrange(1, 5)/10,
                   (random.randint(0, screen.get_width()),
                    random.randint(0, screen.get_height())),
                   random.randint(-1, 2),
                   random.randint(0, 2)
                   )
        bub = Bubble(
            (
                random.randint(0, screen.get_width()),
                random.randint(0, screen.get_height())
            ),
            random.randint(25, 125)/100
        )
        tmp.add(fishGrp)
        if not pygame.sprite.spritecollideany(bub, bubbleGrp):
            bub.add(bubbleGrp)
            if i % 3 == 0:
                frontBub.add(bub)
            else:
                bub.image.set_alpha(200)
                backBub.add(bub)

    bg = pygame.Surface(screen.get_size())
    bg.fill(BLUE)
    bg.set_alpha(150)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                running = False
                break

        fishGrp.update()
        bubbleGrp.update()

        screen.blit(bg, (0, 0))
        backBub.draw(screen)
        fishGrp.draw(screen)
        frontBub.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

        print(clock.get_fps())

    pygame.quit()

if __name__ == "__main__":
    main()
