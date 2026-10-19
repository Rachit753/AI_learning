# ============================================================
# VARIABLES IN PYTHON
# ============================================================

# A variable is a name/reference that refers to an object.
# We use variables to store/reference values and use them later in our program.

x = 10
name = "Rachit"

# In Python, variables (names) refer to objects in memory.

# Conceptually:
#
# x  ─────→  10
#            int object
#
# name ───→ "Rachit"
#            str object




# ============================================================
# RULES FOR DECLARING / NAMING VARIABLES
# ============================================================

# 1. A variable name must start with a letter (A-Z/a-z) or an underscore (_).
# 2. A variable name CANNOT start with a number.
# 3. After the first character, we can use: letters, numbers and underscore.
# 4. Spaces are NOT allowed.
# 5. Python is case-sensitive, name and Name are two different variables.
# 6. We cannot use Python keywords as variable names.



# ============================================================
# IMPORTANT: PYTHON IS DYNAMICALLY TYPED
# ============================================================

# We don't have to declare the type of a variable.

x = 10
# Python knows that 10 is an int object.

x = "Hello"
# Now x refers to a str object.

# So the same variable/name can refer to objects of different types at different times.


# ============================================================
# DATA TYPES
# ============================================================

# Data type tells us what kind of object/value we are working with and what operations are applicable to it.

# In Python, types belong to OBJECTS, not variables.


"""
                    DATA TYPES
                         |
       ┌─────────────────┼──────────────────┐
       |                 |                  |
    Numeric          Sequence          Collection
       |                 |                  |
   ┌───┼───┐       ┌────┼────┐        ┌────┼────┐
   |   |   |       |    |    |        |    |    |
  int float complex list tuple range  set dict ...
       
       Other built-in types
       |
       ├── bool
       ├── str
       ├── bytes
       ├── bytearray
       ├── frozenset
       ├── NoneType
       └── memoryview
"""


# ============================================================
# 1. NUMERIC TYPES
# ============================================================

# Numeric types:
#
# int
# float
# complex


# ----- int -----
# Whole numbers

age = 22
marks = 95
temperature = -5

print(type(age))
# <class 'int'>


# ----- float -----
# Decimal numbers

price = 99.99
height = 5.8
percentage = 85.5

print(type(price))
# <class 'float'>


# ----- complex -----
# Complex numbers contain a real and imaginary part.

z = 3 + 4j

print(type(z))
# <class 'complex'>



# ============================================================
# 2. BOOLEAN TYPE
# ============================================================

# bool has only two values:

True
False

is_student = True
is_logged_in = False

print(type(is_student))
# <class 'bool'>


# ============================================================
# 3. TEXT TYPE
# ============================================================

# str = String
# Used to store text.

name = "Rachit"
city = "xyz"

print(type(name))
# <class 'str'>


# ============================================================
# 4. SEQUENCE TYPES
# ============================================================

# Main sequence types:
#
# list
# tuple
# range


# ----- list -----
# Ordered and mutable collection.

skills = ["Python", "SQL", "Git"]

skills[0] = "Java"

# List can be changed.


# ----- tuple -----
# Ordered and immutable collection.

coordinates = (10, 20)

# Tuple cannot normally be changed after creation.


# ----- range -----
# Represents a sequence of numbers.
# Commonly used in loops.

numbers = range(5)

# Gives:
# 0, 1, 2, 3, 4


# ============================================================
# 5. SET TYPES
# ============================================================

# set
# frozenset


# ----- set -----
# Unordered collection of unique elements.

numbers = {1, 2, 3, 3, 4}

# Result conceptually:
# {1, 2, 3, 4}


# ----- frozenset -----
# Immutable version of a set.

numbers = frozenset({1, 2, 3})


# ============================================================
# 6. MAPPING TYPE
# ============================================================

# dict = Dictionary
# Stores data in key-value pairs.

student = {
    "name": "Rachit",
    "age": 22
}

# Key       Value
# name  →   Rachit
# age   →   22


# Accessing a value:

print(student["name"])
# Rachit


# ============================================================
# 7. BINARY TYPES
# ============================================================

# Binary data types:
#
# bytes
# bytearray
# memoryview


# ----- bytes -----

data = b"Hello"

print(type(data))
# <class 'bytes'>


# ----- bytearray -----

data = bytearray(b"Hello")


# ----- memoryview -----

data = memoryview(b"Hello")


# ============================================================
# 8. NONE TYPE
# ============================================================

# None represents the absence of a value.

result = None

print(type(result))
# <class 'NoneType'>