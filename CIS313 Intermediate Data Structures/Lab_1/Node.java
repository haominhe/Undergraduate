package Lab_1;
/* Haomin He CIS313 Lab1
 * 
 * a simple Node class containing two public data fields: 
 * char data, Node next
 */

public class Node {
	public char data;
	public Node next;
	
	//initialization 
	public Node(char itsdata, Node itsnext) {
		data = itsdata;
		next = itsnext;
	}
	
	public char getitsData() {
		return data; //retrieve the value
	}

	public void setitsData(char aData) {
		data = aData; //assign the value
	}
	
	public Node getitsNext() {
		return next; //retrieve the next Node
	}
	
	public void setitsNext(Node aNext) {
		next = aNext; //assign the next Node
	}
	

}
