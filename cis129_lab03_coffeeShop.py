# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:24:49 2024
By Parker Scott
@author: mail2_s9ys
This code asks the user how much coffee, muffins, cookies, and scones they want, calculates the cost
and prints out a receipt

"""

#  this part will prompt the user to enter the number of coffees, muffins, cookies, and scones
print("***************************************")
print("My Coffee and Muffin and Cookies and Scone Shop")
print("Number of coffees bought?")
numCoffee = input() # 
print("Number of muffins bought?")
numMuffin = input()
print("Number of cookies bought?")
numCookies = input()
print("Number of scones bought?")
numScone = input()
print("***************************************\n\n")

# this part prints the receipt
print("***************************************")
print("My Coffee and Muffins and Cookies and Scone Shop Receipt")

# calculate total coffee cost
print(numCoffee, "Coffee at $5 each: $", "{:.2f}".format(int(numCoffee) * 5.00))
# calculate total muffin cost
print(numMuffin, "Muffins at $4 each: $", "{:.2f}".format(int(numMuffin) * 4.00))
#calculate total cookie cost
print(numCookies, "Cookies at $3 each: $", "{:.2f}".format(int(numCookies) * 3.00))
#calculate total scone cost
print(numScone, "Scone at $4.50 each: $", "{:.2f}".format(int(numScone) * 4.50))

# calculate total tax 
print("6% tax: $ ", "{:.2f}".format(((int(numCoffee) * 5) + (int(numMuffin) * 4) + (int(numCookies) * 3) + (int(numScone) * 4.50)) * 0.06))
print("---------")
# calculate total cost with tax
print("Total: $ ", "{:.2f}".format(((int(numCoffee) * 5) + (int(numMuffin) * 4) + (int(numCookies) * 3) + (int(numScone) * 4.50)) * 1.06))
print("        Thank you for choosing the")
print("My Coffee and Muffins and Cookies and Scone Shop ")
print("***************************************")
