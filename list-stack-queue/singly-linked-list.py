class Node(object):

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList(object):

    def __init__(self):
        self.root = None
        self.size = 0

    def getSize(self):
        return self.size

    def insertEnd(self, newNode):
        if self.root is None:
            self.root = newNode

        else:
            lastNode = self.root

            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
        self.size += 1

    def insertBegin(self, newNode):
        temp = self.root
        self.root = newNode
        self.root.next = temp
        self.size += 1

    def insertSorted(self, newNode):
        if newNode.next is None:
            self.insertEnd(newNode)
            return

        else:
            lastNode = self.root
            temp = self.root.next
            while True:
                if temp.data is newNode.next or temp.next is None:
                    break
                lastNode = temp
                temp = lastNode.next
            lastNode.next = newNode
            newNode.next = temp



    def printList(self):
        if self.root is None:
            print('The list is empty')
            return
        currentNode = self.root
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

def main():
    list = LinkedList()
    fn = Node('John')
    list.insertEnd(fn)
    sn = Node('Ben')
    list.insertEnd(sn)
    tn = Node('Matthew')
    list.insertEnd(tn)

    qn = Node('Gabriel')
    list.insertBegin(qn)

    an = Node('Natan', 'Ben')
    list.insertSorted(an)
    list.printList()

main() 
