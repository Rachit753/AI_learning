# ============================================================
# SETS IN PYTHON
# ============================================================

"""
SET:

A set is an unordered collection of unique elements.

Unordered:
Sets do not support indexing or slicing.

Unique:
Duplicate elements are automatically removed.

Mutable:
We can add or remove elements from a set.

Sets are created using curly braces {} or set().
"""


# ============================================================
# 1. CREATING A SET
# ============================================================

numbers = {10, 20, 30, 40}

print(numbers)

# Output contains:
# 10, 20, 30, 40
# The display order is not guaranteed.


# ============================================================
# 2. DUPLICATE VALUES
# ============================================================

"""
Sets automatically remove duplicate elements.
"""

numbers = {10, 20, 10, 30, 20}

print(numbers)

# Result contains only:
# 10, 20, 30


# ============================================================
# 3. CREATING AN EMPTY SET
# ============================================================

"""
Use set() to create an empty set.

{} creates an empty dictionary, not a set.
"""

my_set = set()

my_dictionary = {}

print(type(my_set))        # <class 'set'>
print(type(my_dictionary)) # <class 'dict'>


# ============================================================
# 4. ADDING ELEMENTS
# ============================================================

"""
add() adds one element.
update() adds elements from an iterable.
"""

numbers = {10, 20, 30}

numbers.add(40)
print(numbers)

numbers.update([50, 60])
print(numbers)


# ============================================================
# 5. REMOVING ELEMENTS
# ============================================================

"""
remove() removes an element but raises KeyError
if the element does not exist.

discard() removes an element without raising an error
if it does not exist.

pop() removes and returns an arbitrary element.
"""

numbers = {10, 20, 30}

numbers.remove(10)
numbers.discard(50)

print(numbers)


# ============================================================
# 6. SET OPERATIONS
# ============================================================

"""
UNION (|):
Returns elements from both sets.

INTERSECTION (&):
Returns elements common to both sets.

DIFFERENCE (-):
Returns elements in the first set but not the second.

SYMMETRIC DIFFERENCE (^):
Returns elements that belong to either set,
but not both.
"""

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # Union: {1, 2, 3, 4, 5, 6}
print(a & b)  # Intersection: {3, 4}
print(a - b)  # Difference: {1, 2}
print(a ^ b)  # Symmetric difference: {1, 2, 5, 6}


# ============================================================
# 7. MEMBERSHIP OPERATORS
# ============================================================

"""
in checks whether an element exists in a set.
"""

numbers = {10, 20, 30}

print(20 in numbers)      # True
print(50 not in numbers)  # True


# ============================================================
# 8. LOOPING THROUGH A SET
# ============================================================

"""
You can iterate through a set using a for loop.
The order of iteration is not guaranteed.
"""

fruits = {"Apple", "Banana", "Mango"}

for fruit in fruits:
    print(fruit)


# ============================================================
# 9. SET LENGTH
# ============================================================

"""
len() returns the number of unique elements.
"""

numbers = {10, 20, 10, 30}

print(len(numbers))  # 3


# ============================================================
# 10. FROZENSET
# ============================================================

"""
frozenset() creates an immutable set.

Its elements cannot be added or removed after creation.
"""

numbers = frozenset([10, 20, 30])

# numbers.add(40)  # AttributeError


# ============================================================
# 11. AI ENGINEER RELEVANCE
# ============================================================

"""
Sets are useful for:

1. Removing duplicate values.
2. Finding unique words or labels.
3. Comparing collections of items.
4. Checking membership efficiently on average.
"""

words = ["AI", "Python", "AI", "ML", "Python"]

unique_words = set(words)

print(unique_words)

# Contains only:
# "AI", "Python", "ML"


# ============================================================
# QUICK REVISION
# ============================================================

"""
1. Sets store unique elements.
2. Sets are mutable.
3. Sets do not support indexing or slicing.
4. Duplicate values are removed automatically.
5. Use set() to create an empty set.
6. add() adds one element.
7. update() adds multiple elements.
8. remove() can raise KeyError.
9. discard() does not raise an error for missing elements.
10. | = Union
11. & = Intersection
12. - = Difference
13. ^ = Symmetric difference
14. frozenset() creates an immutable set.
"""