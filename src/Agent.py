import pygame

class Agent:
    def __init__(self, pos):
        self.pos = pos
        self.dir = "N"
        self.pathToGoal = []
        self.speed = 4

    def updatePos(self):
        if len(self.pathToGoal) != 0:
            if self.getNextCase().content == 0:
                pygame.event.post(pygame.event.Event())
                xgoal = self.getNextCase().x * 32
                ygoal = self.getNextCase().y * 32
                x, y = self.pos
                if x > xgoal:
                    self.dir = "W"
                    x -= self.speed
                if x < xgoal:
                    self.dir = "E"
                    x += self.speed
                if y > ygoal:
                    self.dir = "N"
                    y -= self.speed
                if y < ygoal:
                    self.dir = "S"
                    y += self.speed
                self.pos = (x, y)
    
                if self.pos == (xgoal, ygoal):
                    self.getNextCase().content = self
                    self.pathToGoal = self.pathToGoal[1:]

    def getNextCase(self):
        return self.pathToGoal[0]