class DualStack:
    def __init__(self, capacity):
        self._data = [None] * capacity
        self._capacity = capacity
        self._topStackLeft = 0
        self._topStackRight = capacity-1

    def push(self, element, stackSide):
        if stackSide == 'L':
            if self.isFull():
                print("Overflow")
                return None
            self._data[self._topStackLeft] = element
            self._topStackLeft+=1
        elif stackSide == 'R':
            if self.isFull():
                print("Overflow")
                return None
            self._data[self._topStackRight] = element
            self._topStackRight-=1
        else:
            print('''É necessário escolher uma das duas pilhas que deseja adicionar, 
            a pilha 1 que começa pelo lado esquero ('L'), ou a pilha 2 que começa pelo lado direito ('R')''')

    def pop(self, stackSide):
        if stackSide == 'L':
            if self.isEmpty(stackSide):
                print("Underflow")
                return None
            self._topStackLeft-=1
            return self._data[self._topStackLeft]
        elif stackSide == 'R':
            if self.isEmpty(stackSide):
                print("Underflow")
                return None
            self._topStackRight+=1
            return self._data[self._topStackRight]
        else:
            print('''É necessário escolher uma das duas pilhas que deseja remove, 
            a pilha 1 que começa pelo lado esquero ('L'), ou a pilha 2 que começa pelo lado direito ('R')''')

    def size(self, stackSide):
        if stackSide == 'L':
            return self._topStackLeft
        else:
            return self._capacity - self._topStackRight - 1

    def isEmpty(self, stackSide):
        if stackSide == 'L':
            return self._topStackLeft == 0
        else:
            return self._topStackRight == self._capacity-1
    
    def isFull(self):
        return self.size('L') + self.size('R') == self._capacity


dualstack = DualStack(10)

dualstack.push(0, 'L')
dualstack.push(1, 'L')
dualstack.push(2, 'L')
dualstack.push(3, 'R')

dualstack.push(4, 'R')
dualstack.push(5, 'R')
dualstack.push(6, 'R')
dualstack.push(7, 'R')
dualstack.push(8, 'R')

dualstack.push(9, 'R')
#dualstack.push(8, 'R')
#dualstack.push(8, 'R')