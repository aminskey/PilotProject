import os.path
from os import listdir
from oceanlife import Fish
from variables import RED
import random
from math import sqrt
import pygame

#test 2

class Flock:
  def __init__(self, amount, screen, boidR, bounds):
    #Antallet af fisk i flokken
    self.__amount = amount
    #Fiskene i en array
    self.__fishies = []
    #Radiussen i hvilken fisken bliver påvirket af andre fisk
    self.__boidR = boidR

    self.bounds = bounds
    #Fiskene bliver genereret
    for i in range(0, self.__amount + 1):
      # self.__fishies.append(Fish(random.random()*600, random.random()*500, random.random()*5,random.random()*5))
      fpath = f"assets/fish/{random.choice(listdir('assets/fish/'))}"
      if os.path.isfile(fpath):
          tmp = Fish(fpath, random.randrange(1, 5)/10, screen,(random.randint(bounds.topleft[0], bounds.topright[0]), random.randint(bounds.topright[1], bounds.bottomright[1])))
          self.__fishies.append(tmp)

  @property
  def fish(self):
    return self.__fishies

  # Alle fisk tegnes
  def drawOnImage(self):
    for fish in self.__fishies:
      fish.draw()
  # Alle fisk opdateres
  def update(self):
    for fish in self.__fishies:
      fish.update(self.bounds)
  def updateBoid(self, screen):
    #opdaterer alle fisk i relation til de andre
    for fish in self.__fishies:
      #finder alle fisks naboer indenfor radiussen boidR
      neighbours = []
      for neighbour in self.__fishies:
        if(sqrt((neighbour.rect.centerx-fish.rect.centerx)**2+(neighbour.rect.centery-fish.rect.centery)**2) <= self.__boidR):
          neighbours.append(neighbour)
          pygame.draw.line(screen, RED, (fish.rect.centerx, fish.rect.centery), (neighbour.rect.centerx, neighbour.rect.centery), 5)
          # print("found pair")
