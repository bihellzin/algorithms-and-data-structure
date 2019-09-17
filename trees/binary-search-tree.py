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

                else:
                    if node.right is None:
                        node.right = newNode
                        newNode.parent = node
                        break
                    node = node.right

if __name__ == '__main__':
    arvre = BinaryTree()
    no2 = Node(2)
    no4 = Node(4)
    no1 = Node(1)
    no3 = Node(3)
    no6 = Node(6)

    arvre.insert(no2)
    arvre.insert(no4)
    arvre.insert(no1)
    arvre.insert(no3)
    arvre.insert(no6)
    print(arvre.root.right.right.value)