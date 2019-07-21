package P7_Package;

import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.TimeUnit;

/*
 * Implements Runnable to simulate the consumer.
 * When executed this process should consume Strings from the queue, keeping track of the 
 * overall max String found (using the String compareTo() method). The process should continue 
 * as long as there are Strings in the queue or the producer hasn't finished (so the consumer
 * does not quit if the queue happens to be empty before the producer finishes). Call 
 * Thread.sleep(10), sleep for 10 ms between each String comparison to ensure that the consumer
 * takes longer to execute than the producer. Print progress once every 1000 Strings consumed.
 * Print total number consumed and the max String found when the process completes. 
 */

public class ConsumerClass implements Runnable {
	
	private final ArrayBlockingQueue<String> _queue;
	
	public ConsumerClass( ArrayBlockingQueue<String> queue) {
		_queue = queue;
	}

	@Override
	public synchronized void run() {
		String maxStr = null;
		int hasConsumend = 0;
		int Strlength = Thread.currentThread().getName().length() - 1;
		String ThreadNumber = Thread.currentThread().getName().substring(Strlength);
		
		// The process should continue as long as there are Strings in the queue or 
		// the producer hasn't finished
		while (_queue.size() != 0 || ProducerClass.flagRunning) {				
			try {				
				// Retrieves and removes the head of this queue, waiting if necessary 
				// until an element becomes available. Wait 10 seconds
				// poll() takes care of both waiting and notifying to wake up
				String takeout = _queue.poll((long) 10, TimeUnit.SECONDS); 
				
				if (takeout == null) { // wait for the producer about 10 seconds, still get nothing
					break;             // means no more elements need to be consumed, break out loop
				}
				
				if (maxStr == null) { // get the first element
					maxStr = takeout;
				}
				
				Thread.sleep(10);
				
				if (takeout.compareTo(maxStr) >= 0) {
					maxStr = takeout;
					// The result is a negative integer if this String object lexicographically precedes
					// the argument string. The result is a positive integer if this String object lexicographically 
					// follows the argument string. The result is zero if the strings are equal
				}
				
				++hasConsumend; // keep track of how many has consumed 
				if (hasConsumend % 1000 == 0) {
					System.out.println("consumer " + ThreadNumber + " consumed: " + hasConsumend);
				}				
				
			} catch (InterruptedException ex) {
				System.out.println(ex);
			}
		}																	
		System.out.println( "consumer " + ThreadNumber + " done consuming! " + hasConsumend + " consumed");		
		System.out.println( "consumer " + ThreadNumber + " max String: " + maxStr);
	}
}
















