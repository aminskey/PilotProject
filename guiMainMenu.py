import random
import pygame

from pygame.locals import *
from misc import Bubble
from variables import *
from vector import Vector
from text import Text

def mainMenu(screen):
    titleFont = pygame.font.Font("./assets/fonts/pixelart.ttf", 75)
    title = Text("Marine Life", titleFont, WHITE, shadow=True)
    title.rect.topleft = screen.get_rect().center

    bubbleGrp.empty()
    backBub.empty()
    frontBub.empty()
    for i in range(25):
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
        screen.blit(title.image, title.rect)
        frontBub.draw(screen)

        pygame.display.update()
        clock.tick(30)
