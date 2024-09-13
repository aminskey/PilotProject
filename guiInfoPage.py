import pygame
import random

from variables import *
from misc import Bubble
from text import Text
from vector import Vector

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

    scrollVec = Vector(0, 0)

    content = parseMD("README.md", 10, screen, textColor=(178, 178, 178), shadow=BLACK)

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    scrollVec.y = 10
                    break
                if event.key == pygame.K_DOWN:
                    scrollVec.y = -10
                    break
                if event.key == pygame.K_ESCAPE:
                    return
            elif event.type == pygame.KEYUP:
                scrollVec.y = 0
                break


        bubbleGrp.update()
        for sprite in content.sprites():
            sprite.rect.y += scrollVec.y

        screen.fill(OCEANBLUE)
        backBub.draw(screen)
        screen.blit(bg2, (50, 0))
        screen.blit(overlay, (0, 0))
        screen.blit(shade, (0, 0))
        content.draw(screen)
        frontBub.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

def parseMD(file, margin, screen, **kwargs):
    tmpGrp = pygame.sprite.Group()

    basicFont = pygame.font.Font("assets/fonts/pixelart.ttf", 25)
    codeFont = pygame.font.Font("assets/fonts/Flexi_IBM_VGA_True.ttf", 25)
    titleFont = pygame.font.Font("assets/fonts/pixelart.ttf", 75)
    h2Font = pygame.font.Font("assets/fonts/pixelart.ttf", 50)
    h3Font = pygame.font.Font("assets/fonts/pixelart.ttf", 30)
    h4Font = pygame.font.Font("assets/fonts/pixelart.ttf", 27)

    with open(file, "rb") as f:
        buff = f.read().decode().split('\n')
        buff = " ".join(buff).split(' ')
        f.close()

    print(buff)

    pos = Vector(margin, 0)
    script = basicFont
    for word in buff:
        if "```" in word:
            if script is not codeFont:
                script = codeFont
                margin = 25

            elif script is codeFont:
                script = basicFont
                margin = 10
            pos = Vector(margin, pos.y)
            continue
        elif "#" in word and script is not codeFont:
            script = titleFont
            if word.count("#") == 2:
                script = h2Font
            elif word.count("#") == 3:
                script = h3Font
                script.underline = True
            elif word.count("#") == 4:
                script = h4Font
            continue

        if word == "":
            word = " "

        tmp = Text(word.strip()+" ", script, **kwargs)
        tmp.rect.topleft = pos.tuple
        tmpGrp.add(tmp)

        # Prepping position for next word.

        if len(word) > 0:
            if word[-1] == '\r' or pos.x > screen.get_width() * 3//4:
                print(pos.y)
                pos.y += script.size(word)[1]
                pos.x = margin

                if script is not codeFont:
                    script = basicFont
                script.underline = False
            else:
                pos.x = tmpGrp.sprites()[-1].rect.topright[0]
                pos.y = tmpGrp.sprites()[-1].rect.topright[1]

    return tmpGrp