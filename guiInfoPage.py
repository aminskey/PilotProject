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

    basicFont = pygame.font.Font("assets/fonts/pixelart.ttf", 25)
    scrollVec = Vector(0, 0)

    content = parseMD("README.md", basicFont, screen)

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
                    scrollVec.y = -1
                    break
                if event.key == pygame.K_DOWN:
                    scrollVec.y = 1
                    break
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

def parseMD(file, script, screen):
    tmpGrp = pygame.sprite.Group()
    with open(file, "rb") as f:
        buff = f.readlines()
        f.close()

    i = 0
    for line in buff:
        tmp = line.decode().strip("\r\n")
        set = tmp.split(" ")
        prevWord = ""
        j = 0
        for word in set:
            if (j+1)*12 > screen.get_width()*3//4:
                j = 0
                i += 1
            tmp = Text(word, script, WHITE)
            tmp.rect.topleft = (script.size(prevWord)[0], (1+i)*25)
            tmpGrp.add(tmp)

            prevWord = word
            j+=1
        i += 1

    return tmpGrp