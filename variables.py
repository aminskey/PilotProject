import pygame

from math import sqrt

FPS = 60
stdFPS = 45

dTime = stdFPS/FPS

GREEN = (0, 0, 255)
BROWN = (139, 69, 19)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
OCEANBLUE = (30, 150, 230)
OCEANSHADOW = (23, 67, 117)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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