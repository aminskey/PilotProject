import guiGameOver
import guiMainMenu
import random
import json
import time
import pygame

from pygame.locals import *
from swarm import Flock
from oceanlife import Garbage, Algea
from text import Text
from variables import *
from simpleImage import SimpleImage, Water

pygame.init()

screen = pygame.display.set_mode((1200, 800), SCALED | FULLSCREEN)
pygame.display.set_caption("Marine Life")


def main():

    fishGrp.empty()
    trashGrp.empty()

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
    miniFont = pygame.font.Font("assets/fonts/pixelart.ttf", 25)

    global dTime


    border = Rect(water.rect.topleft, bottom.rect.topright)

    fish = Flock(12, screen, 300, border)
    for f in fish.fishies:
        f.add(fishGrp)


    running = True
    count = 0

    startTime = time.time()

    with open("assets/trash/json/trash.json") as f:
        dat = json.load(f)
        f.close()

    pygame.mixer.music.play(-1)
    x = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        currTime = time.time()

        fishColor = WHITE
        shadow = OCEANBLUE
        if fish.length > fish.maxAmount:
            fishColor = GREEN
        elif fish.maxAmount*0.5 < fish.length < fish.maxAmount*0.75:
            fishColor = YELLOW
            shadow = (155, 155, 0)
        elif fish.length <= fish.maxAmount*0.5:
            fishColor = RED
            shadow = OCEANSHADOW

        t = currTime - startTime
        sec = int(t%60)
        fish_indicator = Text(f"Number of fish: {fish.length}/{fish.maxAmount}", basicFont, fishColor, (screen.get_width()//2, screen.get_height() * 1/10), shadow)
        time_indicator = Text(f"Time: {int(t/60):02}:{sec:02}", miniFont, WHITE, shadow=OCEANBLUE)
        time_indicator.rect.topleft = (0, 0)

        border.update(water.rect.topleft, (bottom.rect.topright[0], bottom.rect.y - water.rect.y))
        border.y = water.rect.y

        if count % (FPS*2 - int(x)) == 0:
            for i in range(int(x)):
                obj = random.choice(dat["list"])
                tmp = Garbage(None, scale=0.5, image=obj["image"])
                tmp.rect.centery = screen.get_height() // 2
                tmp.rect.centerx = random.choice([0, screen.get_width()])

                tmp.vel.x = random.randint(1, 3)
                tmp.vel.x *= -1 if tmp.rect.centerx >= screen.get_width() else 1
                tmp.acc.y = obj["acc_y"]
                tmp.vel.y = random.randint(-3, 3)
                print(tmp.acc.y)

                tmp.add(trashGrp)

                if random.randint(0, 1+x//4) == 0:
                    food = Algea(1, screen)
                    food.rect.centerx = random.choice([0, screen.get_width()])
                    food.rect.centery = screen.get_height() // 2

                    food.vel.y = random.randint(-3, 3)
                    food.vel.x = random.randint(1, 3)
                    food.vel.x *= -1 if tmp.rect.centerx >= screen.get_width() else 1

                    trashGrp.add(food)
            x += 1

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
        screen.blit(time_indicator.image, time_indicator.rect)

        pygame.display.update()
        clock.tick(FPS)

        if fish.length <= 0:
            guiGameOver.gameOver(screen)
            guiMainMenu.main(screen)
            return

        print(clock.get_fps())
        count += 1

    pygame.quit()

if __name__ == "__main__":
    guiMainMenu.main(screen)
