"""CIS 211 Winter 2015
   Haomin He 
   Project 4: Building GUIs with Tk

   2. Write a program that computes the monthly payment on a loan. The payment
   is a function of the loan amount, the annual rate, and the number of years
   to pay off the loan.

   I also tried Extra Credit Ideas, in the file called paymentEC.py.

   You should be able to find formulas that will compute any one of the loan
   attributes given values for the other three. For example, given the interest
   rate, loan amount, and payment amount you should be able to calculate the
   number of years before the loan is paid off. Modify your program so it fills
   in any one of the boxes if the other three have been filled in.
   
"""
import tkinter as tk
from math import log, pow

def calculate():
    readamount = amount.get()
    readrate = rate.get()
    readyears = years.get()
    readmonpay = payment.get()
    if (len(readamount) > 0 and len(readrate) > 0
        and len(readyears) > 0 and len(readmonpay) == 0):
        #To calculate the payment, first compute a value r: as r = rate/100/12
        r = float(readrate) / 100 / 12
        amount_ = float(readamount)
        years_ = float(readyears)

        #value p as: p = 12 * years.
        p = 12 * years_
        
        #Then the payment is:
        monthly_payment = (r * amount_) / (1 - (1 + r)**(-p))

        payment.delete(0, tk.END)
        payment.insert(0, "{:.2f}".format(monthly_payment))

    elif (len(readamount) > 0 and len(readrate) > 0
        and len(readmonpay) > 0 and len(readyears) == 0):
        r = float(readrate) / 100 / 12
        amount_ = float(readamount)
        monpay = float(readmonpay)

        negp = log(1-(r*amount_)/monpay, 1 + r)

        p = -negp

        years_ = p / 12

        years.delete(0, tk.END)
        years.insert(0, "{:.2f}".format(years_))


    elif (len(readamount) > 0 and len(readmonpay) > 0
        and len(readyears) > 0) and len(readrate) == 0:
        amount_ = float(readamount)
        years_ = float(readyears)
        monpay = float(readmonpay)

        N = 12 * years_

        q = (log(1 + (1/N)) / log(2))

        amt1 = pow((1 + (monpay/amount_)),1/q)
        amt2 = pow(amt1-1,q)

        rate_ = 1200 * (amt2 - 1)

        rate.delete(0, tk.END)
        rate.insert(0, "{:.2f}".format(rate_))



    elif (len(readmonpay) > 0 and len(readrate) > 0
        and len(readyears) > 0) and len(readamount) == 0:
        r = float(readrate) / 100 / 12
        years_ = float(readyears)
        monpay = float(readmonpay)

        p = 12 * years_
        
        amount_ = (monpay * (1 - (1 + r)**(-p))) / r

        amount.delete(0, tk.END)
        amount.insert(0, "{:.2f}".format(amount_))
        

root = tk.Tk()  

#Entry 1
amountLabel = tk.Label(root, text = "Loan Amount:")
amountLabel.grid(row = 0, column=0, sticky=tk.W, padx = 20, pady = 30)
amount = tk.Entry(root, bd = 5)
amount.grid(row = 0, column = 1, padx = 20)

#Entry 2
rateLabel = tk.Label(root, text = "Interest Rate:")
rateLabel.grid(row = 1, column=0, sticky=tk.W, padx = 20, pady = 30)
rate = tk.Entry(root, bd = 5)
rate.grid(row = 1, column = 1, padx = 20)

#Entry 3
yearsLabel = tk.Label(root, text = "Number of Years:")
yearsLabel.grid(row = 2, column=0, sticky=tk.W, padx = 20, pady = 30)
years = tk.Entry(root, bd = 5)
years.grid(row = 2, column = 1, padx = 20)

#Entry 4 
paymentLabel = tk.Label(root, text = "Monthly Payment:")
paymentLabel.grid(row = 3, column=0, sticky=tk.W, padx = 20, pady = 30)
payment = tk.Entry(root, bd = 5)
payment.grid(row = 3, column = 1, padx = 20)

paymentButton = tk.Button(root, text = "Payment", width = 25, command = calculate)
paymentButton.grid(row = 4, column = 0, columnspan = 2, pady = 30)


if __name__ == "__main__":
    root.mainloop()
















