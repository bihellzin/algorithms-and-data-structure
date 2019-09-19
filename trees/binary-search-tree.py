class Node:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left
        self.parent = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, newNode):
        if self.root is None:
            self.root = newNode

        else:
            node = self.root
            while newNode.parent is None:
                if newNode.value < node.value:
                    if node.left is None:
                        node.left = newNode
                        newNode.parent = node
                        break
                    node = node.left

                elif newNode.value > node.value:
                    if node.right is None:
                        node.right = newNode
                        newNode.parent = node
                        break
                    node = node.right

                elif newNode.value == node.value:
                    print('Value already put in the tree')
                    break

    def search(self, value):
        node = self.root
        if value == node.value:
            return node.value

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
            # No child case
            if node.right is None and node.left is None:
                if node.parent.right == node:
                    node.parent.right = None
                    node.parent = None
                else:
                    node.parent.left = None
                    node.parent = None

            # 2 children case
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

            # 1 child case
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

        else:
            return False

    def printPreOrder(self, root):

        if root:
            print(root.value)

            self.printPreOrder(root.left)
            self.printPreOrder(root.right)

    def printInOrder(self, root):

        if root:
            self.printInOrder(root.left)
            print(root.value)
            self.printInOrder(root.right)

    def printPostOrder(self, node=None):

        if root:
            self.printPostOrder(root.left)
            self.printPostOrder(root.right)
            print(root.value)

if __name__ == '__main__':
    arvre = BinaryTree()
    no12 = Node(12)
    no5 = Node(5)
    no3 = Node(3)
    no1 = Node(1)
    no7 = Node(7)
    no8 = Node(8)
    no9 = Node(9)
    no11 = Node(11)
    no15 = Node(15)
    no17 = Node(17)
    no20 = Node(20)
    no18 = Node(18)
    no13 = Node(13)
    no14 = Node(14)
    no16 = Node(16)


    arvre.insert(no12)
    arvre.insert(no5)
    arvre.insert(no3)
    arvre.insert(no1)
    arvre.insert(no7)
    arvre.insert(no9)
    arvre.insert(no8)
    arvre.insert(no11)
    arvre.insert(no15)
    arvre.insert(no17)
    arvre.insert(no13)
    arvre.insert(no14)
    arvre.insert(no20)
    arvre.insert(no18)
    arvre.insert(no16)

    print(arvre.printPostOrder(arvre.root))
