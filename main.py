import os.path
import random
import pygame

from pygame.locals import *
from os import listdir
from oceanlife import Fish
from variables import *
from guiMainMenu import mainMenu
from simpleImage import SimpleImage, Water

pygame.init()

screen = pygame.display.set_mode((1200, 800), SCALED | FULLSCREEN)
pygame.display.set_caption("Marine Life")


def main():
    pygame.mixer.music.load("assets/music/InGame/campfire-sulyya-main-version-27140-04-01.mp3")
    bg = SimpleImage("assets/backgrounds/InGame/Himmel.png", screen.get_size())
    bg.rect.topleft = (0, 0)

    bottom = SimpleImage("assets/backgrounds/InGame/Havbund.png")
    bottom.image = pygame.transform.scale_by(bottom.image, screen.get_width()/bottom.image.get_width())
    bottom.rect = bottom.image.get_rect()
    bottom.rect.midbottom = screen.get_rect().midbottom

    water = Water()
    water.image = pygame.transform.scale_by(water.image, screen.get_width()/water.image.get_width())
    water.rect = water.image.get_rect()
    water.rect.midbottom = bottom.rect.midtop

    global dTime

    for i in range(10):
        fpath = f"assets/fish/{random.choice(listdir('assets/fish/'))}"
        if os.path.isfile(fpath):
            tmp = Fish(fpath, random.randrange(1, 5)/10, water.image,(random.randint(0, water.image.get_width()),random.randint(0, water.image.get_height())))
            tmp.add(fishGrp)


    running = True
    pygame.mixer.music.play(0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                running = False
                break

        dTimeUpdate(clock)
        fishGrp.update()
        bubbleGrp.update()
        water.update(bottom.rect.midtop)

        bg.draw(screen)
        fishGrp.draw(water.image)
        water.draw(screen)
        backBub.draw(screen)
        frontBub.draw(screen)
        bottom.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

        print(clock.get_fps())

    pygame.quit()

if __name__ == "__main__":
    mainMenu(screen)
    print(os.getcwd())
    main()
