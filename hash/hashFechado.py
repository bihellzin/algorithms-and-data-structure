import numpy as np


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def vazia(self):
        if self.size == 0:
            return True
        return False

    def inserirFinal(self, value):
        no = Node(value)
        if self.vazia():
            self.root = no

        else:
            ultimo = self.root
            while True:
                if ultimo.next is None:
                    break
                ultimo = ultimo.next

            ultimo.next = no
        self.size += 1

    def inserirInicio(self, value):
        no = Node(value)
        if self.vazia():
            self.root = no

        else:
            primeiro = self.root
            self.root = no
            self.root.next = primeiro

        self.size += 1

    def inserirMeio(self, value, indice):
        if indice > self.size:
            print('Índice não se encontra na lista')
        else:
            if indice == 0:
                self.inserirInicio(value)

            elif indice == self.size:
                self.inserirFinal(value)

            else:
                novoNo = Node(value)
                cont = 0
                no = self.root

                while True:
                    cont += 1

                    if cont == indice:
                        break

                    elif no.next is None:
                        break

                    no = no.next

                temp = no.next
                no.next = novoNo
                novoNo.next = temp

            self.size += 1

    def removerInicio(self):
        self.root = self.root.next
        self.size -= 1

    def removerFinal(self):
        penultimo = self.root
        ultimo = penultimo.next

        while True:
            if ultimo.next is None:
                break
            ultimo = ultimo.next
            penultimo = penultimo.next

        penultimo.next = None
        self.size -= 1

    def removerIndice(self, indice):
        if indice == 0:
            self.removerInicio()

        elif indice == self.size - 1:
            self.removerFinal()

        else:
            if indice >= self.size:
                print('Tá tirando né kraio')
                return

            else:
                penultimo = self.root
                ultimo = penultimo.next
                cont = 0

                while True:
                    cont += 1
                    if cont == indice:
                        break

                    ultimo = ultimo.next
                    penultimo = penultimo.next

                temp = ultimo.next
                penultimo.next = temp
        self.size -= 1

    def removerValor(self, value):
        ant = self.root
        atual = ant.next

        if ant.value == value:
            self.removerInicio()
            self.size -= 1
            print('Nó removido')

        else:

            while atual.next is not None:
                if atual.value == value:
                    ant.next = atual.next
                    print('Nó removido')
                    self.size -= 1
                    break
                atual = atual.next
                ant = ant.next
            print('Nó inexistente')

    def __getitem__(self, indice):
        try:
            if indice >= self.size:
                raise IndexError
            else:
                inicio = 0
                procurado = self.root
                while inicio < indice:
                    procurado = procurado.next
                    inicio += 1
                return procurado.value
        except IndexError:
            print(
                'ERRO !\nVocê inseriu um índice maior que a quantidade de itens da lista')

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


class HashTable:
    def __init__(self, indices=0):
        self.tabela = np.full(indices, None)
        self.indices = indices

    def lerArquivo(self, arquivo):
        pass
