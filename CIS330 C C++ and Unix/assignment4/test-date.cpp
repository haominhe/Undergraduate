/* Winter2016 CIS330 Assignment4 Part1 Haomin He */
/* Problem 4. test Date cipher */
/* test-date.cpp: A test program for the Date cipher class */

/*
-Create a test program test-date that uses your new DateCipher class to encrypt 
and decrypt input in a way similar to the example provided in Rot13Cipher and 
the CaesarCipher you implemented in Problem 1, but with different logic in the 
encrypt and decrypt methods. Do not read in a date from standard input, just 
hard-code any date you wish in your main program.

-Modify the Makefile to build an executable including your test-caesar.cpp and 
caesar.cpp files (and any other required files).
 */

#include <iostream>
#include <fstream>

#include "ioutils.hpp"
#include "cipher.hpp"
#include "date.hpp"

int main(int argc, const char *argv[]) {

	IOUtils io;
	io.openStream(argc,argv);
	std::string input, encrypted, decrypted;
	input = io.readFromStream();
	std::cout << "Original text:" << std::endl << input;

	// 2. Test various ciphers

	// Simple Caesar cipher
	DateCipher thisDate;
	encrypted = thisDate.encrypt(input);
	std::cout << "Encrypted text:" << std::endl << encrypted;

	decrypted = thisDate.decrypt(encrypted);
	std::cout << "Decrypted text:" << std::endl << decrypted;

	if (decrypted == input) std::cout << "Decrypted text matches input!" << std::endl;
	else {
		std::cout << "Oops! Decrypted text doesn't match input!" << std::endl;
		return 1;   // Make sure to return a non-zero value to indicate failure
	}

	return 0;
}
