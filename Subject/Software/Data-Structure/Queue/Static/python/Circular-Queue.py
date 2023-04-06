class CircularQueue:
    def __init__(self, capacity):
        self._capacity = capacity
        self._data = [None] * self._capacity
        self._front = 0
        self._rear = 0
        self._size = 0

    def enqueue(self, element):
        if self.isFull():
            print("Overflow")
        else:
            if self._rear+1 > self._capacity and not self.isFull():
                self._rear = 0
            self._data[self._rear] = element
            self._rear += 1
            self._size += 1

    def dequeue(self):
        if self.isEmpty():
            return "Underflow"
        else:
            if self._front+1 > self._capacity:
                self._front = 0
            removedElement = self._data[self._front]
            self._front += 1
            self._size -= 1
            return removedElement

    def front(self):
        if self.isEmpty:
            return "Not exists front in an empty queue"
        else: 
            return self._data[self._front]

    def isFull(self):
        return self._size == self._capacity
    
    def isEmpty(self):
        return self._size == 0
    

cq = CircularQueue(3)
cq.enqueue(12)
cq.enqueue(9)
cq.enqueue(3)
cq.enqueue(7)
cq.enqueue(7)
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
cq.enqueue(7)
print(cq.dequeue())