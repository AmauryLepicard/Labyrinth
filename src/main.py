import pygame
import game
from params import params

pygame.init()

myGame = game.Game(params.dict['agentsNum'], params.dict['debug'])
myGame.run()
