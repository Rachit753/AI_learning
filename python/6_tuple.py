# ============================================================
# TUPLES IN PYTHON
# ============================================================

"""
TUPLE:

A tuple is an ordered and immutable collection of items.

Ordered:
Items maintain their position.

Immutable:
Items cannot be changed, added, or removed after creation.

Tuples are written using parentheses ().
Tuples allow duplicate values and different data types.
"""


# ============================================================
# 1. CREATING A TUPLE
# ============================================================

numbers = (10, 20, 30, 40)

print(numbers)

# Output:
# (10, 20, 30, 40)


# ============================================================
# 2. ACCESSING TUPLE ELEMENTS
# ============================================================

"""
Indexing starts from 0.
Negative indexing starts from -1.
"""

fruits = ("Apple", "Banana", "Mango")

print(fruits[0])   # Apple
print(fruits[-1])  # Mango


# ============================================================
# 3. TUPLE SLICING
# ============================================================

"""
Syntax: tuple[start:stop:step]

The stop index is excluded.
"""

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

# Output:
# (20, 30, 40)


# ============================================================
# 4. SINGLE-ELEMENT TUPLE
# ============================================================

"""
A comma is required to create a single-element tuple.
"""

a = (10)

b = (10,)

print(type(a))  # <class 'int'>
print(type(b))  # <class 'tuple'>


# ============================================================
# 5. TUPLE METHODS
# ============================================================

"""
Tuples have two commonly used methods:

count() → Counts occurrences of a value.
index() → Returns the index of the first occurrence.
"""

numbers = (10, 20, 10, 30)

print(numbers.count(10))  # 2
print(numbers.index(20))  # 1


# ============================================================
# 6. TUPLE IMMUTABILITY
# ============================================================

"""
Tuples do not support item assignment.
"""

numbers = (10, 20, 30)

# numbers[0] = 100  # TypeError


# ============================================================
# 7. TUPLE VS LIST
# ============================================================

"""
LIST:
- Written using []
- Mutable
- More methods for modifying elements

TUPLE:
- Written using ()
- Immutable
- Has fewer built-in methods

Both are ordered and allow duplicate values.
"""


# ============================================================
# 8. AI ENGINEER RELEVANCE
# ============================================================

"""
Tuples are useful for storing fixed collections of values.

Examples:
- Image dimensions
- Coordinates
- Fixed configuration values
- Returning multiple values from a function
"""

image_size = (224, 224, 3)

height, width, channels = image_size

print(height, width, channels)

# Output:
# 224 224 3


# ============================================================
# QUICK REVISION
# ============================================================

"""
1. Tuple is ordered and immutable.
2. Indexing starts from 0.
3. Tuples allow duplicates.
4. Use a comma for a single-element tuple.
5. count() counts occurrences.
6. index() returns the first matching index.
7. Tuples can contain different data types.
"""