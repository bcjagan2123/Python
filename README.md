# Module 1: Basics of Programming and Python

## Programming Basics

## Key Terms

- **Automation**: The process of replacing a manual step with one that happens automatically.

- **Client-side scripting language**: Primarily used for web programming; scripts are transferred from a web server to the end user’s browser, then executed in the browser.

- **Code editors**: Tools that provide features like syntax highlighting, automatic indentation, error checking, and autocompletion.

- **Computer program**: A step-by-step list of instructions that a computer follows to reach an intended goal.

- **Functions**: Reusable blocks of code that perform specific tasks.

- **IDE**: A software application that provides comprehensive facilities for software development.

- **Interpreter**: The program that reads and executes code.

- **Input**: Information provided to a program by the end user.

- **Logic errors**: Errors in code that prevent it from running correctly.

- **Machine language**: The lowest-level computer language. It communicates directly with computers in binary code (ones and zeros).

- **Object-oriented programming language**: A language where most coding elements are treated as objects with configurable properties.

- **Output**: The end result of a task performed by a function or computer program.

- **Platform-specific scripting language**: A language used by system administrators on a specific platform.

- **Programming**: The process of writing a program to behave in different ways.

- **Programming code**: A set of written computer instructions, guided by rules, using a computer programming language.

- **Programming languages**: Languages with syntax and semantics used to write computer programs.

- **Python**: A general-purpose programming language.

- **Python interpreter**: The program that reads and executes Python code by translating it into computer instructions.

- **Script**: Often used to automate specific tasks.

- **Semantics**: The intended meaning or effect of statements in both human and computer languages.

- **Syntax**: The rules for how statements are constructed in both human and computer languages.

- **Variables**: Named storage locations used to temporarily store changeable values in programming code.

# Python

## Introduction to Python

- **Python**: Python's syntax is easy to read and write, resembling human language. For example, you can define a list of friends and create greetings for each item to show Python's simplicity.

- **Why Python is relevant to IT**: Python is versatile and used in automation, web development, data analytics, machine learning, and many other fields.

- **Python is**:
  - a general-purpose scripting language
  - a popular language for building many types of applications
  - a common tool for automation
  - cross-platform compatible
  - beginner-friendly

- **Python is not**:
  - a platform-specific or OS-specific scripting language
  - a client-side scripting language
  - a purely object-oriented programming language

## Python key terms

- **Platform-specific / OS-specific scripting language**: A language designed for a single operating system, such as PowerShell for Windows or Bash for Linux.

- **Client-side scripting language**: A language used in web browsers where code is downloaded from a server and executed on the user's device. JavaScript is the most common example.

- **Machine language**: The lowest-level programming language, consisting of binary instructions that a computer processor executes directly.

- **Cross-platform language**: A language that works on multiple operating systems, such as Windows, Linux, macOS, iOS, and Android.

- **Object-oriented programming language**: A language in which code is organized around objects that have properties and behaviors. Objects can model real-world entities, like a form field that validates input and interacts with data.

- **Python interpreter**: The program that reads and executes Python code by translating it into computer instructions.


## First Python Program

Before running Python code, install Python and a code editor.

- Windows installation guide: [python.org/downloads/windows](https://www.python.org/downloads/windows)
- Linux installation guide: [python.org/downloads/source](https://www.python.org/downloads/source)
- Visual Studio Code setup: [code.visualstudio.com/docs/setup/setup-overview](https://code.visualstudio.com/docs/setup/setup-overview)

The simplest Python program prints text to the screen. The example below shows the classic "Hello, World!" program.

```python
print("Hello, World!")
```

To run this program, save it as `hello.py` and execute it with Python:

```bash
python hello.py
```

## Writing code using the command line

Python can be written and executed from the command line or terminal on any operating system.

### Using the command line on Linux

- Open the terminal with `Ctrl + Alt + T` or by clicking the terminal icon.
- Check if Python is installed:
  ```bash
  python3 --version
  ```
- If Python is not installed, install Python 3:
  ```bash
  sudo apt install python3
  ```

### Using the command line on Windows

- Open PowerShell or Command Prompt.
- Check if Python is installed:
  ```powershell
  python --version
  ```
- If Python is not installed, download it from [python.org/downloads/windows](https://www.python.org/downloads/windows) and install it.

### Writing Python code in interactive mode

- Start interactive mode on Linux:
  ```bash
  python3
  ```
- Start interactive mode on Windows:
  ```powershell
  python
  ```
- Test with a simple command:
  ```python
  print("Hello, World!")
  ```
- Exit interactive mode by typing:
  ```python
  exit()
  ```

## Code editors and IDEs

- **Code editors** are tools designed to write and edit source code.
- They usually include syntax highlighting, indentation support, search, and simple code completion.
- Examples of code editors are Visual Studio Code (VS Code), Sublime Text, Atom, and other lightweight editors.

- **Integrated Development Environments (IDEs)** include a code editor plus additional developer tools.
- IDEs often add debugging, testing, project management, and language-specific support.
- Examples of IDEs are PyCharm, Spyder, Thonny, and IntelliJ IDEA with Python support.

- A code editor is best for quickly writing and editing code.
- An IDE is more complete for larger or more complex projects because it bundles extra development tools.

### Visual Studio Code

- **VS Code** is a popular code editor from Microsoft that works well with Python.
- It supports syntax highlighting, IntelliSense code completion, debugging, extensions, and integrated terminals.
- To install VS Code, download it from [code.visualstudio.com](https://code.visualstudio.com/) and follow the platform-specific installer instructions.
- In VS Code, install the Python extension from the Extensions view (`Ctrl+Shift+X`) for Python support.
- To write Python code in VS Code:
  1. Open VS Code and create a new file with a `.py` extension.
  2. Write Python code in the editor.
  3. Save the file.
  4. Run the code using the built-in terminal with `python filename.py`, or use the Run button if the Python extension is installed.

### Jupyter Notebook and Jupyter Lab

- **Jupyter Notebook** is a web-based application that lets you create and share documents containing live code, equations, visualizations, and narrative text.
- Notebooks are organized into cells that can contain Python code or formatted text using Markdown.
- Jupyter Notebook is ideal for data exploration, analysis, and teaching.

- **Jupyter Lab** is the next-generation interface for Jupyter. It provides a flexible workspace with code consoles, notebooks, text editors, file browsers, and visualizations in one place.
- Jupyter Lab is more powerful than the classic Jupyter Notebook and is a good choice when you want multiple tools open side-by-side.

To use Jupyter, install it with:

```bash
pip install jupyterlab
```

Then start the app with:

```bash
jupyter lab
```

To open the classic notebook interface instead, use:

```bash
jupyter notebook
```

### Google Colab

- **Google Colab** is a free cloud-based notebook service from Google that runs Python code in the browser.
- Colab is useful when you do not want to install Python locally or when you want to share work with others.
- It supports Python code, Markdown text, and rich media like images and charts.

To use Colab:

1. Visit [colab.research.google.com](https://colab.research.google.com).
2. Sign in with your Google account.
3. Create a new notebook using **File > New notebook**.
4. Enter Python code in a cell and press **Shift + Enter** to run it.

Colab also lets you upload files, install packages, and connect to Google Drive for saved work.

## Functions

A function is a piece of code that performs a unit of work. In the examples you've seen so far, you have only encountered the `print()` function, which outputs a message to the screen. You will use functions frequently in this course to organize and reuse code.

Example:

```python
print("Hello, World!")
```

## Keywords

A keyword is a reserved word in a programming language that performs a specific purpose. Keywords cannot be used as variable names because the language already gives them special meaning.

Common Python keywords include:

- **Values**: `True`, `False`, `None`
- **Conditions**: `if`, `elif`, `else`
- **Logical operators**: `and`, `or`, `not`
- **Loops and iteration**: `for`, `in`, `while`, `break`, `continue`
- **Functions and definitions**: `def`, `return`, `lambda`
- **Import and modules**: `import`, `from`, `as`
- **Exceptions and errors**: `try`, `except`, `finally`, `raise`

Example using keywords:

```python
if True:
    print("This is a keyword example")
```

## Arithmetic operators

Python can calculate numbers using common mathematical operators and a few special operators.

- `x + y`: addition
- `x - y`: subtraction
- `x * y`: multiplication
- `x / y`: division (always returns a floating-point result)
- `x // y`: floor division (integer quotient)
- `x % y`: modulo (remainder)
- `x ** y`: exponentiation (power)

Example:

```python
x = 10
y = 3
print(x + y)  # 13
print(x - y)  # 7
print(x * y)  # 30
print(x / y)  # 3.333...
print(x // y) # 3
print(x % y)  # 1
print(x ** y) # 1000
```

## Order of operations

Python evaluates expressions using a fixed order. This means some operations are done before others.

1. Parentheses: expressions inside `( )` are evaluated first.
2. Exponents: `x ** y`
3. Multiplication, division, floor division, and modulo: `*`, `/`, `//`, `%`
4. Addition and subtraction: `+`, `-`

A helpful mnemonic is PEMDAS: Parentheses, Exponents, Multiplication and Division, Addition and Subtraction.

Example:

```python
result = 2 + 3 * 4
print(result)  # 14, because multiplication happens before addition

result = (2 + 3) * 4
print(result)  # 20, because parentheses change the order
```

# Module 2: Basic Python Syntax

## Expressions and variables

Python expressions combine values, variables, and operators to compute a result. Variables store values that can be used later in the program.

Example:

```python
x = 5
y = 2
total = x + y
print(total)  # 7
```


