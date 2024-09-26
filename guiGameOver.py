import pygame

from text import Text
from pygame.locals import *
from variables import WHITE, BLACK, addVec, clock, OCEANSHADOW
from vector import Vector
from time import time

def gameOver(screen):
    pygame.mixer.music.load("assets/music/InGame/gameOver.ogg")

    font = pygame.font.Font("assets/fonts/pixelart.ttf", 65)
    pfont = pygame.font.Font("assets/fonts/pixelart.ttf", 25)

    title = Text("Game Over", font, WHITE, shadow=OCEANSHADOW)
    subtitle = Text("Press anything to continue..", pfont, WHITE, shadow=OCEANSHADOW)
    bg = screen.copy()
    shade = pygame.Surface(screen.get_size())
    shade.fill(BLACK)
    bg.set_alpha(50)
    shade.set_alpha(50)



    title.rect.midbottom = screen.get_rect().midtop
    vel = Vector(0, 2)
    acc = Vector(0, 1)

    running = True
    pygame.mixer.music.play()
    startTime = time()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                break
            if event.type == pygame.KEYDOWN:
                if acc.length <= 0 and event.key == pygame.K_RETURN:
                    return

        vel += acc
        if title.rect.centery >= screen.get_height()//2:
            vel *= -0.88
            if vel.length <= 0.4:
                vel = Vector(0, 0)
                acc = Vector(0, 0)

        addVec(title.rect, vel)
        subtitle.rect.midtop = title.rect.midbottom

        screen.blit(bg, (0, 0))
        screen.blit(shade, (0, 0))
        screen.blit(title.image, title.rect)
        currTime = time()
        if (currTime - startTime) > 7:
            screen.blit(subtitle.image, subtitle.rect)

        pygame.display.update()
        clock.tick(30)
