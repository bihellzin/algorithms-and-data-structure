class Node:
    def __init__(self, value, key, right=None, left=None):
        self.value = value
        self.key = key
        self.right = right
        self.left = left
        self.parent = None

    def __eq__(self, outroNo):
        if type(self) != type(outroNo):
            raise TypeError
        return self.value == outroNo.value

    def __lt__(self, outroNo):
        if type(self) != type(outroNo):
            raise TypeError
        return self.value < outroNo.value

    def __le__(self, outroNo):
        if type(self) != type(outroNo):
            raise TypeError
        return self.value <= outroNo.value

    def __gt__(self, outroNo):
        if type(self) != type(outroNo):
            raise TypeError
        return self.value > outroNo.value

    def __ge__(self, outroNo):
        if type(self) != type(outroNo):
            raise TypeError
        return self.value >= outroNo.value

    def __ne__(self, outroNo):
        if type(self) != type(outroNo):
            raise TypeError
        return self.value != outroNo.value


class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.elementos = 0

    def insert(self, newNode, key):
        if type(newNode) is int:
            newNode = Node(newNode, key)
        if self.root is None:
            self.root = newNode

        else:
            node = self.root
            while newNode.parent is None:
                if newNode < node:
                    if node.left is None:
                        node.left = newNode
                        newNode.parent = node
                        break
                    node = node.left

                elif newNode > node:
                    if node.right is None:
                        node.right = newNode
                        newNode.parent = node
                        break
                    node = node.right

                elif newNode == node:
                    print('Elemento já foi colocado na árvore')
                    return
        self.elementos += 1

    def search(self, value):
        node = self.root
        if value == node.value:
            return node

        while True:
            if value > node.value:
                if node.value == value:
                    return node

                elif node.right is None:
                    print('Value not found')
                    return False

                node = node.right

            else:
                if node.value == value:
                    return node

                elif node.left is None:
                    print('Value not found')
                    return False

                node = node.left

    def remove(self, value):
        node = self.search(value)
        if node is not False:
            # nó sem filhos
            if node is self.root:
                self.root = None

            elif node.right is None and node.left is None:
                if node.parent.right is node:
                    node.parent.right = None
                    node.parent = None
                else:
                    node.parent.left = None
                    node.parent = None

            # nó com dois filhos pegando o menor da subárvore da direita
            elif node.right is not None and node.left is not None:
                curNode = node.right
                while curNode.left is not None:
                    curNode = curNode.left

                curNode.left = node.left
                node.left.parent = curNode

                if node.right is curNode:
                    temp2 = curNode.left
                    curNode.right = node.right.right
                    curNode.left = temp2
                    temp2.parent = curNode

                else:
                    curNode.right = node.right
                    temp2 = node.right
                    while temp2.left is not None:
                        temp2 = temp2.left
                    temp2.parent.left = None

                curNode.parent = node.parent

                if node.value > node.parent.value:
                    node.parent.right = curNode

                elif node.value < node.parent.value:
                    node.parent.left = curNode

            # nó com um filho

            elif node.right is None and node.left is not None:
                if node.value > node.parent.value:
                    node.parent.right = node.left
                    node.parent = None

                else:
                    node.parent.left = node.left
                    node.parent = None

            elif node.right is not None and node.left is None:
                if node.value > node.parent.value:
                    node.parent.right = node.right
                    node.parent = None

                else:
                    node.parent.left = node.right
                    node.parent = None

            self.elementos -= 1

            '''
            nó com dois filhos pegando o maior número da subárvore da esquerda

            elif node.right is not None and node.left is not None:
                curNode = node.left
                while curNode.right is not None:
                    curNode = curNode.right

                curNode.right = node.right
                node.right.parent = curNode

                if node.left is curNode:
                    temp2 = curNode.right
                    curNode.left = node.left.left
                    curNode.right = temp2
                    temp2.parent = curNode

                else:
                    curNode.left = node.left
                    temp2 = node.left
                    while temp2.right is not None:
                        temp2 = temp2.right
                    temp2.parent.right = None

                curNode.parent = node.parent

                if node.value > node.parent.value:
                    node.parent.right = curNode

                elif node.value < node.parent.value:
                    node.parent.left = curNode
                '''

        else:
            return False

    def printPreOrderKeys(self, root=None, lista=[]):
        if root:
            lista.append(root.key)
            self.printPreOrder(root.left, lista)
            self.printPreOrder(root.right, lista)

        return lista

    def printPreOrder(self, root=None, lista=[]):

        if root:
            lista.append(root.value)
            self.printPreOrder(root.left, lista)
            self.printPreOrder(root.right, lista)

        return lista

    def printInOrder(self, root=None):

        if root:
            self.printInOrder(root.left)
            print(root.value)
            self.printInOrder(root.right)

    def printPostOrder(self, root=None, lista=[]):

        if root:
            self.printPostOrder(root.left)
            self.printPostOrder(root.right)
            print(root.value)
            lista.append(root.value)

        return lista

    def vazia(self):
        if self.root is None:
            return True
        return False

    def __str__(self):
        if self.vazia():
            return None
        return str(self.printInOrder(self.root))

    def __bool__(self):
        if self.vazia:
            return False
        return True

    def __repr__(self):
        if self.vazia():
            return str('BinaryTree()')
        else:
            saida = 'BinaryTree('
            retorno = self.printPreOrder(self.root)
            saida += str(retorno)[1:-1]
            saida += ')'
            return str(saida)

    def __iter__(self):
        class Ponteiro:
            def __init__(self, arvore, passo=0):
                self.arvore = arvore
                self.passo = passo
                self.lista = self.arvore.printPreOrder(self.arvore.root)

            def __next__(self):
                if self.passo >= self.arvore.elementos:
                    raise StopIteration
                value = self.lista[self.passo]
                self.passo += 1

                return value
        return Ponteiro(self)

    def reiniciar(self):
        postOrder = self.printPostOrder(self.root)
        postOrder = postOrder[0:len(postOrder)-1]
        for i in range(len((postOrder))):
            self.remove(postOrder[i])
        self.remove(self.root.value)

    def __getitem__(self, indice):
        try:
            if indice >= self.elementos:
                raise IndexError
            else:
                valoresDosNos = self.printPreOrder(self.root)
                return self.search(valoresDosNos[indice])

        except IndexError:
            print(
                'ERRO !\nVocê inseriu um índice maior que a quantidade de itens da lista')

    def __setitem__(self, indice, novoValor):
        try:
            if indice >= self.elementos:
                raise IndexError
            else:
                valoresDosNos = self.printPreOrder(self.root)
                nodo = self.search(valoresDosNos[indice])
                nodo.value = novoValor

        except IndexError:
            print(
                'ERRO !\nVocê inseriu um índice maior que a quantidade de itens da lista')

    def __delitem__(self, indice):
        try:
            if indice >= self.elementos:
                raise IndexError
            else:
                valoresDosNos = self.printPreOrder(self.root)
                self.remove(valoresDosNos[indice])

        except IndexError:
            print(
                'ERRO !\nVocê inseriu um índice maior que a quantidade de itens da lista')

    def __contains__(self, key):
        listaDeChaves = self.printPreOrderKeys(self.root)

        for i in listaDeChaves:
            if key == i:
                return True

        return False

    def chaves(self):
        todasAsChaves = self.printPreOrderKeys(self.root)
        for i in todasAsChaves:
            print(i)

    def valores(self):
        todosOsValores = self.printPreOrder(self.root)
        for i in todosOsValores:
            print(i)
