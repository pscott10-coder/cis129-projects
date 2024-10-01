# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:24:49 2024
By Parker Scott
@author: mail2_s9ys
This code asks the user how much coffee and muffins they want, calculates the cost
and prints out a receipt

"""

#  this part will prompt the user to enter the number of coffees and muffins
print("***************************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
numCoffee = input() # 
print("Number of muffins bought?")
numMuffin = input()
print("***************************************\n\n")

# this part prints the receipt
print("***************************************")
print("My Coffee and Muffin Shop Receipt")

# calculate total coffee cost
print(numCoffee, "Coffee at $5 each: $", "{:.2f}".format(int(numCoffee) * 5.00))
# calculate total muffin cost
print(numMuffin, "Muffins at $4 each: $", "{:.2f}".format(int(numMuffin) * 4.00))
# calculate total tax 
print("6% tax: $ ", ((int(numCoffee) * 5) + (int(numMuffin) * 4)) * 0.06)
print("---------")
# calculate total cost with tax
print("Total: $ ", "{:.2f}".format(((int(numCoffee) * 5) + (int(numMuffin) * 4)) * 1.06))
print("***************************************")
