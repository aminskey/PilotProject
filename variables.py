import pygame
import text

from math import sqrt
from vector import Vector

FPS = 60
stdFPS = 45

dTime = stdFPS/FPS

GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
OCEANBLUE = (30, 150, 230)
OCEANSHADOW = (23, 67, 117)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()

fishGrp = pygame.sprite.Group()
bubbleGrp = pygame.sprite.Group()
frontBub = pygame.sprite.Group()
backBub = pygame.sprite.Group()
allSprites = pygame.sprite.Group()
trashGrp = pygame.sprite.Group()

def isInRange(x, offset, min, max):
    return (x - offset) > min and (x + offset) < max

def isInBounds(pos, offset, minPoint, maxPoint):
    return isInRange(pos[0], offset, minPoint[0], maxPoint[0]) and isInRange(pos[1], offset, minPoint[1], maxPoint[1])

def dTimeUpdate(clock):
    global dTime
    try:
        dTime = stdFPS/clock.get_fps()
    except:
        if dTime <= 0:
            dTime = stdFPS/FPS

def addVec(rect, vec):
    rect.x += vec.x
    rect.y += vec.y
def subVec(rect, vec):
    addVec(rect, -vec)

def dist(p1, p2):
    return sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def secToTime(s):
    try:
        min=s//60
    except:
        min = 0

    sec = s%60

    return f"{int(min)}:{int(sec)}"

def parseMD(file, margin, screen, sizeMult=1, **kwargs):
    tmpGrp = pygame.sprite.Group()

    basicFont = pygame.font.Font("assets/fonts/pixelart.ttf", int(25*sizeMult))
    codeFont = pygame.font.Font("assets/fonts/Flexi_IBM_VGA_True.ttf", int(25*sizeMult))
    titleFont = pygame.font.Font("assets/fonts/pixelart.ttf", int(75*sizeMult))
    h2Font = pygame.font.Font("assets/fonts/pixelart.ttf", int(50*sizeMult))
    h3Font = pygame.font.Font("assets/fonts/pixelart.ttf", int(30*sizeMult))
    h4Font = pygame.font.Font("assets/fonts/pixelart.ttf", int(27*sizeMult))

    with open(file, "rb") as f:
        buff = f.read().decode().split('\n')
        buff = " ".join(buff).split(' ')
        f.close()

    print(buff)

    pos = Vector(margin, 0)
    script = basicFont
    for word in buff:
        if word.strip() == "<br>":
            pos.y += script.size(word)[1]
            pos.x = margin
            continue

        if word == "":
            word = " "

        if "```" in word:
            if script is not codeFont:
                script = codeFont
                margin = 25
            elif script is codeFont:
                script = basicFont
                margin = 10
            pos.y += 10
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

        tmp = text.Text(word.strip()+" ", script, **kwargs)
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