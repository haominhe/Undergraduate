/*Spring 2015 CIS 212 Assignment 1
 *Student: Haomin He 
 *
 *A Java program which sums a list of positive integers entered by 
 *the user. It repeatedly prompts the user to enter an integer and 
 *use special-case integer values to determine when to print the sum,
 *clear the sum, and quit the application. It may get user input 
 *either from the console or by writing a simple UI.  
 *
 *I also have tried the extra credit.
 */

package P1_Package;

import java.util.Scanner;
import java.util.InputMismatchException;

public class ListIntegerSum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		
		int intnum;
		int total = 0;
		
		System.out.printf("%s%s\n","Enter a positive integer ", "(-1 to print, -2 to reset, -3 to exit):");
		intnum = scanner.nextInt();
		
		while (intnum != -3) {
			try {
				if (intnum >= 0) {			
					System.out.printf("%s%s\n","Enter a positive integer ", "(-1 to print, -2 to reset, -3 to exit):");
					total += intnum;
					intnum = scanner.nextInt();
				} else if (intnum == -1) {
					System.out.printf( "Sum: %d\n", total );
					System.out.printf("%s%s\n","Enter a positive integer ", "(-1 to print, -2 to reset, -3 to exit):");
					intnum = scanner.nextInt();
				} else if (intnum == -2) {
					total = 0;
					System.out.printf("%s%s\n","Enter a positive integer ", "(-1 to print, -2 to reset, -3 to exit):");
					intnum = scanner.nextInt();
				} else if (intnum < -3) {
					System.out.printf("%s%s\n","Enter a positive integer ", "(-1 to print, -2 to reset, -3 to exit):");
					intnum = scanner.nextInt();
				} 
			} catch (InputMismatchException ex){
					System.out.println("Invalid input!");
					scanner.next();
					intnum = 0;
				}
		} 
			
		System.out.printf( "Sum: %d\n", total );	
		
	}

}
