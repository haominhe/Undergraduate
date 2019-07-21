package Lab_2;

/* Haomin He CIS313 Lab2 Fall 2015
 * 
 * a simple Node class containing three public data fields: int data, Node left, 
 * Node right
 * 
 */

public class Node {
	private int data; //value of this node
	private Node left; //left child of this node
	private Node right; //right child of this node
	
	//initialization 
	public Node (int itsdata, Node itsleft, Node itsright){
		data = itsdata;
		left = itsleft;
		right = itsright;
	}
	
	public int getitsData() {
		return data; //retrieve the value
	}

	public void setitsData(int aData) {
		data = aData; //assign the value
	}
	
	public Node getitsLeft() {
		return left; //retrieve the left Node
	}
	
	public void setitsLeft(Node aLeft) {
		left = aLeft; //assign the left Node
	}
	
	public Node getitsRight() {
		return right; //retrieve the right Node
	}
	
	public void setitsRight(Node aRight) {
		right = aRight; //assign the right Node
	}
	
}
