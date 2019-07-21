"""CIS 211 Project 6: SQLite Databases
   Haomin He
   2. Programming Project Extra Credit Ideas

   This program will print a report showing the monthly bill for a customer at
   the Sakila DVD Store. The program will be called from the command line;
   arguments will specify the customer’s last name, a year, and a month. The
   program should fetch the necessary information from the database and print
   a monthly bill for that customer.

   Also have trird Extra Credit Ideas.

"""

from sys import argv
from sqlite3 import *
from datetime import datetime
import locale


def records():
    db = connect("sakila211.db")
    if len(argv) == 4:
        customerlast_name = argv[1].capitalize()
        year = argv[2]
        month = argv[3]
        if int(month) < 10:
            month = '0' + str(month)
        time_to_rent = '%' + year + '-' + month + '%'
        
    elif len(argv) == 3:  #Make the month parameter optional
        customerlast_name = argv[1].capitalize()
        year = argv[2]
        time_to_rent = '%' + year + '-' + '%'
        
    curname = db.execute('SELECT first_name, last_name FROM customer WHERE last_name = ?', (customerlast_name,))
    curdate = db.execute('SELECT title, rental_date, return_date, rental_rate, rental_duration \
                          FROM customer JOIN rental USING(customer_id) JOIN \
                          inventory USING(inventory_id) JOIN film USING(film_id) \
                          WHERE last_name = ? AND rental_date LIKE ?', (customerlast_name, time_to_rent))
    
    curinfo = db.execute('SELECT address, postal_code, email, store_id FROM customer JOIN address USING(address_id) \
                          WHERE last_name = ?', ((customerlast_name,))) #Fetch the customer’s address and other information
    
    
    
    
    print()
    print("--- Sakila DVD Rentals ---")
    print()
    
    for name1, name2 in curname.fetchall():
        print("Monthly report for {} {}".format(name1, name2))
    for add1, add2, mail, store in curinfo.fetchall():
        print("Customer address & email: {}, {}".format(add1 + ' ' + add2, mail))
    curstore = db.execute("SELECT address FROM address WHERE address_id = ?", (store,))
    print("Store Address: {}".format(curstore.fetchall()[0][0])) #Determine which store the customer shops at
    
    print()

    locale.setlocale( locale.LC_ALL, '' )
    
    #print the rental dates and currency using the locale settings on your computer.
    bill = 0
    date_format = "%Y-%m-%d %H:%M:%S.%f"
    for film, rent_time, return_time, cost, duration in curdate.fetchall():
        rented = datetime.strptime(rent_time, date_format)
        returned = datetime.strptime(return_time, date_format)
        diff = returned - rented
        bill += cost
        print("{:<30}{:15}{}".format(film, rented.strftime('%b %d %Y'), str(locale.currency(cost))))

        if diff.days > duration:
            bill += cost
            print("{:30}{:15}{}".format("              **late fee", returned.strftime('%b %d %Y'), str(locale.currency(cost))))

    print()
    bill = float("{0:.2f}".format(bill))
    bill = locale.currency(float(bill))
    
    print("Monthly total:  {}".format(bill))
    ###The locale works perfectly fine on Mac terminal, it prints out extra #s because the Windows command line
    ###on my PC
    



if __name__ == "__main__":
    records()


























