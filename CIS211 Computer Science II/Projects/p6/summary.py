"""CIS 211 Project 6: SQLite Databases
   Haomin He
   2. Programming Project

   This program will print a report showing the monthly bill for a customer at
   the Sakila DVD Store. The program will be called from the command line;
   arguments will specify the customer’s last name, a year, and a month. The
   program should fetch the necessary information from the database and print
   a monthly bill for that customer.

   Also have trird Extra Credit Ideas.
   Other Extra Credit Ideas are in the file, called summaryEC.py

"""

from sys import argv
from sqlite3 import *
from datetime import datetime

def records():
    db = connect("sakila211.db")
    if len(argv) == 4:
        customerlast_name = argv[1].capitalize()
        year = argv[2]
        month = argv[3]
        if int(month) < 10:
            month = '0' + str(month)
        time_to_rent = '%' + year + '-' + month + '%'
        curname = db.execute('SELECT first_name, last_name FROM customer WHERE last_name = ?', (customerlast_name,))
        curdate = db.execute('SELECT title, rental_date, return_date, rental_rate, rental_duration \
                          FROM customer JOIN rental USING(customer_id) JOIN \
                          inventory USING(inventory_id) JOIN film USING(film_id) \
                          WHERE last_name = ? AND rental_date LIKE ?', (customerlast_name, time_to_rent))
        
    elif len(argv) == 5:
        customer_idnum = int(argv[2])
        year = argv[3]
        month = argv[4]
        if int(month) < 10:
            month = '0' + str(month)
        time_to_rent = '%' + year + '-' + month + '%'
        curname = db.execute('SELECT first_name, last_name FROM customer WHERE customer_id = ?', (customer_idnum,))
        curdate = db.execute('SELECT title, rental_date, return_date, rental_rate, rental_duration \
                          FROM customer JOIN rental USING(customer_id) JOIN \
                          inventory USING(inventory_id) JOIN film USING(film_id) \
                          WHERE customer_id = ? AND rental_date LIKE ?', (customer_idnum, time_to_rent))

    
    
    
    
    print()
    print("--- Sakila DVD Rentals ---")
    print()
    
    for name1, name2 in curname.fetchall():
        print("Monthly report for {} {}".format(name1, name2))
        
    print()
    bill = 0
    date_format = "%Y-%m-%d %H:%M:%S.%f"
    for film, rent_time, return_time, cost, duration in curdate.fetchall():
        rented = datetime.strptime(rent_time, date_format)
        returned = datetime.strptime(return_time, date_format)
        diff = returned - rented
        bill += cost
        print("{:<30}{:15}{}".format(film, rented.strftime('%m/%d/%Y'), "$" + str(cost)))

        if diff.days > duration:
            bill += cost
            print("{:30}{:15}{}".format("              **late fee", returned.strftime('%m/%d/%Y'), "$" + str(cost)))
            
    print()
    bill = float("{0:.2f}".format(bill))
    print("Monthly total:  {}".format("$" + str(bill)))




if __name__ == "__main__":
    records()


























