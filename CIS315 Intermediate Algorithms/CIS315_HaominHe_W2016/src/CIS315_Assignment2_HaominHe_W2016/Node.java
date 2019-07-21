package CIS315_Assignment2_HaominHe_W2016;

/* CIS315-Assignment2-HaominHe
 * Winter2016
 * 
 * Node class
 */

public class Node {
	int dataValue;
	Node nextNode;
	
	// Constructor
	public Node(int thisdataVal){
		dataValue = thisdataVal;
	}

	public void printDataValue(){
		System.out.println(dataValue);
	}
}
