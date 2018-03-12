import math
import pygame

from params import params

COLLISION = 24
ARRIVED = 25


def getDistance(xa, ya, xb, yb):
    return (xa - xb) * (xa - xb) + (ya - yb) * (ya - yb)


def getDistManhattan(xa, ya, xb, yb):
    return math.fabs(xa - xb) + math.fabs(ya - yb)

def getGridCoords(mx, my):
    return mx / params['tileSize'], my / params['tileSize']

def pause():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return

def pathToString(path):
    s = ""
    for c in path:
        s += "(" + str(c.x) + "," + str(c.y) + ")"
    return s
