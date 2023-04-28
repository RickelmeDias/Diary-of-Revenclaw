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

    def pop(self):
        node = self._head
        self._size-=1
        if node._next is None:
            removedNode = node._data
            self._head = None            
            return removedNode
        else:
            while node._next._next is not None:
                node = node._next        
            removedNode = self._back
            self._back = node
            node._next = None
            return removedNode._data

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
    
    def delete(self, position):
        if position == 0:
            self._head = self._head._next
        else:
            node = self._head
            while position > 1:
                node = node._next
                position-=1
            node._next = node._next._next
        self._size-=1
        
        # logic to delete determined value inside list
        #if node is not None:
        #    while node is not None and node._next._data is not element:
        #        node = node._next

    def size(self):
        return self._size

    def sort(self):
        if self._size <= 1:
            return print("Cannot sort this list")
            
        


ll = LinkedList()

print("==| insert 5, 12, 3 |==")
ll.append(5)
ll.append(12)
ll.append(3)
ll.print()

print("==| insert 19 in position 0|==")
ll.insert(19, 0)
ll.print()

print("==| after remove element in position 0 |==")
ll.delete(0)
ll.print()

print("==| after sort |==")
ll.sort()
ll.print()

print("==| pop |==")
print(ll.pop())

print("==| after pop |==")
ll.print()

print("==| removing last 2 |==")
ll.pop()
ll.pop()
ll.print()

print("==| adding teacher samples |===")
ll.append(5)
ll.append(6)
ll.insert(1,0)
ll.insert(8,2)
ll.print()

print("==| show the size |==")
print("The size is {}".format(ll.size()))


####
#### Exercicios
####
#### Fazer append() - O(1)
#### Fazer pop() - O(1)

#===================================== change the print(linkedlist)
# def __str__(self):
#     atual = self.head
#     s = []
#     while atual != None:
#         s.append(str(atual.valor))
#         atual = atual.next
#     return ','.joing(s)