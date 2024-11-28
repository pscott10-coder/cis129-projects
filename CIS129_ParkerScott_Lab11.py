excersize 1
----------------------
score = 0


with open('grades.txt', mode='w') as grades:
     # Prompts user for data
     print("Enter students Exam Scores('*' to finish): ")
     # Repeats Program until the sentinal is used
     while  score != '*':
         print("Input score: ")
         score = input()
         if score != "*":
             grades.write(score)
             grades.write("\n")
----------------------
excersize 2
----------------------
counter = 0
total = 0

with open('grades.txt', mode='r') as grades:
        for record in grades:
            total = total + int(record)
            counter = counter + 1
            print(f'{record:<10}')
        average = total / counter
        print(f'Class average is {average:.2f}')
----------------------
excersize 3
----------------------
done = 0

import csv

with open('grades.csv', mode='w', newline='') as grades:
     writer = csv.writer(grades)
     # Prompts user for data
     print("Enter students Exam Scores('done' to finish): ")
     # Repeats Program until the sentinal is used
     while  done != 'done':
         print("Input as follows (firstname,lastname,exam1grade,exam2grade,exam3grade): ")
         firstName = input("Enter first name:")
         lastName = input("Enter last name:")
         g1 = int(input("Enter first grade:"))
         g2 = int(input("Enter second grade:"))
         g3 = int(input("Enter third grade:"))
         
         # Stores data
         writer.writerow([firstName, lastName, g1, g2, g3])
         # 
         print("type 'done' to finish or press Enter to continue: ")
         done = input()
