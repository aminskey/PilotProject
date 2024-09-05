import os.path
from os import listdir
from oceanlife import Fish
import random
from math import sqrt

#test 2

class Flock:
  def __init__(self, amount, screen, boidR):
    #Antallet af fisk i flokken
    self.__amount = amount
    #Fiskene i en array
    self.__fishies = []
    #Radiussen i hvilken fisken bliver påvirket af andre fisk
    self.__boidR = boidR
    #Fiskene bliver genereret
    for i in range(0, self.__amount + 1):
      # self.__fishies.append(Fish(random.random()*600, random.random()*500, random.random()*5,random.random()*5))
      fpath = f"assets/fish/{random.choice(listdir('assets/fish/'))}"
      if os.path.isfile(fpath):
          tmp = Fish(fpath, random.randrange(1, 5)/10, screen,(random.randint(0, screen.get_width()),random.randint(0, screen.get_height())))
          self.__fishies.append(tmp)
  #Alle fisk tegnes
  def draw(self):
    for fish in self.__fishies:
      fish.draw()
  #Alle fisk opdateres
  def update(self):
    for fish in self.__fishies:
      fish.update()
  def updateBoid(self):
    #opdaterer alle fisk i relation til de andre
    for fish in self.__fishies:
      #finder alle fisks naboer indenfor radiussen boidR
      neighbours = []
      for neighbour in self.fishies:
        if(sqrt((neighbour.rect.centerx-fish.rect.centerx)**2+(neighbour.rect.centery-fish.rect.centery)**2) <=50):
          neighbours.append(neighbour)

      
      
