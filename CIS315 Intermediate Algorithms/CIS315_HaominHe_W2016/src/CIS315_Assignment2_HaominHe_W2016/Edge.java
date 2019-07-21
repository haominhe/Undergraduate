package CIS315_Assignment2_HaominHe_W2016;

/* CIS315-Assignment2-HaominHe
 * Winter2016
 * 
 * Edge class
 */

public class Edge {
	// private: Controlling Access to members of a Class
	private Node thisN; // current Node
	private Node nextN; // next Node
	
	// constructor
	public Edge(){
		nextN = null; // initialize the next Node to be null
	}
	
	
	// getter functions 
	public Node getCurrentNode(){
		return thisN;
	}
	public Node getNextNode(){
		return nextN;
	}
	
	// check if the graph is empty
	public boolean isEmpty(){
		return thisN == null; // true if it is empty
	}
	
	// add a new value
	public void intsertNode(int newVal){
		Node newNode = new Node(newVal);
		// current node becomes the nextNode of newNode
		newNode.nextNode = thisN;
		thisN = newNode; // current new node points to the old node
	}
	
	// remove the current node
	public int removeNode(){
		Node holdNode;
		holdNode = thisN;
		thisN = thisN.nextNode;
		return holdNode.dataValue;
	}
	
	public void printListValue(){
		Node thisNode;
		thisNode = thisN; // start from the beginning node
		
		while(thisNode != null){ // when the graph is not empty
			System.out.println(thisNode.dataValue);
			thisNode = thisNode.nextNode;
			
		} // while
		
		
	}

}















