# -*- coding: utf-8 -*-
"""
Module 4 Lab-4
Parker Scott
Created on Mon Oct  7 20:34:50 2024

This code takes asks the user for the monthly sales amount
and the sales increase, and calculates the bonus amount

@author: mail2_ngwkk5e
"""

# declare local variables
monthlySales = 0  # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount = 0  # employee bonus amount
salesIncrease = 0  # percent of sales increase
prompt = "Please input the monthly sales: " # prompt will be a string literal
# This code gets the monthly sales
monthlySales = float(input(prompt))
# include code to get the Increase in Sales
prompt = "Please input the percent of sales increase: " # prompt will be a string literal
salesIncrease = float(input(prompt))
salesIncrease = salesIncrease / 100


# This code determines the storeAmount bonus
if monthlySales >= 110000:
 storeAmount = 6000
elif(monthlySales >= 100000):
 storeAmount = 5000
elif(monthlySales >= 90000):
 storeAmount = 4000
elif(monthlySales >= 80000):
 storeAmount = 3000
else:
    storeAmount = 0


# include code to get the Increase in Sales
if salesIncrease >= 0.05:
 empAmount = 75
elif(salesIncrease >= 0.04):
 empAmount = 50
elif(salesIncrease >= 0.03):
 empAmount = 40
else:
    empAmount = 0

# This code prints the bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if (storeAmount == 6000 ) and (empAmount == 75):
		print('Congrats! You have reached the highest bonus amount possible! ')
