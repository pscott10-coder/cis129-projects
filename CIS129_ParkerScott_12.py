# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 17:59:17 2024

This program asks the user to input pet information then displays that
information. It use oop to do this.

By Parker Scott

@author: mail2_s9ys
"""

# Creates class
class Pet:
    def __init__(self, name, petType, age):
        self.name = name
        self.petType = petType
        self.age = age
        
    # Gets pet name  
    def setName(self):
        print("Enter your pet's name:")        
        self.name = input()
        self.name = self.name.title()
        
    # Gets pet type    
    def setType(self):
        print("Enter your pet's type:")        
        self.type = input()
        self.type = self.type.title()
        
    # Gets pet age    
    def setAge(self):
        print("Enter your pet's age:")        
        self.age = int(input())
        
    # Displays pet name
    def getName(self):
        print("Your pet name:", self.name)
        
    # Displays pet type    
    def getType(self):
        print("Your pet type:", self.type)
        
    # Displays pet age    
    def getAge(self):
        print("Your pet age:", self.age)

# calls the get data functions 
my_pet = Pet('', '', '')
my_pet.setName() 
my_pet.setType() 
my_pet.setAge() 
# calls the display the data functions
print("------------------------")
my_pet.getName() 
my_pet.getType() 
my_pet.getAge() 
