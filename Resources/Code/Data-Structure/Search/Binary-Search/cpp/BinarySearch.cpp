#include <iostream>

using namespace std;

int main()
{
    int array_of_numbers[5] = { 1, 3, 5, 9, 13 };  
    int number_to_find = 0;
    
    cout<<"What number do you want find?: ";
    cin>>number_to_find;

    int last_pos = sizeof(array_of_numbers)/sizeof(int) - 1;
    int mid = 0, first_pos = 0;

    while (first_pos<=last_pos) {
        mid = (last_pos + first_pos)/2;
        if (array_of_numbers[mid] == number_to_find) {
            cout<<"True";
            return 0;
        }
        else if (array_of_numbers[mid] > number_to_find) {
            last_pos = mid-1;
        }
        else {
            first_pos = mid+1;
        }
    }
        
    cout<<"False";
    return 0;
}
