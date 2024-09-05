import os.path
import random
import pygame

from pygame.locals import *
from os import listdir
from oceanlife import Fish
from variables import *
from guiMainMenu import mainMenu

pygame.init()

screen = pygame.display.set_mode((1200, 800), SCALED | FULLSCREEN)
pygame.display.set_caption("Marine14")


def main():
    for i in range(10):
        fpath = f"assets/fish/{random.choice(listdir('assets/fish/'))}"
        if os.path.isfile(fpath):
            tmp = Fish(fpath, random.randrange(1, 5)/10, screen,(random.randint(0, screen.get_width()),random.randint(0, screen.get_height())))
            tmp.add(fishGrp)

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
    mainMenu(screen)
    print(os.getcwd())
    main()
