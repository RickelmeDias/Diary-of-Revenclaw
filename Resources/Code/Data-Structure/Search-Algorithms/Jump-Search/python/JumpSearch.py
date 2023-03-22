# import math 

class Search:
  def __init__(self, array_of_numbers):
    self.array_of_numbers = array_of_numbers

  def jump_search(self, number_to_find):
    array_size=len(self.array_of_numbers)
    stepSize=int(array_size**(1/2)) # int(math.sqrt(array_size))
    start=0
    end=stepSize

    while end < array_size - 1 and array_of_numbers[end] <= number_to_find:
        start = end
        end = end + stepSize
        if end > array_size - 1:
            end = array_size - 1

    while end >= start:
        if array_of_numbers[end] == number_to_find:
            return True
        end-=1

    return False

array_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
search = Search(array_of_numbers)
number_to_find = int(input('What number do you want find?: '))
print(search.jump_search(number_to_find))