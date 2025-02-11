"""
Find potential times to meet by finding the available times in common
among a set of agendas.

Authors: Haomin He
Consulted with: Office Hour

Usage: python3 meetme.py 2012.12.1 8:00 17:00  keith.ag mary.ag syamsul.ag
  Arguments are date, begin time, end time, agenda*
    (zero or more agenda input files)

  Each agenda file is a list of appointments.
"""

from agenda import Appt, Agenda
import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find a time we can all meet.")
    parser.add_argument('date', help="Date to check for available times, format like 2012.05.31")
    parser.add_argument('earliest', help="Earliest potential time to start, format like 8:30")
    parser.add_argument('latest', help="Latest potential time to end, format like 18:00")
    parser.add_argument('participant', help="A text file containing an agenda, e.g., 'charles.ag'", 
                         nargs="*", type=argparse.FileType('r'))

    available = Agenda()
    args = parser.parse_args()
    blockspec = args.date + " " + args.earliest + " " + args.latest + "|Available" # begin time & end time => a block
    freeblock = Appt.from_string(blockspec)
    available.append(freeblock) # have one big initial block 

    for f in args.participant: # agenda files
        participant = Agenda.from_file(f)   
        participant = participant.complement(freeblock)
        available = available.intersect(participant) # update available every comparision round
                                                     # uses the 'intersect' method in class 'Agenda.' 

    if len(available) == 0: # check if it is empty
        print("No free times in common")
    else:
        print(available)
    

    
