import random
import pygame

import guiGameOver
import guiInfoPage

from pygame.locals import *
from misc import Bubble
from variables import *
from vector import Vector
from text import Text
from oceanlife import Fish
from button import Button

buttons = pygame.sprite.Group()


def main(screen):


    titleFont = pygame.font.Font("./assets/fonts/pixelart.ttf", 75)
    pFont = pygame.font.Font("./assets/fonts/pixelart.ttf", 25)

    title = Text("Marine Life", titleFont, WHITE, shadow=OCEANSHADOW, pos2=(5, 4))
    title.rect.topright = screen.get_rect().midright

    bg = pygame.transform.scale(pygame.image.load("assets/backgrounds/MainMenu/reef.png"), screen.get_size())
    bg2 = pygame.transform.scale(pygame.image.load("assets/backgrounds/MainMenu/reef2.png"), (screen.get_width() - 100, screen.get_height()))
    shade = pygame.Surface(screen.get_size())
    shade.fill(OCEANBLUE)

    msg = Text("Start", pFont, OCEANSHADOW)
    start = Button((msg.image.get_width() * 3, msg.image.get_height() * 2))
    start.addText(msg, (start.image.get_width()//2, start.image.get_height()//2 - 4))

    info = Button(start.image.get_size())
    info.addText(Text("About Us", pFont, OCEANSHADOW), (info.image.get_width()//2, info.image.get_height()//2 - 4))
    info.fun = lambda:guiInfoPage.main()

    exitBtn = Button(start.image.get_size())
    exitBtn.addText(Text("Quit Game", pFont, OCEANSHADOW), (exitBtn.image.get_width() // 2, exitBtn.image.get_height() // 2 - 4))

    credBtn = Button(start.image.get_size())
    credBtn.addText(Text("InDev", pFont, OCEANSHADOW),
                    (exitBtn.image.get_width() // 2, exitBtn.image.get_height() // 2 - 4))

    start.rect.topright = title.rect.bottomright + Vector(-10, 40)
    info.rect.midtop = start.rect.midbottom + Vector(0, 5)
    credBtn.rect.midtop = info.rect.midbottom + Vector(0, 5)
    exitBtn.rect.bottomright = screen.get_rect().bottomright + Vector(-10, -10)

    buttons.add(start, info, credBtn, exitBtn)
    allSprites.add(start, title)

    shade.set_alpha(125)
    bg2.set_alpha(150)

    bubbleGrp.empty()
    backBub.empty()
    frontBub.empty()
    fishGrp.empty()

    global dTime

    pygame.mixer.music.load("assets/music/MainMenu/ocean-wave-ambient-boy-main-version-16232-09-09.mp3")

    for i in range(10):
        bub = Bubble(screen, (random.randint(0, screen.get_width()), random.randint(0, screen.get_height())), random.randint(25, 125)/100)

        if i < 3:
            bgFish = Fish("assets/fish/secretFish/fish2.png", random.randint(1, 5), screen,
                          (screen.get_width() // 2 + random.choice((-50, 50)), screen.get_height() // 2 + random.choice((-50, 50))), npc=True)
            fishGrp.add(bgFish)

        if not pygame.sprite.spritecollideany(bub, bubbleGrp):
            bubbleGrp.add(bub)
            if i % 3 == 0:
                bub.vel = Vector(0, -2)
                frontBub.add(bub)
            else:
                bub.image.set_alpha(200)
                backBub.add(bub)
        allSprites.add(bub, bgFish)

    pygame.mixer.music.play()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if start.activated:
                for i in allSprites.sprites():
                    i.kill()
                return
            elif info.activated:
                guiInfoPage.main(screen)
                info.deactivate()
                break
            elif credBtn.activated:
                guiGameOver.gameOver(screen)
                credBtn.deactivate()
                break
            elif exitBtn.activated:
                pygame.quit()
                exit()

        dTimeUpdate(clock)
        print(dTime)

        bubbleGrp.update()
        fishGrp.update(screen.get_rect())
        buttons.update()

        screen.fill(OCEANBLUE)
        screen.blit(bg2, (50, 0))
        backBub.draw(screen)
        fishGrp.draw(screen)
        screen.blit(bg, (0, 0))
        screen.blit(shade, (0, 0))
        screen.blit(title.image, title.rect)
        buttons.draw(screen)
        frontBub.draw(screen)

        pygame.display.update()
        clock.tick(30)

        print(clock.get_fps())
