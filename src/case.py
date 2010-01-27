
class Case:
    def __init__(self, i, x = 0, y = 0):
        self.destinations = {}
        self.x = x
        self.y = y
        self.content = None
        self.id = i
        self.h = 0
        self.g = 0

    def __str__(self):
        return "Case " + self.id + " at [" + str(self.x) + "," + str(self.y) + "]"

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
