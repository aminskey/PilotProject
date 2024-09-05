import os.path
from os import listdir
from oceanlife import Fish
import random

#test 2

class Flock:
  def __init__(self, amount, screen):
    self.__amount = amount
    self.__fishies = []
    for i in range(0, self.__amount + 1):
      # self.__fishies.append(Fish(random.random()*600, random.random()*500, random.random()*5,random.random()*5))
      fpath = f"assets/fish/{random.choice(listdir('assets/fish/'))}"
      if os.path.isfile(fpath):
          tmp = Fish(fpath, random.randrange(1, 5)/10, screen,(random.randint(0, screen.get_width()),random.randint(0, screen.get_height())))
          self.__fishies.append(tmp)
  def draw(self, screen):
    for fish in self.__fishies:
      fish.render(screen)
  def update(self):
    for fish in self.__fishies:
      fish.update()
  def react(self, leftClick, rightClick):
    for fish in self.__fishies:
      if(leftClick == True):
        fish.attract()
      if(rightClick == True):
        fish.avoid()
