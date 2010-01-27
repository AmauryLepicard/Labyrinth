class ParamLoader:
    def __init__(self):
        pass
        self.dict = {'debug' : 0, 'labWidth' : 10, 'labHeight' : 10, 'tileSize' : 32, 'agentsNum' : 2}
        f = open("laby.ini")
        c = f.readline().split()
        while len(c) != 0:
            if len(c) == 3:
                self.dict[c[0]] = int(c[2])
            c = f.readline().split()

params = ParamLoader()
