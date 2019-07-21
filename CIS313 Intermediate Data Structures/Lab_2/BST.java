package Lab_2;

/* Haomin He CIS313 Lab2 Fall 2015
 * 
 * This lab involves using constructing a Binary Search Tree (BST) of numbers.
 * a standard binary search tree data structure, supporting: insert(), delete(),
 * and search()
 *
 */

public class BST {
	private Node root;
	
	//initialization
	public BST(){
		//beginning tree is empty
		root = null;
	}
	
	// set up a boolean flag 
	static boolean flag = false;
	
	
	// use helper functions within code. (Example delete could use smaller functions which
	// handle each of the cases).
	public void insert(int inValue ){
		root = inHelper(root, inValue);	
		flag = true;
	}

	
	private Node inHelper(Node rootNode, int insertValue) {
		if (rootNode == null) { // first element in the tree
			return new Node(insertValue, null, null);
		} 
		
		else if (insertValue < rootNode.getitsData()){
			// if the value is less than the parent, set it to the left leave 
			rootNode.setitsLeft(inHelper(rootNode.getitsLeft(), insertValue));
			
			return rootNode;
		}
		else { // if the value is greater than the parent, set it to the right leave
			rootNode.setitsRight(inHelper(rootNode.getitsRight(), insertValue));
			
			return rootNode;
		}
		
		
	}
	
	public void delete(int deValue){
		root = deHelper(root, deValue);
		
	}
		
	private Node deHelper(Node rootnode, int deleteValue) {
		// if the tree is empty, there is nothing to delete
		// if the value is not in the tree, flag sets to false
		if (rootnode == null){
			flag = false;
			return null;
		}
		// when tree is not empty
		// when the delete value == the value of the node
		if (deleteValue == rootnode.getitsData()){
			flag = true; // when we find the delete value in the tree
			
			// this node does not has any children
			if (rootnode.getitsLeft() == null && rootnode.getitsRight() == null) {
				return null;
			}
			// this node only has the right child
			else if (rootnode.getitsLeft() == null) {
				return rootnode.getitsRight();
			}
			// this node only has the left child
			else if (rootnode.getitsRight() == null) {
				return rootnode.getitsLeft();
			}
			// this node has both right and left children
			else {
				// get the node's right branch and find the smallest value from it
				int smallVal = findSmall(rootnode.getitsRight());
				// set the node's data equals to the smallest value
				rootnode.setitsData(smallVal);
				// reset the right pointer
				rootnode.setitsRight(deHelper(rootnode.getitsRight(), smallVal));
				return rootnode;
			}
		}
		// when the delete value < the value of the node
		// delete the value from the left branch
		// and reset its left pointer
		else if (deleteValue < rootnode.getitsData()){
			rootnode.setitsLeft(deHelper(rootnode.getitsLeft(), deleteValue));
			return rootnode;
		}
		// when the delete value > the value of the node
		// delete the value from the right branch
		// and reset the right pointer
		else {
			rootnode.setitsRight(deHelper(rootnode.getitsRight(), deleteValue));
			return rootnode;
		}
	}


	// find the node with the smallest value
	// smaller value is always on the left
	private int findSmall(Node anode) {
		// if this node does not have left child
		// itself is the smallest value
		if (anode.getitsLeft() == null) {
			return anode.getitsData();
		}
		// recursive call to find the leftmost/smallest value
		else {
			return findSmall(anode.getitsLeft());
		}
	}


	
	
	
	
	public boolean search(int seValue){
		return seHelper(root, seValue);
	}


	private boolean seHelper(Node root_node, int searchValue) {
		// if the tree is empty, there is nothing to search
		// if not find the required value, the node pointer points to null
		if (root_node == null) {
			flag = false;
			return false;
		}
		// if the node data == searchValue, find the value at the current node
		if (root_node.getitsData() == searchValue){
			flag = true;
			return true;
		}
		// if searchValue < node data, search the left branch via recursive call
		// smaller values are always on the left branch
		else if(searchValue < root_node.getitsData()){
			return seHelper(root_node.getitsLeft(), searchValue);
		}
		// if searchValue > node data, search the right branch via recursive call
		// bigger values are always on the right branch
		else{
			return seHelper(root_node.getitsRight(), searchValue);
		}
		
	}	
	
}



































