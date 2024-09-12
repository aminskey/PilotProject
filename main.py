import os.path
import guiMainMenu
import random
import pygame

from pygame.locals import *
from os import listdir
from oceanlife import Fish
from swarm import Flock
from variables import *
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

    fish = Flock(20, screen, 300, water.rect)

    for f in fish.fish:
        f.add(fishGrp)

    running = True
    pygame.mixer.music.play(0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        dTimeUpdate(clock)
        fish.update()
        bubbleGrp.update()
        water.update(bottom.rect.midtop)
        bg.draw(screen)
        # Ask before pushing
        water.draw(screen)
        fish.drawOnImage()
        bottom.draw(screen)
        screen.blit(water.overlay, water.rect)

        pygame.display.update()
        clock.tick(FPS)

        print(clock.get_fps())

    pygame.quit()

if __name__ == "__main__":
    guiMainMenu.main(screen)
    print(os.getcwd())
    main()
