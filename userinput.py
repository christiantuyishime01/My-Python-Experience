#!/bin/usr/env python3

num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

try:
    num1 = int(num1_str)
    num2 = int(num2_str)
except ValueError:
    print("Invalid input. Please enter whole numbers only.")
    exit(1)

result = num1 + num2

print(f"The sum of {num1} and {num2} is {result}.")