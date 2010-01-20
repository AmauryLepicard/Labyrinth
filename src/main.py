import pygame
import game, utils

pygame.init()

myGame = game.Game(utils.load('agentsNum'), utils.load('debug'))
myGame.run()
