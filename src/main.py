import sys, pygame, random
from Labyrinthe import Labyrinthe
from Agent import Agent
pygame.init()


labWidth = 12
labHeight = 12
tileWidth = 32
tileHeight = 32

size = width, height = tileWidth * labWidth, tileHeight * labHeight
screen = pygame.display.set_mode(size)
black = 0, 0, 0

def getGridCoords(mx, my):
    return mx / tileWidth, my / tileHeight

tileset = pygame.image.load("data/dungeon.png")
agentImage = {}
for dir in ["N", "S", "E", "W"]:
    agentImage[dir] = pygame.image.load("data/agent" + dir + ".png")

myLaby = Labyrinthe(labWidth, labHeight)
myLaby.buildPaths(2, 2)
agents = []
for i in range(2):
    agents.append(Agent((32 * random.randint(0, labWidth-1), 32 * random.randint(0, labHeight-1))))

oldTick = 0

while 1:
    #player events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
#        if event.type == pygame.MOUSEBUTTONDOWN:
#            x, y = pygame.mouse.get_pos()
#            myAgent.pathToGoal = myLaby.computePath(myLaby.getCaseAt((myAgent.pos[0] / 32, myAgent.pos[1] / 32)), myLaby.getCaseAt(getGridCoords(x, y)))[1:]

    for a in agents:
        if len(a.pathToGoal)==0:
            a.pathToGoal = myLaby.computePath(myLaby.getCaseAt(((a.pos[0] / 32, a.pos[1] / 32))), myLaby.getCaseAt((random.randint(0,labWidth-1), random.randint(0,labWidth-1))))[1:]
            
            
    #updating
#    if ((oldTick / 100) != (pygame.time.get_ticks() / 100)):
#        print "Updating positions"
        for a in agents:
            a.updatePos()

    #printing
    screen.fill(black)
    for i in range(labWidth):
        for j in range(labHeight):
            screen.blit(tileset, pygame.Rect(tileWidth * i, tileHeight * j, tileWidth, tileHeight), pygame.Rect(tileWidth * myLaby.getCaseAt((i, j)).getImageCode(), 0, tileWidth, tileHeight))
    for a in agents:
        screen.blit(agentImage[a.dir], pygame.Rect(a.pos[0], a .pos[1], tileWidth, tileHeight))
    pygame.display.flip()



