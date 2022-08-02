"""
Create a class that has basic calculating functions.

You can have as many methods as you like but here are few suggestions.
* method to take two numbers and add them and return the sum
* method to take two numbers and subtract the second number from the first number and return the diff
* method to take two numbers and return the multiplication of the two
* method to divide two numbers and return the result (first number divided by second number)

"""


class Calculator(object):
    def __init__(self):
        print("calculator is ready")

    def addition(self, num1, num2):
        print("{} + {} = ".format(num1, num2), num1+num2)

    def subtraction(self, num1, num2):
        print(f"{num1} - {num2} = ", num1-num2)

    def multiplication(self, num1, num2):
        print(num1, "x", num2, "=", num1 * num2)

    def division(self, num1, num2):
        print(num1, "/", num2, "=", num1 // num2)


calc = Calculator()
calc.addition(2, 3)
calc.subtraction(10, 4)
calc.multiplication(3, 5)
calc.division(50, 5)