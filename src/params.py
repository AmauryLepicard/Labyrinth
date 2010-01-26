class ParamLoader:
    def __init__(self):
        pass
        self.params = {'debug' : 0, 'labWidth' : 10, 'labHeight' : 10, 'tileSize' : 32, 'agentsNum' : 2}
        f = open("laby.ini")
        c = f.readline().split()
        while c != "":
            if len(c) == 3:
                self.params[c[0]] = int(c[2])
            c = f.readline().split()

params = ParamLoader()
