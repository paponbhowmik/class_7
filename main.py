# Q1:  Write a Python program that takes a year as input and determines if it is a leap year or not.
year = int(input("Type your year: "))
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("It's a leap year")
        else:
            print("It's not a leap year")
    else:
        print("It's a leap year")
else:
    print("It's not a leap year")
# Q2: Let’s write a Python program to check whether a number is divisible by 2 and 3.
num = int(input("enter your number: "))
if num%2 ==0:
    if num%3 ==0:
        print("The number is divisible by 2 and 3.")
    else:
        print("The number is divisible by 2, but not divisible by 3.")
else:
    print("The number is not divisible 2")
# Q3: Let’s write a program in Python using nested if else statement to check whether a number is zero, positive, or negative.
num = int(input("Enter your number: "))
if num>=-10:
    if num == 0:
        print("number is zero")
    else:
        print("number is positive")
else:
    print("number is negative")
# Q4: Let’s write a simple Python program to print the first 5 natural numbers by using while loop statement.
a = 1
while a <= 5:
    print(a)
    a+=1
# Q5: Let’s write a Python program to display numbers from 5 to 1 by using while loop statement.
a = 5
while a>= 1:
    print(a)
    a-=1
