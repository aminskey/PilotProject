import pygame, random

class Bubble(pygame.sprite.Sprite):
    def __init__(self, screen, pos, sizeF=1):
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load("assets/misc/bubble.png"), sizeF)
        self.rect = self.image.get_rect()
        self.screen = screen

        self.rect.topleft = pos
    def update(self):
        if self.rect.midbottom[1] > 0:
            self.rect.y -= 1
        else:
            self.rect.y = self.screen.get_height()
            self.rect.x = random.randint(0, self.screen.get_width())

