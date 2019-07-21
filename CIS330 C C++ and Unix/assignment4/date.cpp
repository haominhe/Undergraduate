/* Winter2016 CIS330 Assignment4 Part1 Haomin He */
/* Problem 3. A date shift cipher */
/* date.cpp: Date cipher */

/*
-Pick a date. An example would be Steven Spielberg's birthday: December 18, 1946.

-Write out that date using numbers and slash marks: 12/18/46.

-Get rid of the slashes, leaving you with a six-digit number that you will use 
to encipher your message: 121846. Assume the message is "I enjoy the movies of 
Steven Spielberg." Under the message, you will write your six digit number over 
and over until you come to an end: 1 21846 121 846121 84 612184 612184612 is the 
secret message. However, it is not done yet.

-Write out the alphabet from left to right.

-Shift each letter of the plain text by the number of spaces indicated by the 
number below it. The letter I shifts one space, making it J; E shifts 2 spaces, 
making it G. Notice in the word message the Y shifts 6 spaces, causing you to 
wrap around back to the beginning of the alphabet, landing at E. Your final 
message would be: "J gorse ujf usbjgt wj yugwmr yqkftfksi".

-To implement decrypt to decipher this message, simply reverse the process: 
write out the numerical code, then go back that many spaces of the alphabet.

-The Date Shift Cipher has an added advantage into it in that it is fairly 
random - you can change the date at any time. This allows you to update your 
system much more easier than other ciphers. Famous dates, such as December 7, 
1941 (12/07/41), should be avoided, however.

-Modify the Makefile to create date.o from your date.cpp file.
*/


#include "cipher.hpp"
#include "date.hpp"


DateCipher::DateCipher() : Cipher() {  
             // nothing else to do in the constructor
             } // constructor 
             
DateCipher::~DateCipher() {
} // destructor

// global variable of the date
int inputDate[6] = {1,2,1,8,4,6};
// declare all possible values
char lowercase[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char uppercase[26] ={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};

// overloaded encrypt method
std::string DateCipher::encrypt(std::string &inputText) {
            std::string text = inputText;
            std::string::size_type len = text.length();
            int counter = 0;
            int holdVal = 0; // keep track of the current position's to value
            int current = 0; // current character index
                    
            for(int i = 0; i != len; ++i) {                    
                    // counter index cannot be greater than the length of the date (6 digits)
                    while(counter > 5) {
                          counter = counter % 6;
                          } // while
                    // get the date digit from inputDate
                    int holdVal = inputDate[counter];
                    
                    // if the current letter is uppercase
                    if(text[i] >= 'A' && text[i] <= 'Z') {
                       current = text[i] - 'A';
                       int tempVal = current + holdVal;
                       text[i] = uppercase[tempVal % 26];
                       counter++;
                       } // if
                    // if the current letter is lowercase   
                    else if(text[i] >= 'a' && text[i] <= 'z') {
                         current = text[i] - 'a';
                         int tempVal = current + holdVal;
                         text[i] = lowercase[tempVal % 26];
                         counter++;                           
                         } // else if
                    // cast integer back to character
                    text[i] = (char)text[i];
                    
                    } // big for
                    
            return text;
            } // encrypt



// Note that a major difference between the ROT13 and other encryption methods 
// is that normally your decrypt method is not going to be the same as your 
// encrypt method.
std::string DateCipher::decrypt(std::string &textInput) {
            std::string text = textInput;
            std::string::size_type len = text.length();
            int counter = 0;
            int holdVal = 0; // keep track of the current position's to value
            int current = 0; // current character index
                    
            for(int i = 0; i != len; ++i) {                    
                    // counter index cannot be greater than the length of the date (6 digits)
                    while(counter > 5) {
                          counter = counter % 6;
                          } // while
                    // get the date digit from inputDate
                    int holdVal = inputDate[counter];
                    
                    // if the current letter is uppercase
                    if(text[i] >= 'A' && text[i] <= 'Z') {
                       current = text[i] - 'A';
                       int tempVal = current - holdVal + 26;
                       text[i] = uppercase[tempVal % 26];
                       counter++;
                       } // if
                    // if the current letter is lowercase   
                    else if(text[i] >= 'a' && text[i] <= 'z') {
                         current = text[i] - 'a';
                         int tempVal = current - holdVal + 26;
                         text[i] = lowercase[tempVal % 26];
                         counter++;                           
                         } // else if
                    // cast integer back to character
                    text[i] = (char)text[i];
                    
                    } // big for
            
            return text;             
                        
            
            } // decrypt











