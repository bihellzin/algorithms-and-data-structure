import numpy as np
'''
Depende da abordagem que se espera, caso a intenção seja provar os casos onde
a certeza é de 100%, deve ser utilizado o endereçamento fechado, com cada índice
da tabela representando um dia do ano. Caso o interesse seja comprovar os outros
casos, onde o número de pessoas é fixo, então a tabela de endereçamento aberto
é uma opção.

O tipo de tabela utilizado deve ser o de endereçamento fechado, pois devo ter
certeza de que eu não vou ocupar 2 espaços na lista com duas pessoas fazendo 
aniversário no mesmo dia. Caso isso ocorra, já se torna impossível provar o
paradóxo para se ter 100% de certeza.
'''


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
    def __init__(self, indices=365):
        self.tabela = np.full(indices, None)
        self.indices = indices

    def lerArquivo(self, arquivo='pessoasEDatas.txt'):
        file = open(arquivo, 'r')
        linhas = []

        for linha in file.readlines():
            linha = linha.strip()
            linha = linha.split()
            linhas.append(linha)

        return linhas

    def adicionarNaTabela(self):
        arquivo = self.lerArquivo()

        for i in range(len(arquivo)):
            if arquivo[i][1][3:5] == '01':
                indiceNaTabela = int(arquivo[i][1][0:2]) % self.indices

            elif arquivo[i][1][3:5] == '02':
                indiceNaTabela = (int(arquivo[i][1][0:2]) + 31) % self.indices

            elif arquivo[i][1][3:5] == '03':
                indiceNaTabela = (int(arquivo[i][1][0:2]) + 59) % self.indices

            elif arquivo[i][1][3:5] == '04':
                indiceNaTabela = (int(arquivo[i][1][0:2]) + 90) % self.indices

            elif arquivo[i][1][3:5] == '05':
                indiceNaTabela = (int(arquivo[i][1][0:2]) + 120) % self.indices

            elif arquivo[i][1][3:5] == '06':
                indiceNaTabela = (int(arquivo[i][1][0:2]) + 151) % self.indices

            elif arquivo[i][1][3:5] == '07':
                indiceNaTabela = (int(arquivo[i][1][0:2]) + 181) % self.indices

            elif arquivo[i][1][3:5] == '08':
                indiceNaTabela = (int(arquivo[i][1][0:2]) + 212) % self.indices

            elif arquivo[i][1][3:5] == '09':
                indiceNaTabela = (int(arquivo[i][1][0:2]) + 243) % self.indices

            elif arquivo[i][1][3:5] == '10':
                indiceNaTabela = (int(arquivo[i][1][0:2]) + 273) % self.indices

            elif arquivo[i][1][3:5] == '11':
                indiceNaTabela = (int(arquivo[i][1][0:2]) + 304) % self.indices

            elif arquivo[i][1][3:5] == '12':
                indiceNaTabela = (int(arquivo[i][1][0:2]) + 334) % self.indices

            else:
                continue

            if self.tabela[indiceNaTabela] is None:
                self.tabela[indiceNaTabela] = LinkedList()
                self.tabela[indiceNaTabela].inserirInicio(
                    arquivo[i][0] + ' ' + arquivo[i][1])

            else:
                self.tabela[indiceNaTabela].inserirFinal(
                    arquivo[i][0] + ' ' + arquivo[i][1])

    def imprimirDoisOuMais(self):
        for i in range(len(self.tabela)):
            if self.tabela[i] is None:
                continue

            else:
                if self.tabela[i].size >= 2:
                    for j in self.tabela[i]:
                        print(j)
