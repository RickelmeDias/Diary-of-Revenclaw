class Search:
  def __init__(self, array_of_numbers):
    self.array_of_numbers = array_of_numbers

  def linear(self, number_to_find):
    for d in self.array_of_numbers:
      if d == number_to_find:
        return True
    return False

array_of_numbers = [3, 13, 7, 1, 19]
search = Search(array_of_numbers)
number_to_find = int(input('What number do you want find?: '))
print(search.linear(number_to_find))