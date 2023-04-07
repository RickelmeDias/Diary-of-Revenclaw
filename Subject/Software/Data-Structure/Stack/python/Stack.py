class Stack:
    def __init__(self, capacity):
        self._data = [None] * capacity
        self.capacity = capacity
        self._size = 0

    def push(self, element):
        if not self.isFull():
            self._data[self._size] = element
            self._size+=1
        else:
            print("Overflow! Nao e possivel adicionar elemento de uma pilha cheia")
            return None

    def pop(self):
        if not self.isEmpty():
            self._size-=1
            return self._data[self._size]
        else:
            print("Underflow! Nao e possivel remover elementos de uma pilha vazia")
            return None

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def isFull(self):
        return self._size == self.capacity
    
stack = Stack(5)

stack.push(1)
print("Pop\t {}".format(stack.pop()))

stack.push(2)
print("Pop\t {}".format(stack.pop()))

stack.push(3)
print("Pop\t {}".format(stack.pop()))
print("Size\t {}".format(stack.size()))