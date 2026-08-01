# Module 2 Practice: Expressions and Variables

# Question 1
# This code is supposed to display the equation 2 + 2 = 4 on the screen,
# but there is an error. Find the error and fix it.

print("2 + 2 = " + str(2 + 2))

# Question 2
# Two friends are eating dinner at a restaurant.
# The bill is $47.28 and they add a 15% tip.
# Calculate the tip, total bill, and each person's share.

bill = 47.28
tip = bill * 15/100
total = bill + tip
share = total / 2

print("Each person needs to pay: " + str(share))

# Question 3
# This code is supposed to divide one number by another so the result is 1,
# and display the result on the screen.

numerator = 10
denominator = 10
result = numerator / denominator
print(result)

# Question 4
# Combine the variables to display the sentence:
# "How do you like Python so far?"

word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(word1 + " " + word2 + " " + word3 + " " + word4 + " " + word5 + " " + word6 + " " + word7)

# Question 5
# What do you call a combination of numbers, symbols, or other values that
# produce a result when evaluated?

# Answer: An expression

expression = 5 * 3 + 2
print(expression)

# Module 2 Practice: Functions

# A function is a reusable block of code.
# It can take arguments (input values), process them, and return a result.

# Example 1: Function with parameters and a return value

def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

print("Example 1: add_numbers")
print(add_numbers(5, 3))
print(add_numbers(10, 20))

# Example 2: Function with a default argument

def greet(name, time_of_day="morning"):
    """Return a greeting using the given name and time of day."""
    return f"Good {time_of_day}, {name}!"

print("\nExample 2: greet")
print(greet("Aisha"))
print(greet("Ravi", "evening"))

# Example 3: Function returning multiple values

def calculate_total(price, tax_rate):
    """Return the tax amount and total cost."""
    tax = price * tax_rate
    total = price + tax
    return tax, total

print("\nExample 3: calculate_total")
tax_amount, total_amount = calculate_total(100, 0.08)
print(f"Tax: {tax_amount}")
print(f"Total: {total_amount}")

# Example 4: Function with no return value

def show_message():
    """Print a message to the screen."""
    print("Python functions help us reuse code.")

print("\nExample 4: show_message")
show_message()

# Explanation:
# - Arguments are the values passed into a function.
# - return sends a result back to the caller.
# - A function can return one value or multiple values.
# - Default arguments let us provide a value in case the caller does not pass one.

# Built-in functions are functions that Python already provides for us.
# User-defined functions are functions we create ourselves.

print("\nBuilt-in function examples:")
print(len("Python"))
print(str(42))
print(int("10"))
print(float("3.5"))

# User-defined function examples:

def square(number):
    """Return the square of a number."""
    return number * number


def area_of_rectangle(length, width):
    """Return the area of a rectangle."""
    return length * width

print("\nUser-defined function examples:")
print(square(4))
print(area_of_rectangle(5, 6))

# Built-in function vs user-defined function:
# - Built-in functions are already available in Python.
# - User-defined functions are created by the programmer using def.
# - Both can accept inputs and produce output.

