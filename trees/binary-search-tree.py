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
                    return value

                elif node.right is None:
                    print('Value not found')
                    return

                node = node.right

            else:
                if node.value == value:
                    return value

                elif node.left is None:
                    print('Value not found')
                    return

                node = node.left

if __name__ == '__main__':
    arvre = BinaryTree()
    no2 = Node(2)
    no4 = Node(4)
    no1 = Node(1)
    no3 = Node(3)
    no6 = Node(6)
    no8 = Node(8)
    no = Node(3)

    arvre.insert(no2)
    arvre.insert(no4)
    arvre.insert(no1)
    arvre.insert(no3)
    arvre.insert(no6)
    arvre.insert(no8)
    arvre.insert(no)
    print(arvre.root.right.left.right)
