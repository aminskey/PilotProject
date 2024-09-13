import os.path
import os

import guiGameOver
import guiMainMenu
import random
import json
import pygame

from pygame.locals import *
from swarm import Flock
from oceanlife import Garbage
from text import Text
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

    basicFont = pygame.font.Font("assets/fonts/pixelart.ttf", 35)

    global dTime


    border = Rect(water.rect.topleft, bottom.rect.topright)

    fish = Flock(5, screen, 300, border)
    for f in fish.fishies:
        f.add(fishGrp)

    running = True
    count = 0

    with open("assets/trash/json/trash.json") as f:
        dat = json.load(f)
        f.close()

    pygame.mixer.music.play(0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        fishColor = WHITE
        shadow = OCEANBLUE
        if fish.length > fish.maxAmount:
            fishColor = GREEN
        elif fish.maxAmount*0.5 < fish.length < fish.maxAmount*0.75:
            fishColor = YELLOW
        elif fish.length <= fish.maxAmount*0.5:
            fishColor = RED
            shadow = OCEANSHADOW

        fish_indicator = Text(f"Number of fish: {fish.length}/{fish.maxAmount}", basicFont, fishColor, (screen.get_width()//2, screen.get_height() * 1/10), shadow)

        border.update(water.rect.topleft, (bottom.rect.topright[0], bottom.rect.y - water.rect.y))
        border.y = water.rect.y

        if count % (FPS*25) == 0:
            for i in range(10):
                obj = random.choice(dat["list"])
                tmp = Garbage(None, scale=0.5, image=obj["image"])
                tmp.rect.centery = screen.get_height() // 2
                tmp.rect.centerx = screen.get_width()

                tmp.vel.x = -3
                tmp.acc.y = int(obj["acc_y"])

                tmp.add(trashGrp)

        if fish.length <= 0:
            guiGameOver.gameOver(screen)
            guiMainMenu.main(screen)
            return

        dTimeUpdate(clock)
        fish.updateBoid()
        fish.react(pygame.mouse.get_pressed()[0], pygame.mouse.get_pressed()[2])
        fish.update()
        trashGrp.update(border)
        bubbleGrp.update()
        water.update(bottom.rect.midtop)
        bg.draw(screen)

        # Ask before pushing
        water.draw(screen)
        trashGrp.draw(screen)
        fish.drawOnImage()
        bottom.draw(screen)
        screen.blit(water.overlay, water.rect)
        screen.blit(fish_indicator.image, fish_indicator.rect)

        pygame.display.update()
        clock.tick(FPS)

        print(clock.get_fps())
        count += 1

    pygame.quit()

if __name__ == "__main__":
    guiMainMenu.main(screen)
    print(os.getcwd())
    main()
