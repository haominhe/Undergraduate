package P6_Package;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Map.Entry;
import java.util.Set;

/*
 * CIS 212   Spring 2015   Assignment 6 Generic Data and Set Structure
 * Haomin He
 * 
 * Building a new generic data structure and Set structure(that maintains the "add" counts
 * of its unique values so that they can be iterated in sorted order with respect to how
 * many times they've been added to the set). 
 * 
 * The Set implementation will be optimized for efficient add/remove/contains over efficient 
 * iteration, based on the assumption that we'll generally be modifying the structure more 
 * often than accessing its values in sorted order.
 */


public class OccurrenceSet <T> implements Set <T>{
	
	// create and maintain a HashMap -> allow you to easily track the integer "add" count for
	// each value in the set
	private HashMap<T, Integer> trackIntegerHashMap = new HashMap();
	
	
	// all methods should function as specified in the Set documentation
	/*
	 * add~O(1) and addAll~O(n) methods will need to keep track of how many times a value has 
	 * been added to the set
	 */
	@Override
	public boolean add(T e) {		
		if (trackIntegerHashMap.containsKey(e)){ // if contain this key, add occurrence by 1
			int OccurrenceCounter = trackIntegerHashMap.get(e);
			OccurrenceCounter += 1;
			trackIntegerHashMap.put(e, OccurrenceCounter);
			
		} else { // if e is a new key, add its first appearance 
			trackIntegerHashMap.put(e, 1);
		}
		return true;
	}
	
		
	@Override
	public boolean addAll(Collection<? extends T> c) {
		for (T eachKey : c) {
			if (trackIntegerHashMap.containsKey(eachKey)){ // if contain this key, add occurrence by 1
				int OccurrenceCounter = trackIntegerHashMap.get(eachKey);
				OccurrenceCounter += 1;
				trackIntegerHashMap.put(eachKey, OccurrenceCounter);
				
			} else { // if eachKey is a new key, add its first appearance 
				trackIntegerHashMap.put(eachKey, 1);
			}
		}
		return true;
	}
	
	
	/*
	 * remove~O(1), removeAll~O(n), and retainAll methods should remove the necessary 
	 * values from the set completely
	 * (i.e. not just decrement their counts)
	 */
	@Override
	public boolean remove(Object o) { 
		// remove the key value pair from the map
		return trackIntegerHashMap.keySet().remove(o);
	}
	
	
	@Override
	public boolean removeAll(Collection<?> c) { 
		// remove the key value pairs from the map
		return trackIntegerHashMap.keySet().removeAll(c);
	}
	
	
	@Override
	public boolean retainAll(Collection<?> c) {
		// removes from this set all of its elements that are not contained in the 
		// specified collection
		for (Object singleKey : c) { 
			if (trackIntegerHashMap.containsKey(singleKey) == false) {
				trackIntegerHashMap.remove((T) singleKey);
			}
		}
		return true;
	}
	
	
	// behave as documented 
	@Override
	public boolean contains(Object o) { // ~O(1)
		return trackIntegerHashMap.containsKey(o);
		// true: has the key value pair, otherwise false
	}
	
	
	// behave as documented 
	@Override 
	public boolean containsAll(Collection<?> c) { // ~O(n)
		return trackIntegerHashMap.keySet().containsAll(c);
		// true: contains all the keys, false otherwise
	}
	
	
	/*
	 * size~O(1) method should return the number of unique values currently in the set
	 * not considering "add" counts
	 */
	@Override
	public int size() { // how many key value pairs
		int uniqueValues = trackIntegerHashMap.size();
		return uniqueValues;
	}
	
	
	/*
	 * clear and isEmpty methods should behave as documented
	 */
	@Override
	public void clear() {
		// Removes all of the mappings from this map. 
		// The map will be empty after this call returns.
		trackIntegerHashMap.clear();
	}
	
	
	@Override
	public boolean isEmpty() {
		// Returns true if this map contains no key-value mappings.
		return trackIntegerHashMap.isEmpty();
	}
	
	
	/* 
	 * The iterator and toArray methods should return an Iterator or array, respectively,
	 * with elements sorted by their "add" counts in ascending order.
	 * We are optimizing for efficient add/remove/contains over iteration, but these
	 * methods should still be O(n lg n). 
	 * The Iterator remove method does not need to remove the element from the set.
	 * Creating a new List and using the Collections sort method.
	 */
	
	@Override
	public Iterator<T> iterator() {
		// an iterator over the elements in key set
		Iterator<T> iterator = trackIntegerHashMap.keySet().iterator();
		ArrayList<T> keysList = new ArrayList<T>();
		while (iterator.hasNext()) {
			T theKey = iterator.next();
			keysList.add(theKey); // an array of the keys
		} 
		// an iterator over the keys elements in this list in proper sequence
		return keysList.iterator();
	}
	
	
	// Indicates that the named compiler warnings should be suppressed in the 
	// annotated element 
	@SuppressWarnings({ "rawtypes" })
	private LinkedList valueComparison( HashMap<T, Integer> aMap ) {
		
		HashMap<T, Integer> keyValueMap = aMap;
		// the key value pair entry of the HashMap
		LinkedList<HashMap.Entry<T, Integer>> keyValueEntry = 
				new LinkedList<HashMap.Entry<T, Integer>>(keyValueMap.entrySet());
		
		// sort the keys based on their appearance count values
		Collections.sort(keyValueEntry, new Comparator<HashMap.Entry<T, Integer>> () {

			@Override
			public int compare(Entry<T, Integer> o1, Entry<T, Integer> o2) {
				/* compareTo:
				 * the value 0 if this Integer is equal to the argument Integer; 
				 * a value less than 0 if this Integer is numerically less than the 
				 * argument Integer; and a value greater than 0 if this Integer is 
				 * numerically greater than the argument Integer 
				 */
				int comparisonNumber = ((Integer)o1.getValue()).compareTo((Integer)o2.getValue());
				return comparisonNumber;	
			}	
		});
		
		// sorted keys of the HashMap
		LinkedList<T> sortedKeyValueEntry = new LinkedList<T>();
		
		for (int i = 0; i < keyValueEntry.size(); ++i) {
			T sortkey = (T) keyValueEntry.get(i).getKey();
			sortedKeyValueEntry.add(sortkey);
		}
		return sortedKeyValueEntry;
	}
	

	@Override
	public Object[] toArray() {
		// change the sorted keys to array
		return valueComparison(trackIntegerHashMap).toArray();
	}

	
	@Override
	public <T> T[] toArray(T[] a) {
		// change the sorted keys to array
		return (T[]) valueComparison(trackIntegerHashMap).toArray();
	}
	
	
	/*
	 * toSring prints the elements in the list in sorted order
	 * O(n lg n)
	 */
	public String toString() {
		// string representation of the sorted keys
		return valueComparison(trackIntegerHashMap).toString();
		
	}
	
	
	
	/*
	 * Extra Credit: Implement your own Iterator class to be returned by the iterator
	 * method above. Implement the remove method of the Iterator such that the current 
	 * value is removed from the set
	 * 
	 * Calling remove() on an iterator returned by the set's iterator() method will 
	 * actually remove the key from the map and not just from the data structure 
	 * used to create the iterator
	 */
	public class OwnIterator<T> implements Iterator<T> {
		Iterator<T> anIterator;
		ArrayList<T> aSet;
		int trackIndex = 0;
		
		
		public OwnIterator() {  
			aSet = new ArrayList(trackIntegerHashMap.keySet());
		}   // an array list contains all the keys in the map

		
		@Override
		public boolean hasNext() {
			trackIndex += 1; // increment the counter
			if (trackIndex >= aSet.size()) {
				return false; // false: out of the index
			} 
			return true;
		}

		
		@Override
		public T next() {
			trackIndex += 1; // increment the counter
			// the element at the specified position in this list
			T aSetValue = aSet.get(trackIndex);
			if (aSetValue != null) { 
				return (T) trackIntegerHashMap.get(aSetValue);
				// Returns the value to which the specified key is mapped
			}
			return null;
		}
		
		
		@Override 
		public void remove() {
			// the element at the specified position in this list
			T aSetValue = aSet.get(trackIndex);
			if (aSetValue != null) {
				// Removes the element at the specified position in this list
				aSet.remove(trackIndex); 
				// Removes the mapping for the specified key from this map if present
				trackIntegerHashMap.remove(aSetValue);
			}
		}	
	}
}
























