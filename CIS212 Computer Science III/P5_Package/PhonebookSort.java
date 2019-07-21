package P5_Package;
/*
 * CIS 212   Spring 2015   Assignment 5 Selection Sort and Merge Sort
 * Haomin He
 * 
 * Reading data from a file and sorting data using Selection Sort and Merge Sort. This 
 * project will involve building a simple UI to evaluate the efficiency of the two 
 * sorting algorithms. 
 */
 
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;


public class PhonebookSort {
	
	private static ArrayList<PhonebookEntry> datafile = new ArrayList<PhonebookEntry>();
	
	/* First reads data from phone book file into an ArryList of phone book entries.
	 * Differentiate between the name and phone number when sorting and retrieving data, 
	 * so each entry should consist of separate fields for the name and phone number
	 */
	
	public static ArrayList<PhonebookEntry> readData() {
		ArrayList<String[]> alldata = new ArrayList<String[]>();
		
		try {
			FileReader fReader = new FileReader("phonebook.txt");
			BufferedReader bReader = new BufferedReader(fReader); // buffer: speed up the reading
			String linedata = bReader.readLine();
			
			while(linedata != null) { 			// null: end of file
				String[] piecesdata = linedata.split(" ");
				piecesdata[1] = piecesdata[1].replace(",", "");  // remove the comma after each last name.
				alldata.add(piecesdata);
				linedata = bReader.readLine();
			}
			
			for (String[] onedata:alldata) {
				PhonebookEntry singleEntry = new PhonebookEntry(onedata[0], onedata[1], onedata[2]);
				datafile.add(singleEntry);
			}
			
			bReader.close();
			
		} catch (Exception ex) {
			System.err.print(ex.getMessage());
		}
		return datafile;
	}
	
	
	/*
	 * A method that takes an ArrayList of phone book entries as an argument and returns
	 * a sorted copy of the list using Selection Sort to sort alphabetically by phone book
	 * name. The implementation should not modify the input list. 
	 * Source: http://en.wikipedia.org/wiki/Selection_sort
	 * 
	 * "a".compareTo("b") -> -1
	 * The result is a negative integer if this String object lexicographically precedes 
	 * the argument string. The result is a positive integer if this String object 
	 * lexicographically follows the argument string. The result is zero if the strings 
	 * are equal;
	 */
	public static ArrayList<PhonebookEntry> SelectionSort(ArrayList<PhonebookEntry> phone_book_entries) {
		
		ArrayList<PhonebookEntry> entryCopy = new ArrayList<PhonebookEntry>(phone_book_entries);
		int entrySize = phone_book_entries.size();
		int precedeIndex;
		
		for (int i = 0; i < entrySize - 1; ++i) {
			precedeIndex = i;
			for (int j = i + 1; j < entrySize; ++j) {
				if (entryCopy.get(j).getLastName().compareTo(entryCopy.get(precedeIndex).getLastName()) < 0) {
					precedeIndex = j;
				}
			}
			if (precedeIndex != i) { // swap the order
				PhonebookEntry x = entryCopy.get(i);
				entryCopy.set(i, entryCopy.get(precedeIndex));
				entryCopy.set(precedeIndex, x);
			}
		}
		return entryCopy;
	}
	
	
	/*
	 * A method that takes an ArrayList of phone book entries as an argument and returns
	 * a sorted copy of the list using Merge Sort to sort alphabetically by phone book
	 * name. The implementation should not modify the input list.
	 * Source: http://en.wikipedia.org/wiki/Merge_sort
	 */
	public static ArrayList<PhonebookEntry> MergeSort(ArrayList<PhonebookEntry> phone_book_entry) {
		ArrayList<PhonebookEntry> entrycopy = new ArrayList<PhonebookEntry>(phone_book_entry);
		int entrysize = phone_book_entry.size();
		
		// Base Case
		if (entrysize <= 1) {
			return phone_book_entry;
		}
		
		// Progression Case
		int middleIndex = entrysize / 2;
		ArrayList<PhonebookEntry> leftArray = new ArrayList<PhonebookEntry>();
		ArrayList<PhonebookEntry> rightArray = new ArrayList<PhonebookEntry>();
		
		// left hand side of array
		for (int i = 0; i < middleIndex; ++i) {
			leftArray.add(entrycopy.get(i));
		}
		// right hand side of array
		for (int j = middleIndex; j < entrysize; ++j) {
			rightArray.add(entrycopy.get(j));
		}
		
		leftArray = MergeSort(leftArray);
		rightArray = MergeSort(rightArray);
		
		return sortmerge(leftArray, rightArray);
	}
	
	/*
	 * "a".compareTo("b") -> -1
	 * The result is a negative integer if this String object lexicographically precedes 
	 * the argument string. The result is a positive integer if this String object 
	 * lexicographically follows the argument string. The result is zero if the strings 
	 * are equal;
	 */
	private static ArrayList<PhonebookEntry> sortmerge(ArrayList<PhonebookEntry> lefthand,
			ArrayList<PhonebookEntry> righthand) {
		
		ArrayList<PhonebookEntry> sortedPhonebk = new ArrayList<PhonebookEntry>();
		
		while (lefthand.size() > 0 || righthand.size() > 0) {
			if (lefthand.size() > 0 && righthand.size() > 0){
				int comparison = lefthand.get(0).getLastName().compareTo(righthand.get(0).getLastName());
				if (comparison < 0) {
					sortedPhonebk.add(lefthand.get(0));
					lefthand.remove(0);
				} else {
					sortedPhonebk.add(righthand.get(0));
					righthand.remove(0);
				}
				
			} else if (lefthand.size() > 0) {
				sortedPhonebk.add(lefthand.get(0));
				lefthand.remove(0);
				
			} else if (righthand.size() > 0) {
				sortedPhonebk.add(righthand.get(0));
				righthand.remove(0);
			}
		}
				
		return sortedPhonebk;
	}
	
	
	
	/*
	 * A method that takes an ArrayList of phone book entries as an argument and returns
	 * true if the input list is sorted alphabetically by phone book name.
	 * 
	 * "a".compareTo("b") -> -1
	 * The result is a negative integer if this String object lexicographically precedes 
	 * the argument string. The result is a positive integer if this String object 
	 * lexicographically follows the argument string. The result is zero if the strings 
	 * are equal;
	 */
	public static boolean isSorted(ArrayList<PhonebookEntry> maysortedphone) {
		
		boolean flag = false;
		
		for (int i = 0; i < maysortedphone.size() - 1; ++i) {
			int comparison = maysortedphone.get(i).getLastName().compareTo(maysortedphone.get(i + 1).getLastName());
			if (comparison <= 0) {
				flag = true;
			} else {
				flag = false;
				return flag;
			}
		}		
		return flag;
	}
	
}



























