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
        saida = 0
        for i in self.vertices:
            if vertice in self.vertices[i].vizinhos:
                saida += 1

        return saida

    def grau_entrada(self, vertice):
        entrada = 0
        for i in self.vertices:
            if vertice in self.vertices[i].vizinhos:
                entrada += 1

        return entrada

    def adjacentes(self, vertice):
        return self.vertices[vertice].vizinhos

    def __str__(self):
        retorno = ''
        if self.ponderado is False:
            for key in sorted(list(self.vertices.keys())):
                retorno += str(key) + ': ' + str(self.vertices[key].vizinhos) +'\n'

        else:
            for key in sorted(list(self.vertices.keys())):
                retorno += str(key) + ': ' + str(self.vertices[key].vizinhos) +'\n'

        return retorno

    def __getitem__(self, indice):
        if indice >= len(self.vertices):
            raise IndexError
        lista = list(self.vertices)

        for i in range(len(lista)):
            if i == indice:
                return self.vertices[lista[i]].vizinhos

    '''def __repr__(self):
        retorno = 'Grafo_Lista('
        if self.ponderado is False:
            for i in range(len(self.vertices)):
                for j in self.vertices:
                    retorno += '''

    def maior_aresta(self):
        if self.ponderado is False:
            print('Grafo não ponderado, todas as arestas possuem o mesmo tamanho')


        else:
            maior = -9999999999999999
            for i in self.vertices:
                for j in range(len(self.vertices[i].vizinhos)):
                    if self.vertices[i].vizinhos[j][1] > maior:
                        maior = self.vertices[i].vizinhos[j][1]

            maiores = []
            for i in self.vertices:
                for j in range(len(self.vertices[i].vizinhos)):
                    if self.vertices[i].vizinhos[j][1] == maior:
                        maiores.append(str(self.vertices[i].nome) + str(self.vertices[self.vertices[i].vizinhos[j][0]].nome))

            return maiores

    def menor_aresta(self):
        if self.ponderado is False:
            print('Grafo não ponderado, todas as arestas possuem o mesmo tamanho')

        else:
            menor = 9999999999999999
            for i in self.vertices:
                for j in range(len(self.vertices[i].vizinhos)):
                    if self.vertices[i].vizinhos[j][1] < menor:
                        menor = self.vertices[i].vizinhos[j][1]

            menores = []
            for i in self.vertices:
                for j in range(len(self.vertices[i].vizinhos)):
                    if self.vertices[i].vizinhos[j][1] == menor:
                        menores.append(str(self.vertices[i].nome) + str(self.vertices[self.vertices[i].vizinhos[j][0]].nome))

            return menores

    def dfs(self, vertice, vertices_printados=''):
        print(vertice)
        self.vertices[vertice].cor = 'cinza'

        for v in self.vertices[vertice].vizinhos:
            if self.vertices[v].cor == 'branco':
                self.dfs(self.vertices[v].nome)
        self.vertices[vertice].cor = 'preto'

    def bfs(self, vertice):
        fila = []
        self.vertices[vertice].cor = 'cinza'
        print(self.vertices[vertice].nome)

        for v in self.vertices[vertice].vizinhos:
            fila.append(v)

        while len(fila) > 0:
            u = fila.pop(0)
            vertice_u = self.vertices[u]
            vertice_u.cor = 'cinza'
            print(vertice_u.nome)
            for v in vertice_u.vizinhos:
                vertice_v = self.vertices[v]

                if vertice_v.cor == 'branco':
                    fila.append(v)