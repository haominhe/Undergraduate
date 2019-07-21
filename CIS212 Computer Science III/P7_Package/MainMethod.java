package P7_Package;

import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;


/* CIS 212   Assignment 7   Threads 
 * Haomin He
 * 
 * Gain experience working with concurrent programming via multiple threads and thread 
 * synchronization. 
 * An implementation that simulates producer and consumer processes.
 * The simulated consummation process will take far more time to complete than the 
 * production procedure, causing the machine to run out of memory if the threads are not
 * synchronized such that no more than a specified number of units are produced prior to
 * being consumed.  
 * 
 * Execute producer and at least two consumers concurrently. 
 * Shut down the service after starting the two processes.
 */

public class MainMethod {
	
	private static final int QUEUE_SIZE = 1000;

	public static void main(String[] args) {
		
		ArrayBlockingQueue<String> queue = new ArrayBlockingQueue<String>(QUEUE_SIZE);
		
		ProducerClass producer = new ProducerClass(queue);
		ConsumerClass consumer1 = new ConsumerClass(queue);
		ConsumerClass consumer2 = new ConsumerClass(queue);
		
		ExecutorService executor = Executors.newCachedThreadPool();
		executor.execute(consumer1);
		executor.execute(consumer2);
		executor.execute(producer);
		
		executor.shutdown();

	}

}
