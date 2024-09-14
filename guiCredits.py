import pygame

from variables import *
from time import time

def main(screen):

    pygame.mixer.music.load("assets/music/MainMenu/credits2.ogg")

    contents = parseMD("CREDITS.md", 0, screen, 1.5, textColor=WHITE, shadow=OCEANBLUE, pos2=(3, 2))
    shade = pygame.Surface(screen.get_size())
    shade.fill(BLACK)
    shade.set_alpha(6)

    index = 0
    startTime = time()
    l = pygame.sprite.Group()

    pygame.mixer.music.play()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        currTime = time()
        if (currTime - startTime) > 4:
            l.empty()
            if index > len(contents.sprites()) - 1:
                return
            else:
                for tmp in contents.sprites():
                    if tmp.rect.y == contents.sprites()[index].rect.y:
                        l.add(tmp)
                index += len(l)
            startTime = currTime

        screen.blit(shade, (0, 0))
        for txt in l.sprites():
            txt.rect.centery = screen.get_height()//2
            screen.blit(txt.image, txt.rect)

        pygame.display.update()
        clock.tick(30)