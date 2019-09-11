import numpy as np

class Stack(object):
    def __init__(self, size):
        self.stack = np.empty(size, int)
        self.top = -1
        self.size = size

    def emptyStack(self):
        if self.top == -1:
            return True
        else:
            return False

    def popStack(self):
        if self.top == -1:
            print('There is no elements in the stack')
            return
        else:
            self.top -= 1
            return self.stack[self.top+1]

    def fullStack(self):
        if (self.top + 1) == self.size:
            return True
        else:
            return False

    def addStack(self, num):
        if self.fullStack():
            print('The stack is full')
            return False
        else:
            self.stack[self.top+1] = num
            self.top += 1

def main():
    stack = Stack(3)
    stack.popStack()
    print(stack.stack)
    print(stack.emptyStack())
    stack.addStack(2)
    print(stack.stack)
    stack.addStack(32)
    print(stack.stack)

    stack.addStack(5)
    print(stack.fullStack())
    print(stack.stack)
    stack.addStack(4)
    stack.popStack()
    print(stack.top)


main()