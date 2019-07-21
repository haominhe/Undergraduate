"""
Week 2, Project 2, Part 1. 2014/10/6
Count the number of occurrences of each major code in a file.
Authors: Haomin He 
Credits: Prof. Young and Rickie

Input is a file in which major codes (e.g., "CIS", "UNDL", "GEOG")
appear one to a line. Output is a sequence of lines containing major code
and count, one per major.
"""

import argparse

def count_codes(majors_file):
    """
    This function will take a file of majors, prints in alphabetical
    order the major code, and along with the number of the occurrences.
    Each major code appears on a line by itself. Prints 'File is empty',
    if the file is empty. 
    
    Args:
        majors_file: a file containing a list of major codes.
    Returns:
           nothing
           
    """
    majors = [ ]

    for line in majors_file:
        majors.append(line.strip())

    majors = sorted(majors)

    if len(majors)==0:
        print('File is empty')
        return
    
    count = 0
    major_pre = majors[0]
    majors.append('This is not a valid major code')
    
    for major in majors:
        if major == major_pre:
            count = count + 1
        else:
            print(major_pre, count)
            major_pre = major
            count = 1

    return 
    
        

def main( ):
    """
    Interaction if run from the command line.
    Usage:  python3 counts.py  majors_code_file.txt
    """
    parser = argparse.ArgumentParser(description="Count major codes")
    parser.add_argument('majors', type=argparse.FileType('r'),
                        help="A text file containing major codes, one major code per line.")
    args = parser.parse_args()  # gets arguments from command line
    majors_file = args.majors
    count_codes(majors_file)
    
    
if __name__ == "__main__":
    main( )
