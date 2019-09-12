class Node(object):

    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt


class LinkedList(object):

    def __init__(self):
        self.root = None
        self.size = 0

    def emptyList(self):
        if self.root is None:
            return True
        else:
            return False

    def get_size(self):
        return self.size

    def insertEnd(self, newNode):
        if self.emptyList():
            self.root = newNode

        else:
            lastNode = self.root

            while True:
                if lastNode.nxt is None:
                    break
                lastNode = lastNode.nxt
            lastNode.nxt = newNode
        self.size += 1

    def insertBegin(self, newNode):
        if self.emptyList():
            self.root = newNode

        else:
            temp = self.root
            self.root = newNode
            self.root.nxt = temp
            self.size += 1

    def insertSorted(self, newNode):
        if newNode.nxt is None:
            self.insertEnd(newNode)
            return

        else:
            lastNode = self.root
            temp = self.root.nxt
            while True:
                if temp.data is newNode.nxt or temp.nxt is None:
                    break
                lastNode = temp
                temp = lastNode.nxt
            lastNode.nxt = newNode
            newNode.nxt = temp

    def removeBegin(self):
        if self.emptyList():
            print('The list is empty')
            return

        else:
            self.root = self.root.nxt

    def removeEnd(self):
        if self.emptyList():
            print('The list is empty')
            return

        else:
            lastNode = self.root
            prev = None
            while lastNode.nxt is not None:
                prev = lastNode
                lastNode = lastNode.nxt
            prev.nxt = None

    def removeNode(self, nodeData):
        if self.emptyList():
            print('The list is empty')
            return

        else:
            currentNode = self.root
            prev = None
            while currentNode.nxt is not None:
                if currentNode.data == nodeData:
                    if prev is not None:
                        prev.nxt = currentNode.nxt

                    else:
                        self.root = currentNode.nxt

                    return True

                prev = currentNode
                currentNode = currentNode.nxt

            return False

    def searchNode(self, nodeData):
        if self.emptyList():
            print('The list is empty')
            return

        else:
            currentNode = self.root
            while currentNode.nxt is not None and currentNode.data != nodeData:
                currentNode = currentNode.nxt

            if currentNode.data == nodeData:
                print('The node you are looking for', currentNode.data, currentNode)
                return True

            elif currentNode.nxt is None:
                print('The node you want to remove does not exist')
                return False

    def printList(self):
        if self.root is None:
            print('The list is empty')
            return
        currentNode = self.root
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.nxt


def main():
    myList = LinkedList()

    fn = Node('John')
    myList.insertEnd(fn)

    tn = Node('Matthew')
    myList.insertEnd(tn)

    sn = Node('Ben')
    myList.insertEnd(sn)

    qn = Node('Gabriel')
    myList.insertBegin(qn)

    an = Node('Natan', 'Ben')
    myList.insertSorted(an)

    myList.printList()
    print('')
    myList.removeEnd()
    myList.printList()
    print('')
    print(myList.root.data)


main()
