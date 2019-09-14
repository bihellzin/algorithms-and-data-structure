import numpy as np

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
            ultimoNo = self.root
            while ultimoNo.prox is not None:
                ultimoNo = ultimoNo.prox
            ultimoNo.prox = novoNo
            novoNo.ante = ultimoNo
            novoNo.prox = None
        self.size += 1

    def __str__(self):
        nos = ''

        ultimoNo = self.root
        while True:
            if ultimoNo.prox is None:
                nos += ultimoNo.data
                break
            else:
                nos += ultimoNo.data + ', '
            ultimoNo = ultimoNo.prox

        return nos

    def __repr__(self):
        retorno = 'ListaEncadeadaDupla('
        if type(self.objeto_iteravel) is str:
            retorno += "\'"+ self.objeto_iteravel + '\'' + ')'

        elif type(self.objeto_iteravel) is list:
            retorno += "["+ self.objeto_iteravel + ']' + ')'

        elif type(self.objeto_iteravel) is dict:
            retorno += "{" + self.objeto_iteravel + '}' + ')'

        return retorno

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

    #def anexar

def main():
    lista = ListaDuplamenteEncadeada('algoritmos')
    print(lista)
    print(repr(lista))
    print(lista[10])
    lista[0] = 'abc'
    print(lista[0])
    print(lista.indice('s'))
    joao = No('joao')
    lista.anexar(joao)
    print(lista[10])

main()