import random
import pygame

from pygame.locals import *
from misc import Bubble
from variables import *
from vector import Vector
from text import Text
from oceanlife import Fish

def mainMenu(screen):
    titleFont = pygame.font.Font("./assets/fonts/pixelart.ttf", 75)
    title = Text("Marine Life", titleFont, WHITE, shadow=OCEANSHADOW, pos2=(5, 4))
    title.rect.topleft = screen.get_rect().center

    bg = pygame.transform.scale(pygame.image.load("assets/backgrounds/MainMenu/reef.png"), screen.get_size())
    bg2 = pygame.transform.scale(pygame.image.load("assets/backgrounds/MainMenu/reef2.png"), (screen.get_width() - 100, screen.get_height()))
    shade = pygame.Surface(screen.get_size())
    shade.fill(OCEANBLUE)

    shade.set_alpha(125)
    bg2.set_alpha(150)

    bubbleGrp.empty()
    backBub.empty()
    frontBub.empty()
    fishGrp.empty()

    global dTime

    for i in range(15):
        bub = Bubble(screen, (random.randint(0, screen.get_width()), random.randint(0, screen.get_height())), random.randint(25, 125)/100)

        if i < 3:
            bgFish = Fish("assets/fish/secretFish/fish2.png", random.randint(1, 5), screen,
                          (screen.get_width() // 2 + random.choice((-50, 50)), screen.get_height() // 2 + random.choice((-50, 50))))
            #bgFish.base_image.set_alpha(200)
            fishGrp.add(bgFish)

        if not pygame.sprite.spritecollideany(bub, bubbleGrp):
            bubbleGrp.add(bub)
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

        try:
            dTime = stdFPS/clock.get_fps()
        except:
            dTime = stdFPS/FPS

        bubbleGrp.update()
        fishGrp.update()

        screen.fill(OCEANBLUE)
        screen.blit(bg2, (50, 0))
        backBub.draw(screen)
        fishGrp.draw(screen)
        screen.blit(bg, (0, 0))
        screen.blit(shade, (0, 0))
        frontBub.draw(screen)
        screen.blit(title.image, title.rect)

        pygame.display.update()
        clock.tick(30)

        print(clock.get_fps())
