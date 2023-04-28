import math

class Sort:

  def __init__(self, dados):
    self.dados = dados

  def bubbleSort(self):

    ordenado = self.dados.copy()
    c = 0
    i = 0
    while i < len(ordenado):
      j = 0
      flag = False
      while j < len(ordenado) - i - 1:
        c += 1
        if ordenado[j] > ordenado[j + 1]:
          flag = True
          ordenado[j], ordenado[j+1] = ordenado[j+1], ordenado[j]
        j += 1
      if not flag:
        break
      i += 1

    return ordenado, c


dados = [0, 8, 1, 0, 8, 7]
s = Sort(dados)
sort = s.bubbleSort()
print(sort)