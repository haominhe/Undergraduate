package CIS315_Assignment2_HaominHe_W2016;

/* CIS315-Assignment2-HaominHe
 * Winter2016
 * 
write a program which will take the description of a series of unweighted directed acyclic 
graphs from standard input and write to standard output three different measures for each 
graph. The measures the program will need to compute are (i) the length of the shortest 
path from node 1 to node n, (ii) the length of the longest path from 1 to n, and 
(iii) the number of distinct paths from 1 to n.
 * 
 * Main function of the graph. Input and output.
 */

import java.util.StringTokenizer;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;


public class graphMain {

	public static void main(String[] args) throws FileNotFoundException {
		
		System.out.println("Please enter the file you want to process: ");
		// a simple text scanner which can parse primitive types and strings using 
		// regular expressions
		Scanner enteredFile = new Scanner(System.in); // read the input file
		
		// advances this scanner past the current line and returns the input that was skipped
		String processFile;
		processFile = enteredFile.nextLine();
		enteredFile.close(); // close the input file
		System.out.println("The file name: " + processFile);
		
		
		File file = new File(processFile); // this is the input file
		Scanner scanFile = new Scanner(file); // utilize scanner properties/methods
		
		
		// get the number of graphs in the file
		int numGraphs = 0;
		numGraphs = Integer.parseInt(scanFile.nextLine()); // read the first number of the file
		
		// need to print out information about each graph
		int n; // graph counter
		for(n = 0; n < numGraphs; ++n){
			// print out the number of graphs
			System.out.println("Graph number: " + (n+1));
			
			// get the number of vertices in the file
			int numVertices = 0;
			numVertices = Integer.parseInt(scanFile.nextLine()); // read the second number of the file
			
			// use adjacency list -> linear time algorithm
			Edge[] adjacencyListEdge;
			adjacencyListEdge = new Edge[numVertices]; // keep track of edges of vertices 
			
			int x;
			for (x = 0; x < numVertices; ++x){
				Edge thisedge = new Edge();
				adjacencyListEdge[x] = thisedge;				
			} // for vertices
			
			
			// get the number of edges in the file
			int numEdges = 0;
			numEdges = Integer.parseInt(scanFile.nextLine()); // read the third number of the file	
			
			int y;
			for (y = 0; y < numEdges; ++y) {
				// allows an application to break a string into tokens
				StringTokenizer strToken = new StringTokenizer(scanFile.nextLine());
				
				// nextToken: returns the next token from this string tokenizer 
				int val1, val2;
				val1 = Integer.parseInt(strToken.nextToken());
				val2 = Integer.parseInt(strToken.nextToken());
				
				int currentVertice = val1 - 1; // read from the file off by one
				adjacencyListEdge[currentVertice].intsertNode(val2);	
			
			} // for edges
			
				
			int short_path, long_path, distinct_path;
			short_path = shortestPath(adjacencyListEdge, numVertices);
			long_path = longestPath(adjacencyListEdge, numVertices);
			distinct_path = distintPathNum(adjacencyListEdge, numVertices);
			
			System.out.println("Shortest path: " + short_path);
			System.out.println("Longest path: " + long_path);
			System.out.println("Number of paths: " + distinct_path + "\n");
			
			
		} // for graphs
		
	
		
		scanFile.close();	

	} // main 
	
	
	
	// find the length of the shortest path from node 1 to node n
	public static int shortestPath(Edge[] edgeLst, int VerticesNum) {
		// process all vertices in topological order. For every vertex being processes,
		// update distances of its adjacent using distance of current vertex
		
		// an array to hold paths
		int[] shoPath = new int[VerticesNum];
		shoPath[0] = 1; // initialization 
		
		int z;
		for(z = 0; z < VerticesNum; ++z) {
			// keep track of the current node
			Node currentNode = edgeLst[z].getCurrentNode();
			
			while(currentNode != null){
				if (shoPath[currentNode.dataValue - 1] == 0 && shoPath[currentNode.dataValue - 1] != 1){
					// if this node's path is zero
					// the path = current path + 1
					shoPath[currentNode.dataValue - 1] = 1 + shoPath[z];
					currentNode = currentNode.nextNode;
					
				} // if 
				else { // skip to the next node
					currentNode = currentNode.nextNode;
				} // else	
			} // while
		} // for
		
		// off by one
		return shoPath[VerticesNum - 1] - 1;
	} // shortestPath
	
	
	
	// the length of the longest path from 1 to n
	public static int longestPath(Edge[] lstEdge, int VerNum) {
		int[] lonPath = new int[VerNum];
		lonPath[0] = 1; // initialize 
		
		int w;
		for(w = 0; w < VerNum; ++w){
			// keep track of the current node
			Node currentNode = lstEdge[w].getCurrentNode();
			while(currentNode != null) {
				// increment the path by one
				lonPath[currentNode.dataValue - 1] = 1 + lonPath[w];
				currentNode = currentNode.nextNode;
			} // while
			
		} // for
		// off by one
		return lonPath[VerNum - 1] - 1;
		
	} // longestPath
	
	
	
	// the number of distinct paths from 1 to n.
	public static int distintPathNum(Edge[] edge_lst, int ver_num) {
		int[] disPathNum = new int[ver_num];
		disPathNum[0] = 1; // initialize
		
		int h;
		for (h = 0; h < ver_num; ++h) {
			Node currentNode = edge_lst[h].getCurrentNode();
			while(currentNode != null) {
				// disPathNum = old paths + new paths
				disPathNum[currentNode.dataValue - 1] = disPathNum[currentNode.dataValue - 1] + disPathNum[h];
				currentNode = currentNode.nextNode;
			} // while
		} // for
		
		return disPathNum[ver_num - 1];
	} // distintPathNum
	
	
	
	
	

} // graphMain










































