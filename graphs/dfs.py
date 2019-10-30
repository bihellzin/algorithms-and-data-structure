class Vertex:
    def __init__(self, n):
        self.name = n
        self.weight = 1
        self.neighbors = list()

        self.discovery = 0
        self.finish = 0
        self.color = 'black'

    def add_neighbor(self, v):
        nset = set(self.neighbors)
        if v not in nset:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    def __init__(self, iteravel=None):
        if iteravel is None:
            self.vertices = {}
        else:
            for i in iteravel:
                if len(i) == 2:
                    Vertex(i[0])
