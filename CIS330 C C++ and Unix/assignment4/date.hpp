/* Winter2016 CIS330 Assignment4 Part1 Haomin He */
/* Problem 3. Date cipher */
/* date.hpp: Date cipher header file*/

////////////////////////////////////
#ifndef DATE_HPP_
#define DATE_HPP_
/*  we want to inherit from the Cipher class*/
#include "cipher.hpp"
#include <string>

/*
 * An abstract class defining the encryption and decryption
 * interface that is implemented by different concrete
 * encryption strategies.
 * Create a class CaesarCipher that derives from Cipher and implements the 
 * encrypt and decrypt methods for a Caesar cipher. 
 */
 
 /* -Create a class DateCipher that derives from Cipher and implements the encrypt 
and decrypt methods.*/

class DateCipher : public Cipher {
      public: 
              DateCipher(); // constructor 
              virtual ~DateCipher(); // virtual destructor
              
              // Encrypt the text argument and return the encrypted text
	          virtual std::string encrypt( std::string &text );

           	  // Decrypt the text argument and return the decrypted text
              virtual std::string decrypt( std::string &text );   
              
      }; // DateCipher



// A pure virtual destructor is different from other
// pure virtual function in that it must be defined
// (i.e., you have to provide an implementation).


#endif













