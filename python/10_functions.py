# ============================================================
# FUNCTIONS IN PYTHON
# ============================================================

"""
FUNCTION:

A function is a reusable block of code that performs
a specific task.

Functions help us:
1. Reuse code.
2. Reduce repetition.
3. Organize programs.
4. Make code easier to test and maintain.

Use def to define a function.
"""


# ============================================================
# 1. CREATING A FUNCTION
# ============================================================

"""
Syntax:

def function_name():
    # code
"""

def greet():
    print("Hello, Python!")

# Calling the function
greet()


# ============================================================
# 2. PARAMETERS AND ARGUMENTS
# ============================================================

"""
Parameters:
Variables written in the function definition.

Arguments:
Actual values passed when calling the function.
"""

def greet(name):       # name is a parameter
    print("Hello", name)

greet("Rachit")        # "Rachit" is an argument


# ============================================================
# 3. FUNCTION WITH MULTIPLE PARAMETERS
# ============================================================

def add(a, b):
    print(a + b)

add(10, 20)

# Output:
# 30


# ============================================================
# 4. RETURN STATEMENT
# ============================================================

"""
return sends a result back to the caller.

It also ends the current function execution.
"""

def add(a, b):
    return a + b

result = add(10, 20)

print(result)  # 30


# ============================================================
# 5. PRINT VS RETURN
# ============================================================

"""
print():
Displays information on the screen.

return:
Sends a value back so it can be stored or reused.
"""

def square(number):
    return number * number

result = square(5)

print(result)  # 25


# ============================================================
# 6. DEFAULT PARAMETERS
# ============================================================

"""
A default parameter has a value that is used
when the caller does not provide an argument.
"""

def greet(name="User"):
    print("Hello", name)

greet()          # Hello User
greet("Rachit")  # Hello Rachit


# ============================================================
# 7. KEYWORD ARGUMENTS
# ============================================================

"""
Keyword arguments specify parameter names
when calling a function.
"""

def introduce(name, age):
    print(name, age)

introduce(name="Rachit", age=22)
introduce(age=22, name="Rachit")


# ============================================================
# 8. *ARGS
# ============================================================

"""
*args allows a function to receive any number
of positional arguments.

Inside the function, args is a tuple.
"""

def add_all(*args):
    return sum(args)

print(add_all(10, 20, 30))  # 60


# ============================================================
# 9. **KWARGS
# ============================================================

"""
**kwargs allows a function to receive additional
keyword arguments.

Inside the function, kwargs is a dictionary.
"""

def show_details(**kwargs):
    print(kwargs)

show_details(name="Rachit", role="AI Engineer")

# Output:
# {'name': 'Rachit', 'role': 'AI Engineer'}


# ============================================================
# 10. LOCAL AND GLOBAL VARIABLES
# ============================================================

"""
Local variable:
Defined inside a function.

Global variable:
Defined outside a function.
"""

x = 100  # Global variable

def display():
    y = 20  # Local variable
    print(x)
    print(y)

display()

# y cannot normally be accessed outside display().


# ============================================================
# 11. LAMBDA FUNCTION
# ============================================================

"""
A lambda is a small anonymous function containing
a single expression.
"""

square = lambda x: x * x

print(square(5))  # 25

# Use def for normal functions.
# Lambda is useful for short expressions.


# ============================================================
# 12. DOCSTRINGS
# ============================================================

"""
A docstring documents what a function does.
It is written immediately inside the function body.
"""

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

print(multiply(3, 4))
print(multiply.__doc__)


# ============================================================
# 13. AI ENGINEER EXAMPLE
# ============================================================

"""
Functions help organize reusable AI/ML tasks,
such as preprocessing data and calculating results.
"""

def calculate_average(numbers):
    if not numbers:
        return None

    return sum(numbers) / len(numbers)

scores = [80, 90, 85]

average = calculate_average(scores)

print(average)  # 85.0


# ============================================================
# QUICK REVISION
# ============================================================

"""
def       → Defines a function.
Call      → Executes a function.
Parameter → Variable in the function definition.
Argument  → Value passed to the function.
return    → Sends a result back to the caller.
Default   → Value used if an argument is omitted.
*args     → Accepts extra positional arguments as a tuple.
**kwargs  → Accepts extra keyword arguments as a dictionary.
lambda    → Creates a small anonymous function.
Docstring → Documents a function.
"""