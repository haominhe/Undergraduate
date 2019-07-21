package P8_Package;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.InetAddress;
import java.net.Socket;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;


public class ClientPrime {
	private static final int PORT = 1235;
	private ObjectInputStream _inputStream;
	private ObjectOutputStream _outputStream;
	private static ArrayList<Integer> _queueClient;
	
	
	Scanner scanner = new Scanner(System.in);
	
	public ClientPrime() {
		System.out.println("Client started!");
		
		Socket socket = null;
		try {
			System.out.println("Creating and connecting Socket.");
			InetAddress localHost = InetAddress.getLocalHost();
			socket = new Socket(localHost, PORT);
			System.out.println("Socket connected, creating streams!");
			
			_outputStream = new ObjectOutputStream(socket.getOutputStream());
			_outputStream.flush();
			
			_inputStream = new ObjectInputStream(socket.getInputStream());
			
			int eachNumber = 0;
			_queueClient = new ArrayList<Integer>();
			
			while(true) {
				
				System.out.println("Enter a number, blank line to quit: ");
				String message = scanner.nextLine();
				
				try {
					if (message.length() == 0) {					
						sendMessage(_queueClient);				
						break;
					} else {
						try{
							eachNumber = Integer.valueOf(message);
							_queueClient.add(eachNumber);
						} catch (NullPointerException ex){
							ex.printStackTrace();
						}
						
						} 
				} catch (InputMismatchException ex) {
						System.out.println("Input error! \n");
						scanner.next();
						}
				}
			
			
			recievePrime();
			
			// Close streams and sockets regardless of whether or 
			// not an exception occurred.  Make sure they were
			// initialized first, though!
			if (_inputStream != null) {
				_inputStream.close();
				}
			if (_outputStream != null) {
				_outputStream.close();
				}
			if (socket != null) {
				socket.close();
				}
			System.out.println("shutting down");	
				
		} catch (IOException ex) {
			ex.printStackTrace();
			}
	}
	
	private void sendMessage(ArrayList<Integer> queueClient) {
		if (_outputStream == null) {
			return;
		}
		try {
			_outputStream.writeObject(queueClient);
			_outputStream.flush();
			
			System.out.println("client sent: " + queueClient); 
			
		} catch (IOException e) {
			System.out.println("write failed with " + e);
		}
	}
		


	private void recievePrime() {
		try { 
			ArrayList<Integer> primenum = new ArrayList<Integer>();
			try {
				primenum = (ArrayList<Integer>) _inputStream.readObject();
				
				System.out.println("client received: " + primenum); 
				
			} catch (ClassNotFoundException e) {
				e.printStackTrace();
			}
			
		}catch (IOException ex) {
				ex.printStackTrace();
		} 
			
	} 

	public static void main(String[] args) {
		new ClientPrime();
	}
}
