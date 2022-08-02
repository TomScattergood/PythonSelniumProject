"""
Write a program that takes an integer input and checks if it's even number.
Prints out 'True' if the number is even and 'False' if the number is not even.
"""

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("{} is even".format(number))
else:
    print("{} is odd".format(number))