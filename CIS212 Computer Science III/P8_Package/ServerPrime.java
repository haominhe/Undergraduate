package P8_Package;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;


/*
 * CIS 212 Spring 2015 Assignment 8
 * Haomin He 
 * 
 * The goal is to gain experience with network programming, specifically with sockets in 
 * Java. Develop a server and client simultaneously, which is an important skill in itself.
 * The client will allow the user to enter an arbitrary list of integers to be sent to 
 * the server. The server will then return a list of integers containing only the prime 
 * numbers in the original list. 
 * 
 * Create two classes, one for client and one for server. Each class will need a main 
 * method so that both classes can be executed
 * 
 * Implement client to prompt the user to enter a list of integer. Send the list of integers
 * to the server, and then print the list of prime integers received.
 * 
 * Implement server to wait for a socket connection. When a socket is accepted, read a list
 * of integers, remove the integers that are not prime, and then send the list of remaining 
 * integers back to the client. Server can shut down after completing this process and does
 * not need to support multiple sequential connections. 
 */

public class ServerPrime {
	private static final int PORT = 1235;
	private static ArrayList<Integer> _queueServer;
	private static ObjectOutputStream _outputStream = null;
	private static ObjectInputStream _inputStream = null;
	
	@SuppressWarnings("unchecked")
	public static void main(String[] args) {
		try {
			System.out.println("Creating server socket");
			ServerSocket serverSocket = new ServerSocket(PORT);
			Socket _socket = null;
			
			_queueServer = new ArrayList<Integer>();	
			
			System.out.println("waiting for connection..");
			_socket = serverSocket.accept();
			System.out.println("accepted connection");
			
			_outputStream = new ObjectOutputStream(_socket.getOutputStream());
			_outputStream.flush();
		
			_inputStream = new ObjectInputStream(_socket.getInputStream());
			
		
			try {
				_queueServer = (ArrayList<Integer>) _inputStream.readObject();
			} catch (ClassNotFoundException e) {
				e.printStackTrace();
			}
			System.out.println("Server received: " + _queueServer); 
			showPrimeNumber(_queueServer);
			
			_inputStream.close();
			_outputStream.close();
			_socket.close();	
			
			System.out.println("shutting down");

		} catch (IOException ex) {
			ex.printStackTrace();
		}		
	} // end of main

	
	private static void showPrimeNumber(ArrayList<Integer> aQueue) {
		ArrayList<Integer> primeNumbers = new ArrayList<Integer>();
		try {
			for (int each : aQueue){
				if (isPrime(each)) {
					primeNumbers.add(each);
					
				}
			}
			_outputStream.writeObject(primeNumbers);
			_outputStream.flush();
			
			
		} catch (IOException e) {
			System.out.println("write failed with " + e);
		}
		
	}
	

	private static boolean isPrime(int eachnum) {
		if (Math.abs(eachnum) == 2) {
			return true;
		}
		if (eachnum % 2 == 0) {
			return false;
		}
		
		for (int i = 3; i*i <= eachnum; i += 2){
			if (eachnum % i == 0) {
				return false;
			}
		}
		return true;
	}
}
