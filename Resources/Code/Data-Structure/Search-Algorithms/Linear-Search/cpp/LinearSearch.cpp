#include <iostream>
#include <array>

using namespace std;

int main()
{
    int array_of_numbers[5] = { 3, 13, 7, 1, 19 };  
    int number_to_find = 0;
    
    cout<<"What number do you want find?: ";
    cin>>number_to_find;

    int array_size = sizeof(array_of_numbers)/sizeof(int);

    
    for (int i=0; i < array_size; i++) {
        if (array_of_numbers[i] == number_to_find) {
            cout << "True";
            return 0;
        }
    }
    
    cout<<"False";
    return 0;
}