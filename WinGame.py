import pygame as pg
import os

class GameWin():
  
  def __init__(self):
    self.HEIGHT = 600
    self.WIDTH = 600
    self.BG = pg.image.load(os.path.join("Sprites", "background-day.png"))
    self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))

  def drawWin(self):
    pg.display.set_caption('Flappy Birds AI Trainer')
    self.screen.blit(self.BG, (0,0))
    

