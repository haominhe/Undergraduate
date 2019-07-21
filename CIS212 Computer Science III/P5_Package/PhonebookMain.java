package P5_Package;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.util.ArrayList;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class PhonebookMain {
	
	private static ArrayList<PhonebookEntry> thePhonebk = PhonebookSort.readData();
	
	/*
	 * The GUI is unresponsive while sorting, which is because each sorting processes
	 * is started as a result of an event and is therefore executed on the UI thread.
	 * To avoid this issue, run each sorting process on its own thread.
	 * 
	 * Source: http://tutorials.jenkov.com/java-concurrency/creating-and-starting-threads.html
	 */
	Thread selectionthread;
	Thread mergethread;
	
	public static void main(String[] args) {		
		
		/*
		 * A button to call Selection Sort method and report elapsed sorting time in the 
		 * GUI. Clicking the button should report 'Error' if the resulting list is not 
		 * sorted.
		 */
		JFrame mainframe = new JFrame("Assignment 5");
		mainframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		mainframe.setLayout(new BorderLayout());
		mainframe.setPreferredSize(new Dimension(300, 200));
		
		JLabel selectionLabel = new JLabel("0.0");
		JLabel mergeLabel = new JLabel("0.0");
		
		JButton selectionBtn = new JButton("Selection Sort");
		selectionBtn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent ev) {
				Thread selectionthread = new Thread() {
					public void run(){
						long start = System.nanoTime();		
						ArrayList<PhonebookEntry> sortedArrayList = PhonebookSort.SelectionSort(thePhonebk);
						long end = System.nanoTime();
						double elapsed = ((end - start) / 1000000000.0);
						String elapsedString = String.valueOf(elapsed);
						
						if (PhonebookSort.isSorted(sortedArrayList)) {
							selectionLabel.setText(elapsedString);
						} else {
							System.out.println("Error: the resulting list is not sorted.");
						}	
					}
				};
				selectionthread.start();
			} 
		});
		
		
		JButton mergeBtn = new JButton("Merge Sort");
		mergeBtn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent ev) {
				Thread mergethread = new Thread() {
					public void run() {
						long start = System.nanoTime();		
						ArrayList<PhonebookEntry> sortedArrayList = PhonebookSort.MergeSort(thePhonebk);
						long end = System.nanoTime();
						double elapsed = ((end - start) / 1000000000.0);
						String elapsedString = String.valueOf(elapsed);
						
						if (PhonebookSort.isSorted(sortedArrayList)) {
							mergeLabel.setText(elapsedString);
						} else {
							System.out.println("Error: the resulting list is not sorted.");
						}	
					}
				};
				mergethread.start();
			}
		});
		
		JPanel sortPanel = new JPanel();
		sortPanel.setLayout(new GridLayout(2, 2));
		sortPanel.add(selectionBtn);
		sortPanel.add(selectionLabel);
		sortPanel.add(mergeBtn);
		sortPanel.add(mergeLabel);
		
		mainframe.add(sortPanel);
		
		mainframe.pack();
		mainframe.setVisible(true);
		mainframe.setResizable(false);
	}
}






