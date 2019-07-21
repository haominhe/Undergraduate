package Lab_3;


/* Haomin He CIS313 Lab3 Fall 2015
 * 
 * This lab involves using constructing an AVL Tree of numbers.
 * a standard tree data structure, supporting: insert(), delete(),
 * and search()
 * Extend code in programming assignment 2 to now include a 
 * balancing operations 
 * 
 * AVL tree is a self-balancing binary tree.
 *
 */

public class AVLTree {
	private Node root;
	
	//initialization
	public AVLTree(){
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
		if (rootNode == null) { // leaf element in the tree
			return new Node(insertValue, null, null);
		} 
		
		else if (insertValue < rootNode.getitsData()){
			// if the value is less than the parent, set it to the left leave 
			rootNode.setitsLeft(inHelper(rootNode.getitsLeft(), insertValue));
			
			return makeBalance(rootNode); // make the node balanced, and return it
		}
		else { // if the value is greater than the parent, set it to the right leave
			rootNode.setitsRight(inHelper(rootNode.getitsRight(), insertValue));
			
			return makeBalance(rootNode); // make the node balanced, and return it
		}
		
		
	}
	
	


	public void delete(int deValue){
		root = deHelper(root, deValue);
		
	}
		
	private Node deHelper(Node rootnode, int deleteValue) {
		// if the tree is empty, there is nothing to delete
		// if the value is not in the tree, flag sets to false and return null
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
				return makeBalance(rootnode);
			}
		}
		// when the delete value < the value of the node
		// delete the value from the left branch
		// and reset its left pointer
		else if (deleteValue < rootnode.getitsData()){
			rootnode.setitsLeft(deHelper(rootnode.getitsLeft(), deleteValue));
			return makeBalance(rootnode);
		}
		// when the delete value > the value of the node
		// delete the value from the right branch
		// and reset the right pointer
		else {
			rootnode.setitsRight(deHelper(rootnode.getitsRight(), deleteValue));
			return makeBalance(rootnode);
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
	
	
	
	
	/*
	 * In an AVL tree, the heights of the two child subtrees of any node differ by at 
	 * most one; if any time they differ by more than one, re-balancing is done to restore
	 * this property. Search, insertion, deletion all take O(log n) time in both the average
	 * and worst cases, where n is the number of nodes in the tree prior to the operation.
	 * 
	 * Insertions and deletions may require the tree to be re-balanced by one or more
	 * tree rotations. 
	 */
	
	private int findheight(Node fhrootNode){
		// try to find the height difference between left child and right child
		if (fhrootNode.getitsLeft() == null && fhrootNode.getitsRight() == null){
			return 0; // this node is a leaf and it is balanced 
			
		} else if (fhrootNode.getitsRight() == null) {
			// right child is null, but left child is not -> unbalanced
			return fhrootNode.getitsLeft().getitsHeight();
			
		} else if (fhrootNode.getitsLeft() == null) {
			// left child is null, but right child is not -> unbalanced
			return 0 - fhrootNode.getitsRight().getitsHeight();
			
		} else { // check the height of left and right child, see if they differ by at most one
			return fhrootNode.getitsLeft().getitsHeight() - fhrootNode.getitsRight().getitsHeight();
		}
		
	}
	
	
	
	private Node makeBalance(Node barootNode) {
		// left child is null, but right child is not -> unbalanced
		if (findheight(barootNode) < -1) {
			// just rotate the unbalanced tree once
			if (findheight(barootNode.getitsRight()) == -1){
				barootNode = leftrotation(barootNode);
				}
			else {
				barootNode = leftrotationtwice(barootNode);
			}
					
		}
		// right child is null, but left child is not -> unbalanced
		else if (findheight(barootNode) > 1){
			if(findheight(barootNode.getitsLeft()) == 1 || findheight(barootNode.getitsLeft()) == 0){
				barootNode = rightrotation(barootNode);
			}
			else {
				barootNode = rightrotationtwice(barootNode);
			}
		}
		// this node is a leaf and it is balanced 
		else { // findheight(barootNode) == 0 
			balanceheight(barootNode);			
			return barootNode;
		}
		
		
		balanceheight(barootNode);
		
		return barootNode;
	}




	private void balanceheight(Node bahtrootNode0) {
		if(bahtrootNode0.getitsLeft() != null && bahtrootNode0.getitsRight() == null) {
			// if this node only has left child, height = left_height + 1
			bahtrootNode0.setitsHeight(bahtrootNode0.getitsLeft().getitsHeight() + 1);
			
		} else if(bahtrootNode0.getitsLeft() == null && bahtrootNode0.getitsRight() != null) {
			// if this node only has right child, height = right_height + 1
			bahtrootNode0.setitsHeight(bahtrootNode0.getitsRight().getitsHeight() + 1);		
			
		} else if(bahtrootNode0.getitsLeft() != null && bahtrootNode0.getitsRight() != null) {
			// if this node has both left and right children, choose the bigger height + 1
			bahtrootNode0.setitsHeight(biggerheight(bahtrootNode0) + 1);
			
		} else if(bahtrootNode0.getitsLeft() == null && bahtrootNode0.getitsRight() == null){
			// if this node is a leaf, the height should be 1
			bahtrootNode0.setitsHeight(1);
		}
		
	}


	private int biggerheight(Node biggerhtrootNode) {
		// find the biggest child height from the node
		if(biggerhtrootNode.getitsRight().getitsHeight() > biggerhtrootNode.getitsLeft().getitsHeight()){
			return biggerhtrootNode.getitsRight().getitsHeight();
		} else {
			return biggerhtrootNode.getitsLeft().getitsHeight();
		}
		
	}


	private Node leftrotation(Node barootNode1) {
		Node holdnode = barootNode1.getitsRight(); // hold the original node
		barootNode1.setitsRight(holdnode.getitsLeft());
		holdnode.setitsLeft(barootNode1); // shift to the left
		balanceheight(holdnode);        
        return holdnode;
	}
	
	
	private Node leftrotationtwice(Node barootNode2) {
		// rotation on the right child
		// right rotation first, then do the left rotation 
		barootNode2.setitsRight(rightrotation( barootNode2.getitsRight()));
        return leftrotation( barootNode2 );
	}
	
	
	
	private Node rightrotation(Node barootNode3) {
		Node holdnode = barootNode3.getitsLeft(); // hold the original node
		barootNode3.setitsLeft(holdnode.getitsRight());
		holdnode.setitsRight(barootNode3); // shift to the right
		balanceheight(holdnode);
        return holdnode;				
	}
	
	

	private Node rightrotationtwice(Node barootNode4) {
		// rotation on the left child
		// left rotation first, then do the right rotation 
		barootNode4.setitsLeft(leftrotation( barootNode4.getitsLeft() ));
        return rightrotation( barootNode4 );		
	}
	
	
	
	
	public void traverse() {
	     traversePreOrder(root); 
	}
	
	private void traversePreOrder(Node current) {
	     if(current!=null){ 
	         System.out.print(current.getitsData() + " ");
	         traversePreOrder(current.getitsLeft());
	         traversePreOrder(current.getitsRight());
	} 
	}
	
	

}













