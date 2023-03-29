class Search:
  def __init__(self, array_of_numbers):
    self.array_of_numbers = array_of_numbers

  def binary(self, number_to_find):
    last_pos=len(self.array_of_numbers)-1
    first_pos=0 
    mid=0

    while (first_pos<=last_pos):
        mid = (first_pos + last_pos)//2

        if self.array_of_numbers[mid] == number_to_find:
            return True
        elif self.array_of_numbers[mid] > number_to_find:
            last_pos = mid - 1
        else:
            first_pos = mid + 1
    return False

array_of_numbers = [1, 3, 5, 9, 13]
search = Search(array_of_numbers)
number_to_find = int(input('What number do you want find?: '))
print(search.binary(number_to_find))