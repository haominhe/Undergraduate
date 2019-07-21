package Lab_3;


import java.util.Scanner;


/* Haomin He CIS313 Lab3 Fall 2015
 * 
 * a driver class which will contain the main and other functions.
 * 
 * insert, delete and search require an argument which should be separated from the 
 * command by a single whitespace.
 * 
 * Correctly insert a node into, delete a node from and search for a node in a AVL tree. 
 * The program should read in instructions namely : insert, delete, search , exit.
 * 
 * The program should continually accept instructions until exit is entered. On entering 
 * any instruction - the result of the operation should be displayed.
 */

public class AVLDriver {
	// Accept a string from the user. Accept this string using stdin.
	
	public static void main(String[] args) {
		System.out.println("Please create your integer tree:");
		
		Scanner scanner = new Scanner(System.in);
		String[] strs = new String[10];
		AVLTree newTree = new AVLTree();
		
		while(true) {
			String bstInput = scanner.nextLine();
			
			strs = bstInput.split(" ");
			
			try {
				if(strs[0].equals("insert")) {
					int insertnum = Integer.parseInt(strs[1]);
					newTree.insert(insertnum);
					System.out.printf("%d was inserted successfully!\n", insertnum);
				}
				
				
				else if (strs[0].equals("delete")){
					int deletenum = Integer.parseInt(strs[1]);
					newTree.delete(deletenum);
					if(AVLTree.flag){
						System.out.printf("%d deleted successfully!\n", deletenum);					
					} else{						
						System.out.printf("%d does not exist.\n", deletenum);
					}
				}
				
				
				else if (strs[0].equals("search")) {
					int searchnum = Integer.parseInt(strs[1]);
					if(newTree.search(searchnum)){
						System.out.printf("Found %d! \n", searchnum);
					} else {
						System.out.printf("%d does not exist. \n", searchnum);
					}
				}				
				else if(strs[0].equals("exit")) {
					System.out.println("Exiting! \n");
					break;
				}
				
			} catch (NumberFormatException | ArrayIndexOutOfBoundsException ex) {
				System.out.println("insert, delete and search require an argument which "
						+ "should be separated from the command by a single whitespace. ");
				System.out.println("Follow this correct format: operation integer");
			}
			
		}
		scanner.close();
		
	}

}













