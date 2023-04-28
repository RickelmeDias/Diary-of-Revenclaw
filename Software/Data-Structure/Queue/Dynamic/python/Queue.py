class Node:

  def __init__(self, data):
    self._data = data
    self._next = None


class Queue:

  def __init__(self):
    self._front = None
    self._rear = None
    self._size = 0

  def enqueue(self, data):
    node = Node(data)    

    if self.isEmpty():
      self._front = node
      self._rear = self._front
    else:
      node = Node(data)
      self._rear._next = node
      self._rear = node

    self._size += 1

  def dequeue(self):
    if self.isEmpty():
      print("Underflow")
      return None
    else:
      self._front = self._front._next
      self._size -= 1

  def getFront(self):
    return self._front._data if not self.isEmpty() else None

  def isEmpty(self):
    return self._front == None
  
queue = Queue()
queue.enqueue(5)
queue.enqueue(3)
print(queue.getFront())
queue.dequeue()
print(queue.getFront())
queue.dequeue()
print(queue.getFront())
