import pygame as pg
import os
import sys
import Bird
import Pipe
import WinGame

alive = True

while alive:
  pg.init
  win = WinGame.GameWin()
  win.drawWin()
  for event in pg.event.get():
    if event.type == pg.QUIT:
      alive = False
      pg.quit()
      quit()