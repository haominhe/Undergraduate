package Lab_1;
/* Haomin He CIS313 Lab1
 * 
 * a standard stack data structure, supporting: push(), pop(),
 * and isEmpty()
 */

public class Stack {
	private Node StackNode;
	
	//initialization 
	public Stack() {
		StackNode = null; //beginning stack is empty
	}
	
	
	public void push(Node pushNode) {
		Node originalNode;
		Node newNode;
		
		//keep the old stack elements in originalNode
		originalNode = StackNode;  
		//add new element on the originalNode, so that the pushNode 
		//becomes a new data at the top, and originalNode becomes 
		//the rest of stack at the bottom 
		newNode = new Node(pushNode.data, originalNode);
		//assignment: update the stack
		StackNode = newNode;
	}
	
	public char pop() {
		char popValue;
		
		if(!isEmpty()) { //the stack is not empty
			popValue = StackNode.data; // pop out the top element data 
			StackNode = StackNode.next;
			//after popping, new stack equals to the rest of stack
			return popValue;
			
		} else { //the stack is empty
			System.out.print("Nothing to pop, the stack is empty");
			popValue = 0;
			return popValue;
		}		
	}
	
	public boolean isEmpty() {
		return StackNode == null;		
	}
	

}
