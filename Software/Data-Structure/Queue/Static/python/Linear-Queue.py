class LinearQueue:
    def __init__(self, capacity):
        self._capacity = capacity
        self._data = [None] * self._capacity
        self._front = 0
        self._rear = 0

    def enqueue(self, element):
        if self.isFull() or self._rear+1 > self._capacity:
            return "Overflow"       
        else:
            self._data[self._rear] = element
            self._rear += 1

    def dequeue(self):
        if self.isEmpty():
            return "Underflow"
        else:
            removedElement = self._data[self._front]
            self._front += 1
            return removedElement

    def front(self):
        return self._data[self._front]

    def size(self):
        return self._rear - self._front
    
    def isFull(self):
        return self.size() == self._capacity
    
    def isEmpty(self):
        return self.size() == 0


lq = LinearQueue(3)
lq.enqueue(3)
lq.enqueue(5)
lq.enqueue(9)
print(lq.dequeue())
print(lq.dequeue())
print(lq.dequeue())
lq.enqueue(9)
