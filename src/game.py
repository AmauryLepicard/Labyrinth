import agent, utils
from labyrinth import lab
from mailServer import mail
import sys, random, pygame

black = 0, 0, 0

class Game:
    def __init__(self, n, debug):
#        lab.width = w   
#        lab.height = h
        self.tileWidth = utils.tileSize
        self.tileHeight = utils.tileSize
        self.agentNumber = n
        self.debug = debug

        from labyrinth import lab
        lab.buildPaths(2, 2)
        lab.save("lab.map")
#        lab = labyrinth.load("lab.map")

        size = width, height = self.tileWidth * lab.width, self.tileHeight * lab.height
        self.screen = pygame.display.set_mode(size)
        

        self.tileset = pygame.image.load("data/dungeon.png")
        self.agentImage = {}
        for dir in ["N", "S", "E", "W"]:
            self.agentImage[dir] = pygame.image.load("data/agent" + dir + ".png")
        self.goalImage = {}
        for i in range(2):
            self.goalImage[i] = pygame.image.load("data/goal" + str(i+1) + ".png")

#        self.dotImage = pygame.image.load("data/dot.png")



        self.labImage = pygame.Surface(size)
        for i in range(lab.width):
            for j in range(lab.height):
                self.labImage.blit(self.tileset, pygame.Rect(self.tileWidth * i, self.tileHeight * j, self.tileWidth, self.tileHeight), pygame.Rect(self.tileWidth * lab.getCaseAt(i, j).getImageCode(), 0, self.tileWidth, self.tileHeight))


        self.agents = []
        cpt=0
        for i in range(self.agentNumber):
            cpt+=1
            x = random.randint(0, lab.width - 1)
            y = random.randint(0, lab.height - 1)
            xg = random.randint(0, lab.width - 1)
            yg = random.randint(0, lab.height - 1)
            a = agent.Agent(self.tileWidth * x, self.tileHeight * y, lab.getCaseAt(x, y), "a"+str(cpt))
            a.pathToGoal = lab.computePath(lab.getCaseAt(a.x / self.tileWidth, a.y / self.tileHeight), lab.getCaseAt(xg, yg))
            a.globalGoal = lab.getCaseAt(xg, yg)
            self.agents.append(a)
#           print "agent",cpt,":",self.agents[-1]

#        a = self.agent.Agent(self.tileWidth * 0, self.tileHeight * 0, lab.getCaseAt(0, 0), 1)
#        a.pathToGoal = lab.computePath(lab.getCaseAt(a.x / self.tileWidth, a.y / self.tileHeight), lab.getCaseAt(0, 6))
#        a.globalGoal = lab.getCaseAt(0, 0)
#        agents.append(a)
#        a = agent.Agent(self.tileWidth * 0, self.tileHeight * 1, myLab.getCaseAt(0, 1), 2)
#        a.pathToGoal = myLab.computePath(myLab.getCaseAt(a.x / self.tileWidth, a.y / self.tileHeight), myLab.getCaseAt(6, 0))
#        a.globalGoal = myLab.getCaseAt(6, 0)
#        agents.append(a)

    
    def run(self):
        oldTick = 0
        tickNumber = 0
        while 1:
#            print "Nb de messages : " + str(mail.getMailNumber())
           #processing events
        #    print "tick",
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    print "exiting..."
                    sys.exit()
                    
                if event.type == utils.ARRIVED:
                    agent = event.dict['agent']
                    agent.globalGoal = lab.getCaseAt(random.randint(0, lab.width - 1), random.randint(0, lab.height - 1))
                    agent.pathToGoal = lab.computePath(lab.getCaseAt(agent.x / self.tileWidth, agent.y / self.tileHeight), agent.globalGoal)
                    
        #            print tickNumber, agent.id, "arrive","new path : [", utils.pathToString(agent.pathToGoal), "]"
                
                if event.type == utils.COLLISION:
                    agent = event.dict['agent']
        #            print tickNumber, agent.id,"collision : old path : [", utils.pathToString(agent.pathToGoal), "]"
                    newPath = lab.computePath(agent.currentCase, agent.globalGoal)
                    if len(newPath) == 0:
                        agent.globalGoal = None
                    agent.pathToGoal = newPath
        #                print tickNumber, agent.id,"collision : new path : [", utils.pathToString(agent.pathToGoal), "]"
        #            else:
        #                print tickNumber, "pas de chemin disponible"

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    utils.pause()
            
            #updating agents positions
            for a in self.agents:
                a.currentCase.content = None
                a.update()
                a.currentCase = lab.getCaseAt(a.x / self.tileWidth, a.y / self.tileHeight)
                a.currentCase.content = a

            #printing
            self.screen.blit(self.labImage, (0,0))
            for a in self.agents:
                self.screen.blit(self.agentImage[a.dir], pygame.Rect(a.x, a.y, self.tileWidth, self.tileHeight))
                if len(a.pathToGoal) != 0:
#                    for c in a.pathToGoal:
#                        self.screen.blit(self.dotImage, pygame.Rect(c.x * self.tileWidth, c.y * self.tileHeight, self.tileWidth, self.tileHeight));
                    start = (a.currentCase.x + 0.5) * self.tileWidth, (a.currentCase.y + 0.5) * self.tileHeight
                    end = (a.pathToGoal[0].x + 0.5) * self.tileWidth, (a.pathToGoal[0].y + 0.5) * self.tileHeight
                    pygame.draw.line(self.screen, (255,0,0), start, end) 
#                       
                    for i in range(len(a.pathToGoal)-1):
                        start = (a.pathToGoal[i].x + 0.5) * self.tileWidth, (a.pathToGoal[i].y + 0.5) * self.tileHeight
                        end = (a.pathToGoal[i + 1].x + 0.5) * self.tileWidth, (a.pathToGoal[i + 1].y + 0.5) * self.tileHeight
                        pygame.draw.line(self.screen, (255,0,0), start, end) 
#                        self.screen.blit(self.dotImage, pygame.Rect(c.x * self.tileWidth, c.y * self.tileHeight, self.tileWidth, self.tileHeight));
                    self.screen.blit(self.goalImage[0], pygame.Rect(a.pathToGoal[len(a.pathToGoal)-1].x * self.tileWidth, a.pathToGoal[len(a.pathToGoal)-1].y * self.tileHeight, self.tileWidth, self.tileHeight))
            pygame.display.flip()
        #    pygame.time.wait(20)
            tickNumber += 1
