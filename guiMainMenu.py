import random
import pygame

from pygame.locals import *
from misc import Bubble
from variables import *
from vector import Vector

def mainMenu(screen):
    for i in range(10):
        bub = Bubble(screen, (random.randint(0, screen.get_width()), random.randint(0, screen.get_height())), random.randint(25, 125)/100)
        if not pygame.sprite.spritecollideany(bub, bubbleGrp):
            bub.add(bubbleGrp)
            if i % 3 == 0:
                bub.vel = Vector(0, -2)
                frontBub.add(bub)
            else:
                bub.image.set_alpha(200)
                backBub.add(bub)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        bubbleGrp.update()

        screen.fill(OCEANBLUE)
        backBub.draw(screen)
        frontBub.draw(screen)

        pygame.display.update()
        clock.tick(30)
