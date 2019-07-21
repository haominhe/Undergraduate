#include "SimpleString.hpp"
#include <iostream>
#include <cstdlib>

//Include any libraries as necessary
// Call: g++ -std=c++11 main.cpp SimpleString.cpp

int main(int argc, const char *argv[])
{
    SimpleString s1("Hello ");
    SimpleString s2("World!");
    SimpleString s3;
     
   //Here is some sample usage of the functions that you're
   //implementing; uncomment the lines to test your code.

    std::cout << s1.getString() << std::endl; //Hello
    std::cout << s2.getString() << std::endl; //World!
    s3 = s1 + s2;
    s2 = s1;
    

    //Now write some simple code or print statements to test out
    //the remaining overloaded operators.
    std::cout << s1.getString() << std::endl; 
    std::cout << s2.getString() << std::endl; 
    std::cout << s3.getString() << std::endl;
    
    ++s3; ++s3;
    std::cout << s3.getString() << std::endl;
    
    --s3;
    std::cout << s3.getString() << std::endl;
    
    
    std::cout << "Using overloaded ostream(<<) " << std::endl;
    std::cout << "s3 = " << s3 << std::endl;
 
    SimpleString s4;
    std::cout << "Enter a string: " << std::endl;
    std::cin >> s4;
    std::cout << "Using overloaded istream(>>) " << std::endl;
    std::cout << "Input string is = " << s4;
    
    
    return 0;
}
