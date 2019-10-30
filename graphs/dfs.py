class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = []
        self.cor = 'branco'

    def add_vizinho(self, vertice):
        dic_vizinhos = set(self.vizinhos)
        if vertice not in dic_vizinhos:
            self.vizinhos.append(vertice)
            self.vizinhos.sort()


class Grafo_Lista:
    def __init__(self, iteravel=None):
        self.ponderado = False
        if iteravel is None:
            self.vertices = {}

        else:
            self.vertices = {}
            if len(iteravel[0]) > 2:
                self.ponderado = True
            for i in range(len(iteravel)):

                for j in range(1):
                    if self.ponderado is False:
                        self.add_vertice(Vertice(iteravel[i][0]))
                        self.add_vertice(Vertice(iteravel[i][1]))
                        self.add_aresta(iteravel[i][0], iteravel[i][1])

                    else:
                        self.add_vertice(Vertice(iteravel[i][0]))
                        self.add_vertice(Vertice(iteravel[i][1]))
                        self.add_aresta(iteravel[i][0], iteravel[i][1], iteravel[i][2])


    def add_vertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nome not in self.vertices:
            self.vertices[vertice.nome] = vertice
            return True

        else:
            return False

    def add_aresta(self, v1, v2, peso=1):
        if v1 in self.vertices and v2 in self.vertices:
            if self.ponderado is False:
                for key, value in self.vertices.items():
                    if key == v1:
                        value.add_vizinho(v2)

                    if key == v2:
                        value.add_vizinho(v1)

            else:
                for key, value in self.vertices.items():
                    if key == v1:
                        value.add_vizinho((v2, peso))

                    if key == v2:
                        value.add_vizinho((v1, peso))

            return True

        else:
            return False

    def verifica_aresta(self, v1, v2):
        if v2 in self.vertices[v1].vizinhos or v1 in self.vertices[v2].vizinhos:
            return True
        return False

    def grau_saida(self, vertice):
        #return len(self.vertices[vertice].vizinhos)
        pass

    def grau_entrada(self, vertice):
        '''entrada = 0
        for i in self.vertices:
            if vertice in self.vertices[i].vizinhos:
                entrada += 1

        return entrada'''
        pass

    def adjacentes(self, vertice):
        return self.vertices[vertice].vizinhos

    def __str__(self):
        retorno = ''
        if self.ponderado is False:
            for key in sorted(list(self.vertices.keys())):
                retorno += str(key) + str(self.vertices[key].vizinhos) + '\n'

        else:

        return retorno

    def dfs(self, vertice):
        vertice.cor = 'cinza'

        for v in vertice.vizinhos:
            if self.vertices[v].cor == 'branco':
                self.dfs(self.vertices[v])
        vertice.cor = 'preto'