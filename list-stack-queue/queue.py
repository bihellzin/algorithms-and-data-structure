import numpy as np

class Queue(object):
    def __init__(self, size, start = -1):
        self.start = start
        self.end = start
        self.size = size
        self.emptySpace = size
        self.queue = np.empty(size, int)

    def emptyQueue(self):
        if self.emptySpace == self.size:
            return True
        else:
            return False

    def fullQueue(self):
        if self.emptySpace == 0:
            return True
        else:
            return False

    def enqueue(self, num):
        if self.fullQueue():
            print('The queue is full')
            return

        elif self.emptyQueue():
            self.start += 1
            self.queue[self.start] = num
            self.emptySpace -= 1
            self.end += 1

        else:
            self.emptySpace -= 1
            if self.end == self.size - 1:
                self.end = 0
            else:
                self.end += 1
            self.queue[self.end] = num

    def dequeue(self):
        if self.emptyQueue():
            print('The queue is empty')
            return
        else:
            self.emptySpace += 1
            leaving = self.queue[self.start]
            if self.start == self.size - 1:
                self.start = 0
            else:
                self.start += 1
            return leaving 
