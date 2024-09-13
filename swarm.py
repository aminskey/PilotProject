import os.path
from os import listdir
from oceanlife import Fish
from variables import RED
from variables import GREEN
from vector import *
import random
from math import sqrt
from math import cos
from math import sin
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
    for i in range(1, self.__amount):
      # self.__fishies.append(Fish(random.random()*600, random.random()*500, random.random()*5,random.random()*5))
      fpath = f"assets/fish/{random.choice(listdir('assets/fish/'))}"
      if os.path.isfile(fpath):
          tmp = Fish(fpath, random.randrange(1, 5)/10, screen,(random.randint(bounds.topleft[0], bounds.topright[0]), random.randint(bounds.topright[1], bounds.bottomright[1])))
          self.__fishies.append(tmp)
          tmp.flock = self

  @property
  def fishies(self):
    return self.__fishies

  @property
  def length(self):
    return len(self.__fishies)

  @property
  def maxAmount(self):
    return self.__amount

  # Alle fisk tegnes
  def drawOnImage(self):
    for fish in self.__fishies:
      fish.draw()
  # Alle fisk opdateres
  def update(self):
    for fish in self.__fishies:
      fish.update(self.bounds)
  def react(self, leftClick, rightClick):
    for fish in self.__fishies:
      fish.attract()
      if(rightClick == True):
        fish.avoid()
  def updateBoid(self):
    #opdaterer alle fisk i relation til de andre
    for fish in self.__fishies:
      #finder alle fisks naboer indenfor radiussen boidR
      neighbours = []
      for neighbour in self.__fishies:
        if(sqrt((neighbour.rect.centerx-fish.rect.centerx)**2+(neighbour.rect.centery-fish.rect.centery)**2) <= self.__boidR and fish != neighbour):
          neighbours.append(neighbour)
          # pygame.draw.line(screen, RED, (fish.rect.centerx, fish.rect.centery), (neighbour.rect.centerx, neighbour.rect.centery), 5)
          # pygame.draw.line(screen, GREEN, (fish.rect.centerx, fish.rect.centery), (fish.rect.centerx + 40*cos(fish.angle), fish.rect.centery + 40*sin(fish.angle)), 3)
        fish.vel = fish.vel + self.seperation(fish, neighbours, 30)
        fish.vel = fish.vel + self.allignment(fish, neighbours, 0.001)
        fish.vel = fish.vel + self.cohesion(fish, neighbours, 0.004)
  def seperation(self, fish, neighbours, seperation_strength):
    seperationVel = Vector(0, 0)
    totalVel = Vector(0,0)
    if(len(neighbours) != 0):
      for neighbour in neighbours:
        if(sqrt((fish.rect.centerx-neighbour.rect.centerx)**2+(fish.rect.centery-neighbour.rect.centery)**2) != 0):
          #definerer kraftens styrke ud fra afstanden til den nærmeste fisk
          styrke = (1/(sqrt((fish.rect.centerx-neighbour.rect.centerx)**2+(fish.rect.centery-neighbour.rect.centery)**2))**2)
          # print(f"{sqrt((fish.rect.centerx-neighbour.rect.centerx)**2+(fish.rect.centery-neighbour.rect.centery)**2)} AHHH")
          totalVel = totalVel + Vector((fish.rect.centerx - neighbour.rect.centerx), (fish.rect.centery - neighbour.rect.centery))*styrke
      seperationVel = (totalVel/len(neighbours))*seperation_strength
    return seperationVel
  def allignment(self, fish, neighbours, allignment_strength):
    allignment_vector = Vector(0, 0)
    total_vector = Vector(0, 0)
    if(len(neighbours) != 0):
      for neighbour in neighbours:
        total_vector = total_vector + neighbour.vel
      allignment_vector = (total_vector/len(neighbours))*allignment_strength
    return allignment_vector

    
    
  def cohesion(self, fish, neighbours, cohesion_strength):
    allignment_vector = Vector(0, 0)
    total_vector = Vector(0, 0)
    if(len(neighbours) != 0):
      for neighbour in neighbours:
        total_vector = total_vector + Vector(neighbour.rect.centerx-fish.rect.centerx, neighbour.rect.centery-fish.rect.centery)
      allignment_vector = (total_vector/len(neighbours))*cohesion_strength
    return allignment_vector
      
    



      


    
