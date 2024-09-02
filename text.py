from pygame.locals import *
from misc import Bubble
from variables import *
from vector import Vector

class Text(pygame.sprite.Sprite):
    def __init__(self, msg, script, textColor, pos=(0, 0), shadow=False):
        super().__init__()

        img = script.render(msg, None, textColor)
        if not shadow:
            self.image = img.copy()
        else:
            self.image = pygame.Surface((img.get_width()*1.02, img.get_height()*1.02)).convert_alpha()
            self.image.fill((23, 16, 1))
            self.image.set_colorkey((23, 16, 1))
            shadowText = Text(msg, script, BLACK)
            shadowText.rect.topleft = (3, 2)

            self.image.blit(shadowText.image, shadowText.rect)
            self.image.blit(img, (0, 0))

        self.rect = self.image.get_rect()
        self.color = textColor
        self.rect.center = pos
        self.alphaValue = 255
        self.deltaA = -20
    def blink(self):
        self.alphaValue += self.deltaA
        if not isInBounds(self.alphaValue, 255, 0):
            self.deltaA *= -1
        self.image.set_alpha(self.alphaValue)