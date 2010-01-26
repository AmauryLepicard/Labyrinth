import pygame
import game
from params import params

pygame.init()

myGame = game.Game(params['agentsNum'], params['debug'])
myGame.run()
print "coucou"
