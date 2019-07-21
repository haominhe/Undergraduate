package P6_Package;

public class OccurrenceSetMain {

	public static void main(String[] args) {
		
		OccurrenceSet<Integer> intSet = new OccurrenceSet<Integer>();
		intSet.add(1);
		intSet.add(3);
		intSet.add(5);
		intSet.add(5);
		intSet.add(3);
		intSet.add(3);
		intSet.add(3);
		System.out.println(intSet);
		
		OccurrenceSet<String> stringSet = new OccurrenceSet<String>();
		stringSet.add("hello");
		stringSet.add("hello");
		stringSet.add("world");
		stringSet.add("world");
		stringSet.add("world");
		stringSet.add("here");
		System.out.println(stringSet);
		
		System.out.println("------------------------");
		
		stringSet.remove("world");
		System.out.println(stringSet);
		
		stringSet.remove("here");
		System.out.println(stringSet);
	}
}


















