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
            if node.right is None and node.left is None:
                if node.parent.right == node:
                    node.parent.right = None
                    node.parent = None
                else:
                    node.parent.left = None
                    node.parent = None

            elif node.right is not None and node.left is not None:
                pass

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
        
if __name__ == '__main__':
    arvre = BinaryTree()
    no2 = Node(2)
    no4 = Node(4)
    no1 = Node(1)
    no3 = Node(3)
    #no6 = Node(6)
    #no8 = Node(8)


    arvre.insert(no2)
    arvre.insert(no4)
    arvre.insert(no1)
    arvre.insert(no3)
    #arvre.insert(no6)
    #arvre.insert(no8)
    arvre.remove(4)
    print(arvre.root.right.value)
