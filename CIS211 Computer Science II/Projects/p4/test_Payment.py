# Test the Payment app

import payment as app

app.amount.insert(0, "150000")
app.years.insert(0, "30")
app.rate.insert(0, "4.5")

app.button.invoke()

print(app.payment.get())
    
