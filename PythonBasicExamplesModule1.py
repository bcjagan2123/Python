"""PythonBasicExamplesModule1.py

Module 1: Basics of Programming and Python
This file contains example code from Module 1 with comments.
"""

# Hello World example
print("Hello, World!")  # Print a message to the screen

# Variables store values that can change
message = "Welcome to Python"
number = 42
pi_approx = 3.14

print(message)
print("number =", number)
print("pi_approx =", pi_approx)

# Basic arithmetic operations
sum_result = number + 8
difference = number - 10
product = number * 2
quotient = number / 3
floor_division = number // 5
remainder = number % 5
power = 2 ** 3

print("sum_result:", sum_result)
print("difference:", difference)
print("product:", product)
print("quotient:", quotient)
print("floor_division:", floor_division)
print("remainder:", remainder)
print("power:", power)

# Using a function to keep code reusable

def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"

print(greet("Student"))

# Simple conditional logic
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Demonstrating a loop and variable updates
count = 1
while count <= 5:
    print("Count is", count)
    count += 1

# Example list and iteration
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# Comments explain code and do not affect execution
# This is a single-line comment

''' 
This is a multi-line comment block. 
Use multi-line comments to describe larger sections of code.
'''

# End of Module 1 examples
