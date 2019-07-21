/* Winter2016 CIS330 Assignment4 Part1 Haomin He */
/* Problem 1. Caesar cipher */
/* caesar.hpp: Caesar cipher header file*/

////////////////////////////////////
#ifndef CAESAR_HPP_
#define CAESAR_HPP_
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
 
class CaesarCipher : public Cipher {
      public: 
              CaesarCipher(); // constructor 
              virtual ~CaesarCipher(); // virtual destructor
              
              // Encrypt the text argument and return the encrypted text
	          virtual std::string encrypt( std::string &text );

           	  // Decrypt the text argument and return the decrypted text
              virtual std::string decrypt( std::string &text );
              
              
      private: // keep track of the shift letter
              int rotation;
      
      }; // CaesarCipher



// A pure virtual destructor is different from other
// pure virtual function in that it must be defined
// (i.e., you have to provide an implementation).


#endif













