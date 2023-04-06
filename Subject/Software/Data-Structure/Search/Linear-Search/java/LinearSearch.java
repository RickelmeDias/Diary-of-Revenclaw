import java.util.Scanner;

public class LinearSearch
{
	public static String search(int array_of_numbers[], int number_to_find) {
		int array_size = array_of_numbers.length;
		
		for (int i=0; i<array_size; i++) {
			if (array_of_numbers[i] == number_to_find) {
				return "True";
			}
		}
		return "False";
	}
    
	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
	    
		int array_of_numbers[] = { 3, 13, 7, 1, 19 };
	    
		System.out.println("What number do you want find?: ");
		int number_to_find = scn.nextInt();

		String isItFind = search(array_of_numbers, number_to_find);
		System.out.println(isItFind);
	}
}
