package P5_Package;

public class PhonebookEntry {
	private String _phoneNumber;
	private String _firstName;
	private String _lastName;
	
	public PhonebookEntry(String number, String lName, String fName) {
		_phoneNumber = number;
		_firstName = fName;
		_lastName = lName;
	}
	
	public String getNumber(){
		return _phoneNumber;
	}
	
	public String getFirstName(){
		return _firstName;
	}
	
	public String getLastName(){
		return _lastName;
	}
	
	@Override
	public String toString(){
		return _phoneNumber + " " + _firstName + " " + _lastName;
	}
}
