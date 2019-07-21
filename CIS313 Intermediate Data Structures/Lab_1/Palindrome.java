package Lab_1;
/* Haomin He CIS313 Lab1
 * 
 * a driver class which will contain the main and other functions (example : 
 * is_Palindrome() ). 
 */

import java.util.Scanner;
public class Palindrome {

	public static void main(String[] args) {
		// Accept a string from the user. Accept this string using stdin.
		System.out.print("Please enter a Palindrome (no puctuation) : ");
		Scanner scanner = new Scanner(System.in);
		String PalinInput = scanner.nextLine();
		//call the palindrome checker function 
		is_Palindrome(PalinInput);
	}

	
	public static void is_Palindrome(String checkPalin) {	
		/* A palindrome can be defined as a phrase that reads the same forwards or 
		 * backwards, ignoring all whitespaces and capitalization.
		 */
		String lower = checkPalin.toLowerCase();
		String CheckPalin = lower.replaceAll("\\s+", "");
		
		int Palinlength = CheckPalin.length();
		char[] ArrayPalin = CheckPalin.toCharArray(); //convert string to array
		
		// Test the phrase to check whether it is a palindrome or not, using Stacks and 
		// Queues.
		
		//1.Stack Check
		Stack astack = new Stack();
		for (int i = 0; i < Palinlength; i++) {
			Node pushnode = new Node(ArrayPalin[i], null);
			astack.push(pushnode);	// add at the end		
		}
		String reversePalin1 = "";
		//if the stack is not empty, pop out elements and put them in the reverse order
		while (astack.isEmpty() == false) { 
			reversePalin1 += astack.pop();
		}
		if (CheckPalin.equals(reversePalin1)) { //the phrase equals to itself in the reverse order
			System.out.println("Stack Check: " + CheckPalin + " is a palindrome.");
		} else {
			System.out.println("Stack Check: " + CheckPalin + " is not a palindrome.");
		}
		
		//2.Queue Check
		Queue aqueue = new Queue();
		//Queue is first-in, first-out
		for (int i = Palinlength -1 ; i >= 0; i--) {
			Node enqnode = new Node(ArrayPalin[i], null);
			aqueue.enqueue(enqnode);
		}
		String reversePalin2 = "";
		
		//if the queue is not empty, dequeue out elements and put them in the reverse order
		while (aqueue.isEmpty() == false) {
			reversePalin2 += aqueue.dequeue();
		}
		
		if (CheckPalin.equals(reversePalin2)) {	//the phrase equals to itself in the reverse order		
			System.out.println("Queue Check: " + CheckPalin + " is a palindrome.");
		} else {
			System.out.println("Queue Check: " + CheckPalin + " is not a palindrome.");
		}
	}

}













