#include "SimpleString.hpp"
#include <string>

//Include any other header files as necessary


//Define and implement the SimpleString class methods in this file

//The 2 constructors are defined for you:

SimpleString::SimpleString() {
    this->input = "Default value ";
}

SimpleString::SimpleString(std::string s) {
    this->input = s;
}

//TODO: Define the getter/setter and operator overloading methods
void SimpleString::setString(std::string str) {
     this->input = str;     
     } // set	
     
std::string SimpleString::getString(){
     return this->input;
     } // get

//Operator= : should be very similar to copy constructor. It returns a SimpleString
SimpleString & SimpleString::operator=(const SimpleString & c){
             this->input = c.input;
             return *this;
             } // =
             
/*Operator+ : it concatenates two SimpleStrings together and returns 
SimpleString. Refer to string::append.*/ 
SimpleString & SimpleString::operator+(const SimpleString & c) {
             this->input += c.input;
             return *this;         // return a reference     
             } // +

/* Operator++ : both pre and post increment; it adds a ¡°*¡± character 
to the end of current string. Refer to string::push_back. */
SimpleString & SimpleString::operator++(){
             (this->input).push_back('*');
             return *this;
             } // ++

/*Operator-- : both pre and post decrement; it removes the last character from 
current string. Refer to string::erase or string::pop_back (C+11 only).*/
SimpleString & SimpleString::operator--(){
             this->input.pop_back();
             return *this;
             }// --
             
/*The ostream (<<) and the istream (>>) operators. Simply returns and 
initializes the SimpleString. Note that you should define these operators 
as friend and implement them as functions.*/
std::ostream& operator<<(std::ostream& os, const SimpleString& s){
       os << s.input << std::endl;
       return os;
       } //ostream
    		
            
            
std::istream& operator>>(std::istream& is, SimpleString& c){
       is >> c.input;
       return is;
       } //istream











































