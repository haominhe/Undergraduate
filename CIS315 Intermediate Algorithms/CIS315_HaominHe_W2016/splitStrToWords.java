package CIS315_Assignment6_HaominHe_W2016;


import java.io.File;
import java.util.Arrays;
import java.util.Scanner;

/* CIS315-Assignment6-HaominHe
 * Winter2016
 * 
There is a string of characters which might have been a sequence of words with all the 
spaces removed, and we want to find a way, if any, in which to insert spaces that 
separate valid English words. For example, theyouthevent could be from ¡°the you the 
vent¡±, ¡°the youth event¡± or ¡°they out he vent¡±. If the input is theeaglehaslande, 
then there¡¯s no such way. Your task is to implement a dynamic programming solution in 
two separate ways:
-iterative bottom-up version
-recursive memoized version

Assume that the original sequence of words had no other punctuation (such as periods), 
no capital letters, and no proper names - all the words will be available in a 
dictionary file¡£

 */

public class splitStrToWords {
	// static: the variable is shared between all instances of this class. Changes from 
	// one instance will reflect on all instances. 
	public static String wordsInDict[] = new String[58114];
	public static String currentWord;
	
	// find valid English word
	public static boolean checkDictionary(String checkWord){
		// The name of the dictionary file should be hardwired in the code. Testing 
		// program on a file named "diction10k.txt"
		File appliedDictionary = new File("diction10k.txt");
		Scanner scanFile;		
		// scan see if the word is in the dictionary, use try catch in case errors happen
		try {
			if(wordsInDict[0] == null) { // if the array is empty, put in words
				int ctr = 0; 
				scanFile = new Scanner(appliedDictionary); // initialize 
				while(scanFile.hasNextLine()) { // go through every word in the dictionary
					// nextLine: advances this scanner past the current line and return the
					// input that was skipped
					String currentWord = scanFile.nextLine(); 
					// returns a copy of the string and omits leading and trailing whitespace
					currentWord = currentWord.trim();
					wordsInDict[ctr] = currentWord; // to fill words in the wordsInDict array	
					
					ctr++; // increment the counter
				} // while	
				Arrays.sort(wordsInDict);
				scanFile.close();
			} // if
			/* binarySearch(): searches the specified array for the specified value using
			 the binary search algorithm. The array must be sorted before making this call.
			 returns the index of the search key if it is contained in the array, else it 
			 returns -1, not found. */
			// sorts the array into ascending numerical order. 
			int found;			
			found = Arrays.binarySearch(wordsInDict, checkWord);						
			if (found > -1) { // if find the word exists in the array
				return true;
			} // if
		} // try
		catch(Exception ex){
			System.out.println("File error.");
		} // catch 
		return false; // did not find the word in the dictionary array 
	} // checkDictionary 
	
	
	
	
	
	public static boolean iterativeBottomUp(String iterStr){
		currentWord = ""; // initialization to empty string
		String inputStr = iterStr; // create a hold variable
		
		int inputStrLength = inputStr.length();
		int counter;
		for(counter = 1; counter <= inputStrLength; counter++){
			if (checkDictionary(inputStr)){ // if this word is in the dictionary
				currentWord += inputStr;    // add it to currentWord
				return true;				
			} // 1st if
			/*String substring(int beginIndex, int endIndex): Returns the substring 
			 * starting from the given index(beginIndex) till the specified 
			 * index(endIndex-exclusive).*/
			if(checkDictionary(inputStr.substring(0, inputStrLength - counter))) {
				// find the very first word that exits in the dictionary
				currentWord += inputStr.substring(0, inputStrLength - counter) + " ";
				// continue search the rest of the inputStr without first qualified word
				inputStr = inputStr.substring(inputStrLength - counter, inputStrLength);
				inputStrLength = inputStr.length();
				counter = 1; // set the counter back to 1 and go back to for loop with
							 // latter part of the string
			} // 2nd if 
		} // for
		
		return false; // if this string is not splittable 
	} // iterativeBottomUp
	
	
	
	
	public static String currentRecWord = "";
	public static boolean recursiveMemoized(String recStr){
		int recStrLength = recStr.length();		
		int count;
		if(checkDictionary(recStr)){ // if this word is in the dictionary
			currentRecWord += recStr; 
			return true;			 // base case
		} // if
		for (count = 1; count < recStrLength; count++){
			// if the very first word is in the dictionary
			if(checkDictionary(recStr.substring(0, recStrLength - count))){
				currentRecWord += recStr.substring(0, recStrLength - count) + " ";
				// check the rest of the string see if there are any qualified words in the string
				return recursiveMemoized(recStr.substring(recStrLength - count, recStrLength));
			} // if
		} // for
		return false;
	} // recursiveMemoized 
	

	
	
	
	public static void main(String[] args) {
		System.out.println("CIS315-Assignment6-HaominHe-Winter2016\n");
		
		Scanner scanner; // scan the string file
		scanner = new Scanner(System.in);
		
		File strFile; // read the string file
		Scanner scanner1;
		int numofLines = 0; // how many lines in this string file
		String currentLine; // the current string that is being tested
		
		try{
			strFile = new File(scanner.nextLine()); // get the file name first 
			scanner.close();
			scanner1 = new Scanner(strFile); // read the file
			numofLines = scanner1.nextInt(); // read how many lines are in the file
			currentLine = scanner1.nextLine(); // get rid of the new line character
			int ctrr;
			for (ctrr = 0; ctrr < numofLines; ctrr++) {
				System.out.printf("phrase number: %d \n", ctrr + 1);
				currentLine = scanner1.nextLine(); // check every line see if it is splittable 
				currentLine = currentLine.trim();
				System.out.println(currentLine  + "\n");
				
				System.out.println("iterative attempt");
				if(iterativeBottomUp(currentLine)){
					System.out.println("YES, can be split");
					System.out.println(currentWord + "\n");
				} // if
				else {
					System.out.println("NO, cannot be split" + "\n");
				} // else
				
				System.out.println("memoized attempt");
				if(recursiveMemoized(currentLine)){
					System.out.println("YES, can be split");
					System.out.println(currentRecWord + "\n");
				} // if
				else {
					System.out.println("NO, cannot be split" + "\n");
				} // else
			} // for
			scanner1.close();
		} catch(Exception ex) {
			System.out.println("Errors happen. Please try again.");
		}
		
		
		
		
	} // main

} // splitStrToWords





















