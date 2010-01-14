from Case import Case
import random, pygame, heapq

class Labyrinthe:
    def __init__(self, w, h):
        print "Initializing labyrinthe ...",
        self.width = w
        self.height = h
        self.caseArray = []
        for i in range(0, self.width):
            ligne = []
            for j in range(0, self.height):
                ligne.append(Case(i, j))
            self.caseArray.append(ligne)

        print "done"

    def buildPaths(self, startx, starty):
        print "Building paths ...",
        tempList = [self.caseArray[startx][starty]]
        self.caseArray[startx][starty].content = 0
        delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        words = ["right", "left", "down", "up"]
        counter = 0
        while len(tempList) != 0:
            counter += 1
            orig = tempList.pop(0)
#            print counter, "current case : [", orig.x, orig.y, "] connecting to",
            order = range(4)
            random.shuffle(order)
            for i in order:

                destx = orig.x + delta[i][0]
                desty = orig.y + delta[i][1]
                if (destx in range(self.width)) and (desty in range(self.height)):
                    # if the dest is not yet connected, add to the list, and try to connect it
                    if self.caseArray[destx][desty].content == -1:
                        proba = 0.8
                    else:
                        proba = 0.1

                    r = random.uniform(0, 1)
                    if r < proba:
                        self.caseArray[destx][desty].content = 0
                        tempList.append(self.caseArray[destx][desty])
#                            print words[i], delta[i],
                        self.caseArray[orig.x][orig.y].destinations[words[i]] = self.caseArray[destx][desty]
                        self.caseArray[destx][desty].destinations[self.getOpposite(words[i])] = self.caseArray[orig.x][orig.y]
#                            print "[", self.caseArray[destx][desty].x, self.caseArray[destx][desty].y, "]",
        print " done"

    def toString(self):
        tmp = ""
        for j in range(0, self.width):
            #printing the first line of each case
#            s = ""
#            for i in range(0, self.height):
#                s += " "
#                d = self.caseArray[i][j]
#                if "up" in d.destinations:
#                    s += "|"
#                else:
#                    s += " "
#                s += " "
#            tmp += s + "\n"
            s = ""
            for i in range(0, self.height):
                d = self.caseArray[i][j]
                if "left" in d.destinations:
                    s += "-"
                else:
                    s += " "
                s += "+"
                if "right" in d.destinations:
                    s += "-"
                else:
                    s += " "
            tmp += s + "\n"
            s = ""
            for i in range(0, self.height):
                d = self.caseArray[i][j]
                s += " "
                if "down" in d.destinations:
                    s += "|"
                else:
                    s += " "
                s += " "
            tmp += s + "\n"
        return tmp

    def printCases(self):
        for i in range(self.width):
            for j in range(self.height):
                case = self.caseArray[i][j]
                print "[" + str(case.x) + "," + str(case.y) + "] connected to",
                for dir in case.destinations.keys():
                    print dir + " : [" + str(case.destinations[dir].x) + "," + str(case.destinations[dir].y) + "]",
                print


    def addCase(self, c):
        for case in self.caseArray:
            print case.x == c.x and case.y == c.y
            if case.x == c.x and case.y == c.y:
                pass
        self.caseArray.append(c)

    def getCaseAt(self, pos):
        return self.caseArray[pos[0]][pos[1]]

    def getOpposite(self, dir):
        if dir == "up":
            return "down"
        if dir == "down":
            return "up"
        if dir == "left":
            return "right"
        if dir == "right":
            return "left"

    def computePath(self, start, end):
        openList = [start]
        estimate = [start.getDistManhattan(end)]
        closedList = []
        parent = {}
        parent[start] = None
        while len(openList) != 0:
            id = 0
            dist = 100000000
            #Getting the index of the node which is the closest of the end
            for i in range(len(estimate)):
                if estimate[i] < dist:
                    id = i
                    dist = estimate[i]
            current = openList[id]
            #adding the node to the closed list, and removing the node from open list
            closedList.append(current)
            del estimate[id]
            del openList[id]

            #if the node is the goal, stop and build the path
            if current == end:
                path = [end]
                while current != start:
                    path = [parent[current]] + path
                    current = parent[current]
                return path

            #Adding the neighbors
            for n in current.getNeighbors():
                if n not in closedList:
                    e = dist + 1 + n.getDistManhattan(end)
                    if n in openList:
                        if e < estimate[openList.index(n)]:
                            estimate[openList.index(n)] = e
                            parent[n] = current
                    else:
                        openList.append(n)
                        parent[n] = current
                        estimate.append(e)



