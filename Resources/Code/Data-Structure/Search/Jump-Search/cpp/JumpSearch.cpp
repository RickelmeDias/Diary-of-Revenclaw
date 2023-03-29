#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int array_of_numbers[10] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    int number_to_find = 0;
    
    cout<<"What number do you want find?: ";
    cin>>number_to_find;
    int array_size = sizeof(array_of_numbers)/sizeof(int) - 1;
    int blockSize = pow(array_size, 2), start = 0, end = blockSize;

    while (end < array_size - 1 && array_of_numbers[end] <= number_to_find) {
        start = end;
        end = end + blockSize;
        if (end > array_size - 1) {
            end = array_size - 1;
        }
    }
    
    for (int i = end; i >= start; i--) {
        if (array_of_numbers[end] == number_to_find) {
            cout<<"True";
            return 0;
        }
        end--;
    }
        
    cout<<"False";
    return 0;
}