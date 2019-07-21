/* Winter2016 CIS330 Assignment4 Part1 Haomin He */
/* Problem 1. Caesar cipher */
/* caesar.cpp: Caesar cipher */

/*
  -The basic idea in this cipher is that you pick an integer for a key, and 
   shift every letter of your message by the key. 
  -For example, if your message was ¡°hello¡± and your key was 2, ¡°h¡± becomes 
   ¡°j¡±, ¡°e¡± becomes ¡°g¡±, and so on.
  -In this problem, we will use a variant of the standard Caesar cipher where 
   the space character is included in the shifts: space is treated as the letter 
   after ¡°z¡±, so with a key of 2, ¡°y¡± would become ¡± ¡°, ¡°z¡± would become 
   ¡°a¡±, and ¡± ¡± would become ¡°b¡±.
  -Modify the Makefile to create caesar.o from your caesar.cpp file.
*/



#include "cipher.hpp"
#include "caesar.hpp"

// In this problem, key is 2
CaesarCipher::CaesarCipher() : Cipher(), rotation(2) {  
             // nothing else to do in the constructor
             } // constructor 
             
CaesarCipher::~CaesarCipher() {
} // destructor


// overloaded encrypt method
std::string CaesarCipher::encrypt(std::string &inputText) {
            std::string text = inputText;
            std::string::size_type len = text.length();
            
            for(int i = 0; i != len; ++i) {
                    // the uppercase of the input text
                    // characters: A - Z, ASCII values: 65 - 90
                    if(text[i] >= 65 && text[i] <= 90) {
                                text[i] = (text[i] + this->rotation) % 91;
                                if(text[i] < 65){ // if the new value of text[i]
                                                   // is less than 65
                                   text[i] = text[i] + 65;                                            
                                   } // inner if                                
                                } // if
                    
                    // the lowercase of the input text
                    // characters: a - z, ASCII values: 97 - 122
                    else if(text[i] >= 97 && text[i] <= 123) {
                         text[i] = (text[i] + this->rotation) % 124;
                         if(text[i] < 97) {
                            text[i] = text[i] + 97;
                            } // inner if
                         if(text[i] == 123) {
                            text[i] = 32; // this is the space character 
                            } // second inner if
                         } // else if
                         
                    // the space character of the input text
                    // characters: (space), ASCII value: 32
                    else if(text[i] == 32) {
                         if(this->rotation == 0) { // rotation value equals zero
                            text[i] = 32;
                            } // if
                         else {
                            text[i] = 96 + this->rotation; // lowercase number 
                                                           // plus rotation value
                            } // else
                         } // second else if 
                         
                    else {
                         text[i] = text[i]; // nothing changed
                         } // else
            
               } // for
            
            return text;            
            } // encrypt



// Note that a major difference between the ROT13 and other encryption methods 
// is that normally your decrypt method is not going to be the same as your 
// encrypt method.
std::string CaesarCipher::decrypt(std::string &textInput) {
            std::string text = textInput;
            std::string::size_type len = text.length();
            


            
            for(int i = 0; i != len; ++i) {
                    // the uppercase of the input text
                    // characters: A - Z, ASCII values: 65 - 90
                    if(text[i] >= 65 && text[i] <= 90) {
                                text[i] = (text[i] - this->rotation);
                                if(text[i] < 65){ // if the new value of text[i]
                                                   // is less than 65
                                   text[i] = text[i] + 26;                                            
                                   } // inner if                                
                                } // if
                    
                    // the lowercase of the input text
                    // characters: a - z, ASCII values: 97 - 122
                    else if(text[i] >= 97 && text[i] <= 123) {
                         text[i] = text[i] - this->rotation;
                         if(text[i] < 97) {
                            text[i] = text[i] + 27;
                            } // inner if
                         if(text[i] == 123) {
                            text[i] = 32; // this is the space character 
                            } // second inner if
                         } // else if
                         
                    // the space character of the input text
                    // characters: (space), ASCII value: 32
                    else if(text[i] == 32) {
                         text[i] = 'y';
                         } // second else if 
                         
                    else {
                         text[i] = text[i]; // nothing changed
                         } // else
            
               } // for
            
            return text;             
            
            
            
            
            
            
            
            
            
            } // decrypt











