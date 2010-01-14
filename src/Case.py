import math

class Case:
    def __init__(self, x = 0, y = 0):
        self.destinations = {}
        self.x = x
        self.y = y
        self.content = -1

    def getImageCode(self):
        s = 0
        i = 1
        for dir in ["up", "right", "down", "left"]:
            if dir in self.destinations.keys():
                s += i
            else:
                s += 0
            i = i * 2
        return s

    def getNeighbor(self, dir):
        if dir in self.destinations.keys():
            return self.destinations[dir]

    def getNeighbors(self):
        return self.destinations.values()

    def getDistance(self, c):
        return (self.x - c.x) * (self.x - c.x) + (self.y - c.y) * (self.y - c.y)
    
    def getDistManhattan(self, c):
        return math.fabs(self.x - c.x) +math.fabs (self.y - c.y)
