import random
import pygame

from pygame.locals import *
from os import listdir
from oceanlife import Fish
from misc import Bubble
from variables import *

screen = pygame.display.set_mode((1200, 800), SCALED | FULLSCREEN)
pygame.display.set_caption("Fish - Testing Vectors")

clock = pygame.time.Clock()

fishGrp = pygame.sprite.Group()
bubbleGrp = pygame.sprite.Group()
frontBub = pygame.sprite.Group()
backBub = pygame.sprite.Group()

def main():
    for i in range(10):
        f = random.choice(listdir("assets/fish/"))
        tmp = Fish(f"assets/fish/{f}", random.randrange(1, 5)/10, screen,(random.randint(0, screen.get_width()),random.randint(0, screen.get_height())))
        bub = Bubble(screen, (random.randint(0, screen.get_width()), random.randint(0, screen.get_height())), random.randint(25, 125)/100)
        if not pygame.sprite.spritecollideany(bub, bubbleGrp):
            bub.add(bubbleGrp)
            if i % 3 == 0:
                frontBub.add(bub)
            else:
                bub.image.set_alpha(200)
                backBub.add(bub)

        tmp.add(fishGrp)

    bg = pygame.Surface(screen.get_size())
    bg.fill(BLUE)
    bg.set_alpha(150)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                running = False
                break

        fishGrp.update()
        bubbleGrp.update()

        screen.blit(bg, (0, 0))
        backBub.draw(screen)
        fishGrp.draw(screen)
        frontBub.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

        print(clock.get_fps())

    pygame.quit()

if __name__ == "__main__":
    main()
