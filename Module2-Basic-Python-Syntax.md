# Module 2: Basic Python Syntax

## Python basics

Coding languages are similar to spoken languages in that they have a way to classify words according to their function. In English, words are grouped into nouns, verbs, prepositions, and so on. Python also has basic building blocks that help us write code.

- Variables: store data such as strings, numbers, lists, and dictionaries.

```python
name = "Alice"
age = 25
```

- Keywords: reserved words with special meanings in Python.

```python
if age > 18:
    print("Adult")
```

- Operators: symbols that perform operations on values.

```python
result = 10 + 5
print(result)
```

- Expressions: combinations of values, variables, and operators that produce a result.

```python
total = 10 + 5 * 2
print(total)
```

- Functions: named blocks of code that perform a task and may return a value.

```python
def greet(name):
    return "Hello, " + name

print(greet("Alice"))
```

- Conditional statements: control the flow of the program based on a condition.

```python
score = 85

if score >= 80:
    print("Pass")
else:
    print("Try again")
```

Python will raise syntax errors if keywords or code structure are used incorrectly.

```python
# This will cause a syntax error
if True
    print("Missing colon")
```

## Naming rules and conventions

When assigning names to objects, programmers follow a set of rules and conventions that help keep code readable and consistent. Here are some important naming rules:

- Names cannot contain spaces.
- Names may use a mix of uppercase and lowercase letters.
- Names cannot start with a number, but they may contain numbers after the first character.
- Variable names and function names should be written in snake_case, which means all letters are lowercase and words are separated by underscores.
- Descriptive names are better than short abbreviations because they make the code easier to understand.

```python
student_name = "Aisha"
total_score = 92
```

A good example is `student_name` instead of `sn`. Even when it seems longer at first, descriptive names make code much easier to read later.

> Tim Peters, a Python programmer, wrote a famous set of guiding principles for writing Python code: “Beautiful is better than ugly.”

## Expressions and variables

## Data types

Data types are categories used to classify values in Python. Every value has a type, and Python uses that type to decide what operations are allowed. For example, text values are strings, whole numbers are integers, and true/false values are booleans.

- **String**: text enclosed in quotes

```python
name = "Python"
print(name)
```

- **Integer**: whole numbers

```python
age = 25
print(age)
```

- **Float**: numbers with decimal points

```python
price = 19.99
print(price)
```

- **Boolean**: true or false values

```python
is_active = True
print(is_active)
```

- **List**: an ordered collection of values

```python
numbers = [1, 2, 3, 4]
print(numbers)
```

## Annotating Variables by Type

Type annotation allows you to clearly communicate the argument types and return type of functions in your code. It is like giving yourself and other developers hints about what kind of data a variable is supposed to hold. This has several benefits: it reduces the chance of common mistakes, helps document your code for others to reuse, and allows integrated development environments (IDEs) and other tools to provide better feedback.

In this reading, you will learn more about annotating variables by type and best practices.

### How to annotate a variable

Think of annotating a variable as if you were putting a label on a container, and anything in that container should hold what the label describes. Let’s take a look at an example:

```python
name: str = "Betty"
```

The variable `name` is declared using a colon (`:`) and annotated with the type `str`, indicating that the variable should hold a string value. And it does! `"Betty"` is a string, and we know it is a string because it is enclosed in quotes.

```python
age: int = 34
```

In this example, `age` is the variable, and `int` is the type annotation that tells you and other developers that the value should be an integer.

**Pro tip:** If a function expects a list of integers, annotate it as `List[int]`, not just `List`. Being specific with your types can catch more potential bugs and misunderstandings.

### Dynamic typing

Many languages, such as C# or Java, require you to declare variable types, but Python does not. One of the great things about Python is that the type of a variable can change over time as new values are assigned to it.

```python
a = 3          # a is an integer
a = "Hello world"  # a is now a string
```

Dynamic typing allows programmers to write code more quickly and offers flexibility because you do not have to explicitly declare the type of every variable.

**Note:** Python decides which built-in type a variable is and therefore how it should behave. For more information, refer to the Python documentation on [Built-in types](https://docs.python.org/3/library/stdtypes.html).

### Duck typing

This form of typing comes from the saying, “If it walks like a duck and quacks like a duck, it must be a duck.” Python will infer the variable type at runtime and decide which behaviors are available to the given object.

```python
a = "Hello world"  # looks like a string
```

### Annotating variables with type comments

Another way to annotate variables is to use type comments, where the interpreter ignores the comments.

```python
captain = "Picard"  # type: str
```

**Note:** This way of annotating variables may be useful when you need to know what types belong to which variables but do not want the overhead of using a linter or IDE on that specific variable.

### Annotating variables directly

Let’s use the same example above to annotate a variable directly.

```python
captain: str = "Picard"
```

**Note:** You might hear annotating variables directly called the more “modern” way to annotate a variable.

Another advantage is that you can use automated tools such as linters or mypy to check types and make code more resilient. Most modern IDEs, such as VS Code and JetBrains PyCharm, scan code for type annotations and can use them to help you write better code more quickly.

### How type annotations affect runtime behavior

Any time a library is called or an IDE scans your code, additional computational overhead is required.

**Pro tip:** Be strategic when annotating variables by type. Overusing annotations can add unnecessary overhead.

Type annotation is less common among Python users in data science, as it can be burdensome to manually map data every time a new set of data comes in. On the other hand, when doing object-oriented programming or writing functions, using type annotations becomes extremely important because it helps clarify code when you are dealing with more than just built-in types.

## Expressions, numbers, and type conversions

Expressions are combinations of values, variables, and operators that Python evaluates to produce a result. They are the basic building blocks of computation in any program.

```python
x = 10
y = 5
result = x + y * 2
print(result)
```

In this example, Python evaluates the multiplication first, then adds the result to `x`. This is because Python follows operator precedence rules.

### Numbers in Python

Python supports several numeric types:

- **int**: whole numbers
- **float**: numbers with decimal points
- **complex**: numbers with real and imaginary parts

```python
whole_number = 42
decimal_number = 3.14
complex_number = 2 + 3j

print(type(whole_number))
print(type(decimal_number))
print(type(complex_number))
```

### Common arithmetic operators

```python
addition = 10 + 5
subtraction = 10 - 5
multiplication = 10 * 5
division = 10 / 5
remainder = 10 % 3
power = 2 ** 3

print(addition)
print(subtraction)
print(multiplication)
print(division)
print(remainder)
print(power)
```

### Type conversion

Type conversion, also called casting, allows you to change one data type into another. This is useful when you need to combine values or prepare data for a specific operation.

```python
age = "25"
converted_age = int(age)
print(converted_age + 5)
```

Python provides built-in conversion functions such as:

```python
int("25")
float("3.14")
str(42)
bool(1)
```

### Examples of conversions

```python
number_as_text = "100"
number_as_int = int(number_as_text)
print(number_as_int)

price = 19.99
price_as_int = int(price)
print(price_as_int)

value = 5
value_as_string = str(value)
print(value_as_string)
```

**Note:** Converting a string to an integer or float will fail if the text is not valid for that type. For example, `int("hello")` will raise a `ValueError`.

### Why type conversion matters

Type conversion helps you control how data is used in a program. You may need to convert user input from text to a number before performing math, or convert a number to text when printing a message.

```python
user_input = "12"
score = int(user_input)
print(score + 8)
```

This makes Python programs more flexible and helps prevent errors when working with different kinds of data.

### Key takeaways

Expressions are the heart of Python programming because they combine variables and operators to compute values. Numbers can be represented in different forms, and understanding type conversion helps you work with data safely and correctly. By using the right types at the right time, you can write clearer and more reliable code.

## Implicit vs explicit conversion

As we saw earlier, some data types can be mixed and matched because of implicit conversion. Implicit conversion happens when Python automatically changes one data type into another without us telling it to do so.

```python
x = 10
print(x + 2.5)
```

Here, Python converts the integer `10` to a float so the calculation can work correctly.

By contrast, explicit conversion is when we manually convert one data type into another by calling a conversion function. This is useful when we need a value in a specific form.

```python
number = 42
text = str(number)
print("The number is " + text)
```

In this example, we use `str()` to convert the integer to a string before joining it with text. Without this conversion, Python would raise a type error.

### Short understanding

- **Implicit conversion**: Python does it automatically.
- **Explicit conversion**: we do it manually with functions like `str()`, `int()`, and `float()`.

This is an important concept because it helps us control how data behaves in Python programs.

## Quick Learning Summary: Expressions and Variables

This study guide provides a quick-reference summary of what you learned in this lesson and serves as a guide for the upcoming practice quiz.

In the Expressions and Variables segment, you learned about expressions, variables, and the main data types: strings, integers, and floats. You also learned how to convert values from one data type to another and how to fix common Python errors.

### Terms

- **expression**: a combination of numbers, symbols, or other values that produce a result when evaluated
- **data types**: categories of data such as string, int, float, and Boolean, which define the properties and behaviors of variables
- **variable**: a named place in memory that stores a value that can change during program execution
- **implicit conversion**: when Python automatically converts one data type to another
- **explicit conversion**: when code manually converts one data type to another using a conversion function
- **str()**: converts a value to a string
- **int()**: converts a value to an integer
- **float()**: converts a value to a float

### Variables annotated by type

```python
import typing

# Define a variable of type str
name: str = "Hello, world!"

# Define a variable of type int
count: int = 10

# Define a variable of type float
price: float = 1.23

# Define a variable of type list
numbers: typing.List[int] = [1, 2, 3]

# Define a variable of type tuple
coordinates: typing.Tuple[int, int, int] = (1, 2, 3)

# Define a variable of type dict
scores: typing.Dict[str, int] = {"quiz1": 90, "quiz2": 95}

# Define a variable of type set
unique_numbers: typing.Set[int] = {1, 2, 3}
```

### Example: calculating shared cost

```python
# The following lines assign variables to values and arithmetic expressions.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total / room_guests

print("Each person needs to pay: " + str(share_per_person))
```

This example shows how Python can combine numbers with strings by converting the numeric result to a string before printing it.

### Example: building a full name

```python
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."

print(salutation + " " + first_name + " " + middle_name + " " + last_name + ", " + suffix)
```

This works because all of the values are strings, and the `+` operator joins them together.

### Example: common type error and fix

```python
# This causes a type error because a string and an integer are being combined.
print("5 * 3 = " + str(5 * 3))
```

When you need to combine a number with text, convert the number to a string first:

```python
print("5 * 3 = " + str(5 * 3))
```

### Example: division by zero

```python
numerator = 7
denominator = 0

# This would raise a ZeroDivisionError:
# result = numerator / denominator

# A safe fix is to avoid dividing by zero.
denominator = 1
result = numerator / denominator
print(result)
```

This example shows why it is important to check values before performing operations such as division. In real programs, a denominator may come from user input or data from a file, so validation is important.

### Quick takeaway

Expressions help us calculate values. Variables store those values. Data types define what kind of value a variable can hold. Type conversion helps us change values when needed, and careful coding helps prevent errors like type mismatches and division by zero.

## Functions

A function is a reusable block of code that performs a specific task. Functions help organize programs and avoid repeating the same code over and over.

### Why functions are useful

Functions make code easier to read, test, and reuse. Instead of writing the same steps repeatedly, you can define a function once and call it whenever you need it.

```python
def greet(name):
    return "Hello, " + name

print(greet("Alice"))
print(greet("Sam"))
```

In this example, the function `greet()` takes a name as input and returns a greeting string.

### Function syntax

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print(result)
```

A function starts with `def`, followed by a name and parentheses. The values inside the parentheses are parameters, and the `return` statement sends the result back to where the function was called.

### Function with no return value

Some functions only perform an action and do not return a value.

```python
def print_welcome():
    print("Welcome to Python!")

print_welcome()
```

### Built-in functions

Python already includes many useful built-in functions, such as `print()`, `len()`, `str()`, and `int()`.

```python
message = "Python"
print(len(message))
print(str(123))
```

### Key takeaways

Functions help group related code into reusable blocks. They make programs easier to organize, easier to maintain, and more efficient to write.





