class Deque:
    def __init__(self, capacity):
        self._capacity = capacity
        self._data = [None] * self._capacity
        self._front = 0
        self._rear = 0
        self._size = 0

    def enqueueFront(self, element):
        if self.isFull():
            return print("Overflow")
        pass

    def enqueueRear(self, element):
        if self.isFull():
            return print("Overflow")
        pass

    def dequeueFront(self):
        if self.isEmpty():
            return print("Underflow")        
        pass

    def dequeueRear(self):
        if self.isEmpty():
            return print("Underflow")
        pass

    def isFull(self):
        return self._size == self._capacity
    
    def isEmpty(self):
        return self._size == 0


