## Binary Search

![Binary Search Image](../../Assets/Binary-Search-Example-GeeksforGeeks.png)

> Binary Search Example Image from [GeeksForGeeks](https://www.geeksforgeeks.org/binary-search/)

#### How it works?

This is used to search a sorted array by repeatedly dividing the search interval in half.

#### FAQ

**Why is it faster than Linear Search?** Because each comparison reduces the number of possible candidates by a factor of 2.

**So, what is bad in Binary Search?** In the binary search we have a fast searching, but the problem is that the array needs to be sorted!

#### Complexity

Best case O(1):

- Find the element exactly in the middle of the array

Worst case O(log(n)):

- Find the element in the first or last position of an array, or if it not exits.

With these points about the Linear Search is possible to make a pseudocode to find a number that the user input:

#### Pseudocode

```pseudocode
Start
    Declare Array<Integer> array_of_numbers = [1, 3, 5, 9, 13]
    Declare Integer number_to_find = input("What number do you want find?: ")

    Declare Integer last_pos = size(array_of_numbers) - 1
    Declare Integer mid = 0, first_pos = 0

    While first_pos <= last_pos
        mid = (last_pos + first_pos)/2

        If array_of_numbers[mid] == number_to_find
            print True # or return true
            break;
        Else If array_of_numbers[mid] > number_to_find
            last_pos = mid - 1
        Else
            first_pos = mid + 1

    print False # or return false
End
```

#### Algorithm Implementation

You can see this implementation in other language too. Here some implementations that I did:

- [C++ Binary Search](./cpp/BinarySearch.cpp)
- [Java Binary Search](./java/BinarySearch.java)
- [Python Binary Search](./python/BinarySearch.py)
