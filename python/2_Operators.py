# ============================================================
# OPERATORS IN PYTHON
# ============================================================

# Operators are symbols or keywords used to perform operations on values/objects (operands).

# Example:
a = 10
b = 5
result = a + b

# Here:
# a and b  → operands
# +        → operator
# result   → 15


# ============================================================
# TYPES OF OPERATORS
# ============================================================

"""
                         OPERATORS
                             |
      ┌──────────────┬───────┼────────┬───────────────┐
      ↓              ↓       ↓        ↓               ↓
  Arithmetic    Comparison  Assignment Logical      Identity
      |              |       |          |              |
   + - * /        == !=      = +=      and             is
   // % **        > <        -= *=     or              is not
                  >= <=      /= %=     not
                             //= **=
      
      ┌──────────────┬───────────────┐
      ↓              ↓               ↓
 Membership       Bitwise       Conditional
      |              |              |
   in             & | ^ ~       x if condition else y
   not in         << >>
"""


# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================

# Used to perform mathematical operations.
a = 10
b = 3
print(a + b)    # Addition       → 13
print(a - b)    # Subtraction    → 7
print(a * b)    # Multiplication → 30
print(a / b)    # Division       → 3.333...
print(a // b)   # Floor division → 3
print(a % b)    # Modulus        → 1
print(a ** b)   # Power          → 1000


# Important:
#
# /  → normal division, usually returns float
# // → floor division
# %  → remainder
# ** → exponent/power


# Example:
print(10 / 2)      # 5.0
print(10 // 3)     # 3
print(10 % 3)      # 1
print(2 ** 3)      # 8


# ============================================================
# 2. COMPARISON OPERATORS
# ============================================================

# Used to compare two values.
# The result is always a Boolean value: True or False.

a = 10
b = 5
print(a == b)   # Equal to              → False
print(a != b)   # Not equal to          → True
print(a > b)    # Greater than          → True
print(a < b)    # Less than             → False
print(a >= b)   # Greater/equal         → True
print(a <= b)   # Less/equal            → False


# ============================================================
# 3. ASSIGNMENT OPERATORS
# ============================================================

# Used to assign or update values.
x = 10

# Compound assignment operators:
x += 5
# Same as: x = x + 5
# x = 15

x -= 5
# Same as: x = x - 5
# x = 10

x *= 2
# Same as: x = x * 2
# x = 20

x /= 2
# Same as: x = x / 2
# x = 10.0

x //= 3
# Same as: x = x // 3

x %= 3
# Same as: x = x % 3

x **= 2
# Same as: x = x ** 2


# Main assignment operators:

"""
= 
+=
-=
*=
/=
//=
%=
**=
"""


# ============================================================
# 4. LOGICAL OPERATORS
# ============================================================

# Used to combine or modify conditions, Python has three logical operators: and , or , not 


# -------------------------
# AND
# -------------------------

# Returns True when both conditions are True.

age = 22
has_id = True

print(age >= 18 and has_id)
# True


# Truth table:

"""
True  and True  → True
True  and False → False
False and True  → False
False and False → False
"""


# -------------------------
# OR
# -------------------------

# Returns True if at least one condition is True.

is_weekend = False
is_holiday = True

print(is_weekend or is_holiday)
# True


# Truth table:

"""
True  or True  → True
True  or False → True
False or True  → True
False or False → False
"""


# -------------------------
# NOT
# -------------------------

# Reverses the truth value.

is_logged_in = True

print(not is_logged_in)
# False


# ============================================================
# 5. IDENTITY OPERATORS
# ============================================================

# Identity operators check whether two names refer to the SAME OBJECT.

# Operators:
#
# is
# is not


a = [1, 2, 3]
b = a

print(a is b)
# True
#
# Both a and b refer to the same list object.


# Example:

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True
print(a is b)   # False


# Why?
#
# == checks VALUE equality.
# is checks OBJECT IDENTITY.


# VERY IMPORTANT:
#
# ==  → "Are their values equal?"
# is  → "Are they the same object?"


# Use "is" commonly with None:

result = None

if result is None:
    print("No result")


# Prefer:
# result is None
#
# instead of:
# result == None


# ============================================================
# 6. MEMBERSHIP OPERATORS
# ============================================================

# Used to check whether a value exists inside an iterable.

# Operators:
#
# in
# not in


skills = ["Python", "SQL", "Git"]

print("Python" in skills)
# True

print("Java" in skills)
# False

print("Java" not in skills)
# True


# Membership also works with strings:

text = "Python is powerful"

print("Python" in text)
# True


# With dictionary:
#
# "in" checks KEYS by default.

student = {
    "name": "Rachit",
    "age": 22
}

print("name" in student)
# True

print("Rachit" in student)
# False


# ============================================================
# 7. BITWISE OPERATORS
# ============================================================

# Bitwise operators work at the level of individual bits of integer values.

# Operators:
#
# &   → Bitwise AND
# |   → Bitwise OR
# ^   → Bitwise XOR
# ~   → Bitwise NOT
# <<  → Left shift
# >>  → Right shift


a = 5
b = 3

# Binary:
#
# 5 = 101
# 3 = 011


print(a & b)

"""
  101
  011
  ---
  001

Result = 1
"""


print(a | b)

"""
  101
  011
  ---
  111

Result = 7
"""


print(a ^ b)

"""
  101
  011
  ---
  110

Result = 6
"""


# Left shift

print(5 << 1)

# 5 = 101
# 101 << 1 = 1010
# 1010 = 10


# Right shift

print(5 >> 1)

# 5 = 101
# 101 >> 1 = 10
# 10 = 2


# Bitwise operators are useful in:
#
# - Low-level programming
# - Flags and permissions
# - Performance-sensitive operations
# - Networking
# - Some algorithms
# - Computer vision / AI implementations in some contexts


# ============================================================
# 8. CONDITIONAL EXPRESSION (TERNARY)
# ============================================================

# Python has a one-line conditional expression.

age = 22

status = "Adult" if age >= 18 else "Minor"

print(status)
# Adult


# General syntax:
#
# (value_if_true) if condition else (value_if_false)


# ============================================================
# 9. OPERATOR PRECEDENCE
# ============================================================

# When multiple operators are present in an expression,
# Python follows operator precedence rules.

result = 2 + 3 * 4

print(result)
# 14
#
# Multiplication happens before addition.


# Parentheses have higher priority:

result = (2 + 3) * 4

print(result)
# 20


# Basic precedence order to remember:

"""
1. ()
2. **
3. +x, -x, ~x
4. *, /, //, %
5. +, -
6. <<, >>
7. &
8. ^
9. |
10. ==, !=, >, <, >=, <=, is, is not, in, not in
11. not
12. and
13. or
14. if ... else
"""


# IMPORTANT:
# When in doubt, use parentheses.

result = (10 + 5) * 2


# ============================================================
# 10. SHORT-CIRCUIT EVALUATION
# ============================================================

# Python does not always evaluate every part of an
# "and" or "or" expression.

# With "and":
#
# If the first condition is False,
# Python does not need to evaluate the second condition.

x = 5

if x > 10 and x / 0 > 1:
    print("Hello")

# x > 10 is False.
# So Python stops there.
# It does NOT evaluate x / 0.


# With "or":
#
# If the first condition is True,
# Python does not need to evaluate the second condition.

x = 10

if x == 10 or x / 0 > 1:
    print("Hello")

# x == 10 is True.
# Python stops and does not evaluate x / 0.


# This is called SHORT-CIRCUIT EVALUATION.



# ============================================================
# IMPORTANT TERMS
# ============================================================


# ============================================================
# 1. TYPE CONVERSION
# ============================================================

# Type conversion means converting a value/object from one data type to another data type.


# There are two common types:

# 1. IMPLICIT TYPE CONVERSION
# Python automatically performs the conversion when appropriate.

a = 10       # int
b = 2.5      # float

result = a + b

print(result)        # 12.5
print(type(result))  # <class 'float'>
# int + float → float


# 2. EXPLICIT TYPE CONVERSION
# The programmer manually converts a value using built-in
# functions such as int(), float(), str(), bool(), etc.

age = "22"

age = int(age)

print(age)        # 22
print(type(age))  # <class 'int'>


# Common conversion functions:
int()
float()
str()
bool()
list()
tuple()
set()
dict()


# Examples:
x = "10"

print(int(x))       # 10
print(float(x))     # 10.0
print(str(10))      # "10"
print(bool(1))      # True


# IMPORTANT:
# Not every conversion is possible.

# int("Hello")      # ❌ ValueError
# int("10.5")       # ❌ ValueError


# ============================================================
# 2. IDENTIFIER
# ============================================================

# An identifier is a name used to identify a programming element such as a variable, function, class, module, etc.

name = "Rachit"
# "name" is an identifier.


def calculate_sum():
    pass
# "calculate_sum" is an identifier.


class Student:
    pass
# "Student" is an identifier.


# ============================================================
# RULES FOR IDENTIFIERS
# ============================================================

# 1. An identifier can contain:
#    - letters (A-Z, a-z)
#    - digits (0-9)
#    - underscore (_)

# 2. An identifier CANNOT start with a digit.
# 3. Spaces are not allowed.
# 4. Python is case-sensitive.
# 5. Python keywords cannot be used as identifiers.



# ============================================================
# IDENTIFIER vs VARIABLE
# ============================================================

# Identifier = a general name used to identify something.

# Variable = a name/reference that refers to an object.

x = 10

# "x" is:
# - an identifier
# - specifically, it is being used as a variable name.


# Example:

def greet():
    print("Hello")

# "greet" is an identifier.
# Here it is the name of a function.


class Student:
    pass

# "Student" is an identifier.
# Here it is the name of a class.



# ============================================================
# IMPORTANT DIFFERENCES
# ============================================================

# 1. = vs ==

x = 10       # Assignment
x == 10      # Comparison


# 2. (==) vs (is)

a = [1, 2]
b = [1, 2]

a == b       # True → same values
a is b       # False → different objects


# 3. (in) vs (is)

"Python" in ["Python", "SQL"]
# Checks membership.

a is b
# Checks object identity.


# ============================================================
# OPERATORS QUICK REVISION
# ============================================================

"""
Arithmetic:
+  -  *  /  //  %  **

Comparison:
==  !=  >  <  >=  <=

Assignment:
=  +=  -=  *=  /=  //=  %=  **=

Logical:
and  or  not

Identity:
is  is not

Membership:
in  not in

Bitwise:
&  |  ^  ~  <<  >>

Conditional:
x if condition else y
"""


# ============================================================
# IMPORTANT FOR AI ENGINEERING
# ============================================================

# As an AI Engineer, the most important operators initially are:

"""
1. Arithmetic
2. Comparison
3. Assignment
4. Logical
5. Membership
6. Identity
7. Bitwise (understand the basics)
"""

# These will be used heavily in:
#
# - Data preprocessing
# - Conditions
# - Loops
# - Functions
# - Lists/dictionaries
# - NumPy
# - Pandas
# - Machine Learning code
# - Data filtering
# - Model evaluation
# - Boolean masks