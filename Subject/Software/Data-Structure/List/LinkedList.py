class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

class LinkedList:
    def __init__(self):
        self._size = 0
        self._head = None
        self._back = None

    def append(self, element):
        node = Node(element)
        if self._head is None:
            self._head = node
            self._back = node 
        else:
            self._back._next = node
            self._back = self._back._next
        self._size += 1

    def print(self):
        node = self._head
        if node is not None:
            while node is not None:
                print(node._data)
                node = node._next
    
    def search(self, element):
        node = self._head
        if node is not None:
            while node is not None:
                if node._data is element:
                    return print(True)
                node = node._next
            return print(False)
        
    def insert(self, element, position):
        if position > self._size:
            return print("position not exists")
        newNode = Node(element)
        if position == 0:
            node = self._head
            newNode._next = node
            self._head = newNode
        elif position == self._size:
            node = self._back
            node._next = newNode
            self._back = newNode
        else:
            node = self._head
            while position-1 > 0:
                node = node._next
                position -= 1
            newNode._next = node._next
            node._next = newNode
        self._size += 1
    
    def delete(self, element):
        node = self._head
        if node is not None:
            while node is not None and node._next._data is not element:
                node = node._next
            node._next = node._next._next

    def sort(self):
        if self._size <= 1:
            return print("Cannot sort this list")
            
        


ll = LinkedList()

print("====")
ll.append(5)
ll.append(12)
ll.append(3)
ll.print()

print("====")
ll.insert(19, 0)
ll.print()

print("====")
ll.delete(5)
ll.print()

print("====")
ll.sort()
ll.print()