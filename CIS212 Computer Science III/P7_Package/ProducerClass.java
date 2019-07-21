package P7_Package;

import java.util.UUID;
import java.util.concurrent.ArrayBlockingQueue;

/*
 * Implements Runnable to simulate the producer. 
 * When executed, this process should add 10000 random Strings (hint: the UUID class) 
 * to the queue, waiting until there is space in the queue if necessary (using the
 * ArrayBlockingQueue put() method). Print progress once every 1000 Strings produced.
 */

public class ProducerClass implements Runnable{
	
	private final ArrayBlockingQueue<String> _queue;
	public static final int STRING_COUNT = 10000;
	public static boolean flagRunning = true;
	
	public ProducerClass( ArrayBlockingQueue<String> queue) {
		_queue = queue;
	}

	@Override
	public synchronized void run() {
		
		int totalProduced = 0;
		
		for (int i = 1; i < STRING_COUNT + 1; ++i) {
			try {
				// A hint to the scheduler that the current thread is willing 
				// to yield its current use of a processor.
				Thread.yield();
				
				// A randomly generated UUID
				String randomStr = UUID.randomUUID().toString();
				
				// Inserts the specified element at the tail of this queue, waiting for 
				// space to become available if the queue is full.
				_queue.put(randomStr);
				
				// Print progress once every 1000 Strings produced				
				if (i % 1000 == 0) {
					System.out.println( "produced: " + i);
					totalProduced = i;
				}
				
			} catch ( InterruptedException ex) {
				System.out.println(ex);
			}
		} // end of for loop, finish adding String elements
		System.out.println("done producing! " + totalProduced + " produced");
		flagRunning = false;
	}

}





















