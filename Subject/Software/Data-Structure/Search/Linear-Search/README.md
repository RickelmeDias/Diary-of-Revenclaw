## Linear Search

![Linear Search Image](../../Assets/Linear-Search-Example-GeeksforGeeks.png)

> Linear Search Example Image from [GeeksForGeeks](https://www.geeksforgeeks.org/linear-search/)

#### How it works?

In the linear search we iterate each element of an array, so we can get two cases when we finding for an element:

#### Complexity

Best case O(1):

- Find the element in the first position of array

Worst case O(n):

- Find the element in the last position of array or this element is not in the array

With these points about the Linear Search is possible to make a pseudocode to find a number that the user input:

#### Pseudocode

```pseudocode
Start
    Declare Array<Integer> array_of_numbers = [3, 13, 7, 1, 19]
    Declare Integer number_to_find = input("What number do you want find?: ")

    Declare Integer array_size = size(array_of_numbers)

    For i = 0; i < array_size; i++
        If array_of_numbers[i] ==  number_to_find
            print True # or return true
            break

    print False # or return false
End
```

#### Algorithm Implementation

You can see this implementation in other language too. Here some implementations that I did:

- [C++ Linear Search](./cpp/LinearSearch.cpp)
- [Java Linear Search](./java/LinearSearch.java)
- [Python Linear Search](./python/LinearSearch.py)
