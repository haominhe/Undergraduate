package Lab_1;
/* Haomin He CIS313 Lab1
 * 
 * a standard queue data structure, supporting: enqueue(), dequeue(),
 * and isEmpty()
 */

public class Queue {
	//Queue is first-in, first-out
	private Node QueueNode_front;
	private Node QueueNode_back;
	
	//initialization 
	public Queue() {
		//beginning queue is empty
		QueueNode_front = null; 
		QueueNode_back = null;
	}
	
	
	public void enqueue(Node enqNode) {
		Node newlastNode;		// new added element
		newlastNode = new Node(enqNode.data, enqNode.next);
		
		if (isEmpty()) { // if empty, only one value adds to the queue
			QueueNode_front = QueueNode_back = newlastNode;
		} else { // add the new element at the end
			QueueNode_back.next = newlastNode;
			QueueNode_back = newlastNode;
		}		
	}
	
	
	public char dequeue() {
		char deqvalue;
		
		if (isEmpty()) {
			System.out.print("Nothing to dequeue, the queue is empty");
			return deqvalue = 0;
			
		} else { // get the value from the front
			deqvalue = QueueNode_front.data;
			QueueNode_front = QueueNode_front.next;
			// 1st element is removed, so set the front pointer to the
			// 2nd element
			
			// check if it is empty, if so, make the last Node null
			if(isEmpty()) {
				QueueNode_back = null;
			}
			return deqvalue;
		}		
	}
	
	
	public boolean isEmpty() {
		return QueueNode_front == null;
	}
}
