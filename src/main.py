import sys, pygame, random
import labyrinth, agent, utils
pygame.init()


labWidth = 8
labHeight = 8
tileWidth = 32
tileHeight = 32
agentNumber = 2

size = width, height = tileWidth * labWidth, tileHeight * labHeight
screen = pygame.display.set_mode(size)
black = 0, 0, 0


tileset = pygame.image.load("data/dungeon.png")
agentImage = {}
for dir in ["N", "S", "E", "W"]:
    agentImage[dir] = pygame.image.load("data/agent" + dir + ".png")
goalImage = {}
for i in range(2):
    goalImage[i] = pygame.image.load("data/goal" + str(i+1) + ".png")

#myLab = labyrinth.Labyrinth(labWidth, labHeight)
#myLab.buildPaths(2, 2)
#myLab.save("lab.map")
myLab = labyrinth.load("lab.map")

labImage = pygame.Surface(size)
for i in range(labWidth):
    for j in range(labHeight):
        labImage.blit(tileset, pygame.Rect(tileWidth * i, tileHeight * j, tileWidth, tileHeight), pygame.Rect(tileWidth * myLab.getCaseAt(i, j).getImageCode(), 0, tileWidth, tileHeight))


agents = []
cpt=0
#for i in range(agentNumber):
#    cpt+=1
#    x = random.randint(0, labWidth - 1)
#    y = random.randint(0, labHeight - 1)
#    agents.append(agent.Agent(tileWidth * x, tileHeight * y, myLab.getCaseAt(x, y), cpt))
#    print "agent",cpt,":",agents[-1]

a = agent.Agent(tileWidth * 0, tileHeight * 0, myLab.getCaseAt(0, 0), 1)
a.pathToGoal = myLab.computePath(myLab.getCaseAt(a.x / tileWidth, a.y / tileHeight), myLab.getCaseAt(0, 6))
a.globalGoal = myLab.getCaseAt(0, 0)
agents.append(a)
a = agent.Agent(tileWidth * 0, tileHeight * 1, myLab.getCaseAt(0, 1), 2)
a.pathToGoal = myLab.computePath(myLab.getCaseAt(a.x / tileWidth, a.y / tileHeight), myLab.getCaseAt(6, 0))
a.globalGoal = myLab.getCaseAt(6, 0)
agents.append(a)

oldTick = 0
tickNumber = 0
while 1:
    #processing events
#    print "tick",
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            print "exiting..."
            sys.exit()
            
        if event.type == utils.ARRIVED:
            agent = event.dict['agent']
            agent.globalGoal = myLab.getCaseAt(random.randint(0, labWidth - 1), random.randint(0, labWidth - 1))
            agent.pathToGoal = myLab.computePath(myLab.getCaseAt(agent.x / tileWidth, agent.y / tileHeight), agent.globalGoal)
            
#            print tickNumber, agent.id, "arrive","new path : [", utils.pathToString(agent.pathToGoal), "]"
        
        if event.type == utils.COLLISION:
            agent = event.dict['agent']
#            print tickNumber, agent.id,"collision : old path : [", utils.pathToString(agent.pathToGoal), "]"
            newPath = myLab.computePath(agent.currentCase, agent.globalGoal)
            if len(newPath) == 0:
                agent.globalGoal = None
            agent.pathToGoal = newPath
#                print tickNumber, agent.id,"collision : new path : [", utils.pathToString(agent.pathToGoal), "]"
#            else:
#                print tickNumber, "pas de chemin disponible"

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            utils.pause()
    
    #updating agents positions
    for i in range(len(agents)):
        a = agents[i]
        a.currentCase.content = None
        a.updatePos()
        a.currentCase = myLab.getCaseAt(a.x / tileWidth, a.y / tileHeight)
        a.currentCase.content = a

    #printing
    screen.blit(labImage, (0,0))
    for a in agents:
        screen.blit(agentImage[a.dir], pygame.Rect(a.x, a.y, tileWidth, tileHeight))
        if len(a.pathToGoal) != 0:
            screen.blit(goalImage[a.id % 2], pygame.Rect(a.pathToGoal[len(a.pathToGoal)-1].x * tileWidth, a.pathToGoal[len(a.pathToGoal)-1].y * tileHeight, tileWidth, tileHeight))
    pygame.display.flip()
#    pygame.time.wait(20)
    tickNumber += 1
