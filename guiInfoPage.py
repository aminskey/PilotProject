import pygame
import random

from variables import *
from misc import Bubble

def main(screen):

    for b in bubbleGrp.sprites():
        b.kill()

    overlay = pygame.transform.scale(pygame.image.load("assets/backgrounds/MainMenu/unused.png"), screen.get_size())
    bg2 = pygame.transform.scale(pygame.image.load("assets/backgrounds/MainMenu/reef2.png"),
                                 (screen.get_width() - 100, screen.get_height()))
    shade = pygame.Surface(screen.get_size())
    shade.fill(BLACK)

    shade.set_alpha(200)
    bg2.set_alpha(100)

    for i in range(10):
        bub = Bubble(screen, (random.randint(0, screen.get_width()), random.randint(0, screen.get_height())), random.randint(0, 125)/100)
        bubbleGrp.add(bub)
        if i % 2 == 0:
            frontBub.add(bub)
        else:
            backBub.add(bub)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        bubbleGrp.update()

        screen.fill(OCEANBLUE)
        backBub.draw(screen)
        screen.blit(bg2, (50, 0))
        screen.blit(overlay, (0, 0))
        screen.blit(shade, (0, 0))
        frontBub.draw(screen)

        pygame.display.update()
        clock.tick(FPS)