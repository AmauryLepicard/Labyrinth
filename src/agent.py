import random

import pygame
import utils
from labyrinth import lab
from mailServer import mail
from params import params


# TODO : systeme de satisfaction
#       -calculer score en fonction des objectifs atteints

class Agent:
    def __init__(self, x, y, c, i):
        self.x = x
        self.y = y
        self.dir = "N"
        self.pathToGoal = []
        self.globalGoal = None
        self.goalReached = False
        self.currentCase = c
        self.maxSpeed = 2
        self.id = i
        self.currentDecision = "moveToGoal"
        self.health = 1.0
        self.hunger = 0.0
        self.beliefs = {'minotaurCoords': (0, 0), 'exitCoords': (0, 0), 'labyrinthMap': [c]}

    def __str__(self):
        return "Agent " + self.id + " at [" + str(self.x) + "," + str(self.y) + "]"

    def update(self):
        self.checkGoals()
        self.checkMessages()
        self.updateKnowledge()
        self.takeDecision()
        self.act()

    def checkGoals(self):
        if self.currentDecision == "moveToGoal":
            if self.currentCase == self.globalGoal:
                #                print( "goal reached", str(self.currentCase))
                self.goalReached = True

    def checkMessages(self):
        for m in mail.getMessages(self):
            print(m[0].id, "->", self.id, ":", m[1])

    def updateKnowledge(self):
        if self.currentCase not in self.beliefs['labyrinthMap']:
            self.beliefs['labyrinthMap'].append(self.currentCase)

    def takeDecision(self):
        if self.goalReached:
            self.globalGoal = lab.getCaseAt(random.randint(0, lab.width - 1), random.randint(0, lab.height - 1))
            self.currentDecision = "moveToGoal"

    def act(self):
        if self.currentDecision == "moveToGoal":
            self.updatePos()

    def updatePos(self):
        # print( "updating pos ", self.id, len(self.pathToGoal))
        if len(self.pathToGoal) != 0:
            if self.pathToGoal[0].content != None:
                #print( "Collision : ", self.id, "avec",self.pathToGoal[0].content.id)
                mail.addMessage(self, self.pathToGoal[0].content, "you're blocking me !!")
                pygame.event.post(
                    pygame.event.Event(utils.COLLISION, {"agent": self, "collider": self.pathToGoal[0].content}))
                return
            else:
                xgoal = self.pathToGoal[0].x * params.dict['tileSize']
                ygoal = self.pathToGoal[0].y * params.dict['tileSize']

                if self.x > xgoal:
                    self.dir = "W"
                    self.x -= self.getSpeed()
                if self.x < xgoal:
                    self.dir = "E"
                    self.x += self.getSpeed()
                if self.y > ygoal:
                    self.dir = "N"
                    self.y -= self.getSpeed()
                if self.y < ygoal:
                    self.dir = "S"
                    self.y += self.getSpeed()

                if self.x == xgoal and self.y == ygoal:
                    self.pathToGoal[0].content = self
                    self.pathToGoal = self.pathToGoal[1:]

        if len(self.pathToGoal) == 0:
            pygame.event.post(pygame.event.Event(utils.ARRIVED, {"agent": self, "goal": self.currentCase}))
            return

    def getSpeed(self):
        return self.maxSpeed * self.health * (1 - self.hunger)
