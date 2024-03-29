import numpy as np

# Q1

class No:
    def __init__(self, data=None, prox=None, ante=None):
        self.data = data
        self.prox = prox
        self.ante = ante

class ListaDuplamenteEncadeada:

    def __init__(self, objeto_iteravel=None):
        self.root = None
        self.size = 0
        if objeto_iteravel is not None:
            self.objeto_iteravel = objeto_iteravel
            for i in objeto_iteravel:
                node = No(i)
                self.anexar(node)
            self.size = len(objeto_iteravel)

    def listaVazia(self):
        if self.size:
            return False
        return True

    def anexar(self, novoNo):
        if self.listaVazia():
            self.root = novoNo
            self.root.prox = None

        else:
            if type(novoNo) is str or type(novoNo) is int or type(novoNo) is dict or type(novoNo) is list or type(novoNo) is tuple:
                novoNo = No(novoNo)
            ultimoNo = self.root
            while ultimoNo.prox is not None:
                ultimoNo = ultimoNo.prox
            ultimoNo.prox = novoNo
            novoNo.ante = ultimoNo
            novoNo.prox = None
        self.size += 1

    def __str__(self):
        if self.size > 0:
            nos = ''

            ultimoNo = self.root
            while True:
                if ultimoNo.prox is None:
                    nos += str(ultimoNo.data)
                    break
                else:
                    nos += str(ultimoNo.data) + ', '
                ultimoNo = ultimoNo.prox

            return nos

        else:
            return 'Lista vazia'
    def __repr__(self):
        if self.listaVazia():
            return 'ListaEncadeadaDupla()'

        retorno = 'ListaEncadeadaDupla(['
        ultimo = self.root
        while True:
            if ultimo.prox is None:
                retorno += str(ultimo.data) + '])'
                return retorno
            retorno += str(ultimo.data) + ', '
            ultimo = ultimo.prox

    def __getitem__(self, indice):
        try:
            if indice >= self.size:
                raise IndexError
            else:
                inicio = 0
                procurado = self.root
                while inicio < indice:
                    procurado = procurado.prox
                    inicio += 1
                return procurado.data
        except IndexError:
                print('ERRO !\nVocê inseriu um índice maior que a quantidade de itens da lista')


    def __setitem__(self, indice, value):
        try:
            if indice >= self.size:
                raise IndexError
            else:
                inicio = 0
                procurado = self.root
                while inicio < indice:
                    procurado = procurado.prox
                    inicio += 1
                procurado.data = value

        except IndexError:
            print('ERRO !\nVocê inseriu um índice maior que a quantidade de itens da lista')

    def indice(self, value):
        try:
            encontrou =False
            inicio = 0
            procurado = self.root
            while inicio < self.size:
                if value == procurado.data:
                    return inicio
                procurado = procurado.prox
                inicio += 1
            if not encontrou:
                raise ValueError

        except ValueError:
            print('ERRO !\nVocê inseriu um valor que não existe')

    def selecionar(self, indice):
        if indice >= self.size:
            print('Índice maior que a quantidade de índices da lista')
        else:
            if indice == 0:
                item = self.root.data
                self.root = self.root.prox
                #self.root.ante = None
            else:
                inicio = 0
                achado = self.root
                proximo = achado.prox
                while inicio < indice:
                    achado = proximo
                    proximo = achado.prox
                    inicio += 1
                item = achado.data
                achado.ante.prox = proximo
                proximo.ante = achado.ante
            self.size -= 1
            return item

    def inserir(self, indice, valor):
        if indice > self.size:
            print('índice não pode ser inserido na lista')
            return

        if self.listaVazia():
            valor = No(valor)
            self.root = valor
            self.root.prox = None

        else:
            inicio = 0
            if type(valor) is str or type(valor) is int or type(valor) is dict or type(valor) is list or type(valor) is tuple:
                valor = No(valor)

            if indice == 0:
                temp = self.root
                self.root = valor
                self.root.prox = temp
                temp.ante = self.root
            else:
                achado = self.root
                proximo = achado.prox
                while inicio < indice:
                    achado = proximo
                    proximo = achado.prox
                    inicio += 1
                temp = achado.ante
                valor.ante = temp
                achado.ante.prox = valor
                achado.ante = valor
                valor.prox = achado
        self.size += 1

    def concatenar(self, lista):
        ultimoLista = lista.root
        while ultimoLista.prox is not None:
            self.anexar(lista.selecionar(0))
            ultimoLista = ultimoLista.prox
        self.anexar(lista.selecionar(0))

    def __iter__(self):
        class Ponteiro:
            def __init__(self, lista, passo=0):
                self.passo = passo
                self.lista = lista

            def __next__(self):
                if self.passo >= self.lista.size:
                    raise StopIteration
                value = self.lista[self.passo]
                self.passo += 1

                return value

        return Ponteiro(self)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Q2

class Fila:
    def __init__(self, size, inicio=-1):
        self.inicio = inicio
        self.end = inicio
        self.size = size
        self.espacosVazios = size
        self.queue = np.empty(size, int)

    def filaVazia(self):
        if self.espacosVazios == self.size:
            return True
        else:
            return False

    def filaCheia(self):
        if self.espacosVazios == 0:
            return True
        else:
            return False

    def enqueue(self, num):
        if self.filaCheia():
            print('A fila está cheia')
            return

        elif self.filaVazia():
            self.inicio += 1
            self.queue[self.inicio] = num
            self.espacosVazios -= 1
            self.end += 1

        else:
            self.espacosVazios -= 1
            if self.end == self.size - 1:
                self.end = 0
            else:
                self.end += 1
            self.queue[self.end] = num

    def dequeue(self):
        if self.filaVazia():
            print('A fila está vazia')
            return
        else:
            self.espacosVazios += 1
            removido = self.queue[self.inicio]
            if self.inicio == self.size - 1:
                self.inicio = 0
            else:
                self.inicio += 1
            return removido

class Pilha(Fila):
    def __init__(self, size):
        self.pilha = np.empty(size, int)
        self.topo = -1
        self.size = size

    def filaVazia(self):
        if self.topo == -1:
            return True
        else:
            return False

    def dequeue(self):
        if self.topo == -1:
            print('Não há elementos na pilha')
            return
        else:
            self.topo -= 1
            return self.pilha[self.topo + 1]

    def filaCheia(self):
        if (self.topo + 1) == self.size:
            return True
        else:
            return False

    def enqueue(self, num):
        if self.filaCheia():
            print('A pilha está cheia')
            return False
        else:
            self.pilha[self.topo + 1] = num
            self.topo += 1

if __name__ == '__main__':
    lista = ListaDuplamenteEncadeada('algoritmos')
    for p in lista:
        print(p)