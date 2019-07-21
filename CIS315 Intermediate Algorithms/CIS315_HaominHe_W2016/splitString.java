import java.util.*;
import java.FileNotFoundException;

public class splitString {
	static Set<String> dictionary = new HashSet<String>();

	public static void loadDicitionary(String dictionaryFile) {
		File inFile = new File(dictionaryFile);

		try {
			Scanner sc = new Scanner(inFile);
			String line;
			while (sc.hasNext()) {
				line = sc.next();
				dictionary.add(line.trim());
			}
			sc.close();
		}
		catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}	

	
	public static void main(String[] args) {
		loadDicitionary("diction10k.txt");
		System.out.println("Word a:" + dictionary.contains("a"));

	}
}