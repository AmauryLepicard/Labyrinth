import math

COLLISION = 42
ARRIVED = 43

tileSize = 32

def getDistance((xa, ya), (xb, yb)):
    return (xa-xb)*(xa-xb)+(ya-yb)*(ya-yb)

def getDistManhattan((xa, ya), (xb, yb)):
    return math.fabs(xa-xb)+math.fabs(ya-yb)

def getGridCoords(mx, my):
    return mx / tileWidth, my / tileHeight

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

def load(paramName):
#    params = {'debug' : 0, 'labWidth' : 10, 'labHeight' : 10, 'tileSize' : 32, 'agentsNum' : 2}
    f = open("laby.ini")
    c = f.readline().split()
    while c != "":
        if len(c) == 3 and c[0] == paramName:
            return int(c[2])
        c = f.readline().split()
    print "bug",paramName

