/* CIS 212 Assignment 2  
 * Array and ArrayList, Sparse Array and Dense Array
 * Haomin He
 * 
 * This program prompts the user for an integer array length and a double-precision array
 * density.
 * It also records the amount of time taken to run each of the methods and prints timing 
 * results. 
 */
package P2_Package;

import java.util.Scanner;
import java.util.InputMismatchException;
import java.util.Random;
import java.util.ArrayList;

// After trying different combinations of inputs, sparse array implementations are faster than 
// dense array implementations when the density is low (closer to 0). And the sparse findMax()
// is faster. 
// However, when the density is high (closer to 1), dense array implementations are faster than
// sparse implementations. And the dense array findMax() is faster. 

public class ArrayAndArrayList {		
	
	/* This method takes an integer length and an array density of type double as arguments
	 * and returns a new array of type int representing a dense array. For each entry in 
	 * the array, compare the density with a random number on the range [0.0, 1.0) to 
	 * determine whether or not the entry should be 0. If the entry should be 0, simply 
	 * populate the entry as such. If the entry should be non-zero, populate it with a 
	 * random integer on the range [1, 1000000]. 
	 */
		private static final int MAX_INT = 1000000;
		
		public static int[] createDenseArray(int len, double density) {
			long startTime = System.nanoTime(); // beginning time 
			
			int[] denseArray = new int[len];
			Random random = new Random();
			
			// Math.random() returns a double value x, where 0.0 <= x < 1.0
			for (int i = 0; i < len; ++i) {
				double randomnum = Math.random();
				if (randomnum < density) {
					int randint = random.nextInt(MAX_INT) + 1;
					denseArray[i] = randint;
				}
				
			}
			long estimatedTime = System.nanoTime() - startTime; // time interval 
			System.out.println("createDenseArray() length:" + len + " time: " + estimatedTime);
			return denseArray;
		}
		
	/* This method takes an integer length and an array density of type double as arguments
	 * and returns a new ArrayList representing a sparse array. As above, use the density to
	 * determine whether or not each entry should be 0. If the entry should be non-zero, 
	 * store its index and value in ArrayList.
	 */
		public static ArrayList<int[]> createSparseArray(int len, double density) {
			long startTime = System.nanoTime(); // beginning time
			ArrayList<int[]> sparseArray = new ArrayList<int[]>();
			Random random = new Random();
			
			for (int i = 0; i < len; ++i) {
				double randomnum = Math.random();
				if (randomnum < density) {
					int[] smallArr = new int[2];
					int randint = random.nextInt(MAX_INT) + 1;
					smallArr[0] = i;
					smallArr[1] = randint;
					sparseArray.add(smallArr);
				}
			}
			long estimatedTime = System.nanoTime() - startTime; // time interval 
			System.out.println("createSparseArray() length:" + sparseArray.size() + " time: " + estimatedTime);
			return sparseArray;
		}
		
	/* This method takes an int array as an argument and prints the max value in the array,
	 * along with the index of that value in the array.	
	 */
		public static void findMaxArray(int[] array) {
			long startTime = System.nanoTime(); // beginning time
			int maxnum = 0;
			int maxindex = 0;
			for (int i = 0; i < array.length; ++i) {
				if (array[i] > maxnum) {
					maxnum = array[i];
					maxindex = i;
				}
			}
			long estimatedTime = System.nanoTime() - startTime; // time interval 
			System.out.println("findMax (array): " + maxnum + " at: " + maxindex);
			System.out.println("dense findMax() time: " + estimatedTime);
		}
		
	/* This method takes an ArrayList as an argument and prints the max value in the array,
	 * along with the original index of that value in the array. 
	 */
		public static void findMaxList(ArrayList<int[]> list) {
			long startTime = System.nanoTime(); // beginning time
			int maxnum = 0;
			int maxindex = 0;
			for (int i = 0; i < list.size(); ++i) {
				int index = list.get(i)[0];
				int num = list.get(i)[1];
				if (num > maxnum) {
					maxnum = num;
					maxindex = index;
				}
			}
			long estimatedTime = System.nanoTime() - startTime; // time interval 
			System.out.println("findMax (list): " + maxnum + " at: " + maxindex);
			System.out.println("sparse findMax() time: " + estimatedTime);
		}
		
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int arrayLength = 0;
		double arrayDensity = 0.0;
		boolean checkFlag = true;
		
		do {
			try {
			System.out.println("Please enter array length:");
			arrayLength = scanner.nextInt();
			System.out.println("Enter density:");
			arrayDensity = scanner.nextDouble();
			checkFlag = true;
			} catch (InputMismatchException ex) {
				System.out.println("Unparsable input! Please reenter the values." );
				scanner.next();
				checkFlag = false;
			}
		} while(checkFlag == false);
		
		int[] denseArray = createDenseArray(arrayLength, arrayDensity);
		ArrayList<int[]> sparseArray = createSparseArray(arrayLength, arrayDensity);
		findMaxArray(denseArray);
		findMaxList(sparseArray);
	}
}

