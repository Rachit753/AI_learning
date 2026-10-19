# ============================================================
# LISTS IN PYTHON
# ============================================================

"""
LIST:

A list is an ordered and mutable collection of items.

Ordered:
Items maintain their position in the list.

Mutable:
We can add, remove, or modify items after creating a list.

A list can store different data types, including duplicate values.

Lists are written using square brackets [].
"""


# ============================================================
# 1. CREATING A LIST
# ============================================================

numbers = [10, 20, 30, 40, 50]
empty_list =[]

print(numbers)

# Output:
# [10, 20, 30, 40, 50]


# ============================================================
# 2. ACCESSING LIST ELEMENTS
# ============================================================

"""
Each item in a list has an index.

Positive indexing starts from 0.
Negative indexing starts from -1 at the end.
"""

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[0])   # Apple
print(fruits[1])   # Banana
print(fruits[-1])  # Orange
print(fruits[-2])  # Mango


# ============================================================
# 3. MODIFYING LIST ELEMENTS
# ============================================================

"""
Lists are mutable, so we can change an element
using its index.
"""

fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)

# Output:
# ['Apple', 'Orange', 'Mango']


# ============================================================
# 4. LIST SLICING
# ============================================================

"""
Slicing is used to access a portion of a list.

Syntax:

list[start:stop:step]

start = Starting index (included)
stop  = Ending index (excluded)
step  = Interval between elements
"""

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])
# [20, 30, 40]

print(numbers[:3])
# [10, 20, 30]

print(numbers[2:])
# [30, 40, 50, 60]

print(numbers[::2])
# [10, 30, 50]

print(numbers[::-1])
# [60, 50, 40, 30, 20, 10]


# ============================================================
# 5. len() FUNCTION
# ============================================================

"""
len() returns the number of elements in a list.
"""

numbers = [10, 20, 30, 40]

print(len(numbers))

# Output:
# 4


# ============================================================
# 6. APPEND()
# ============================================================

"""
append() adds one item to the end of a list.

It modifies the original list.
"""

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)

# Output:
# [10, 20, 30, 40]


# ============================================================
# 7. INSERT()
# ============================================================

"""
insert() adds an item at a specified index.

Syntax:

list.insert(index, value)
"""

numbers = [10, 30, 40]

numbers.insert(1, 20)

print(numbers)

# Output:
# [10, 20, 30, 40]


# ============================================================
# 8. EXTEND()
# ============================================================

"""
extend() adds the elements of an iterable to the end
of the existing list.
"""

numbers = [10, 20]

numbers.extend([30, 40])

print(numbers)

# Output:
# [10, 20, 30, 40]


# ============================================================
# 9. APPEND() VS EXTEND()
# ============================================================

"""
append():

Adds its argument as one item.

extend():

Adds the elements from an iterable individually.
"""

numbers1 = [1, 2]
numbers1.append([3, 4])

print(numbers1)

# Output:
# [1, 2, [3, 4]]


numbers2 = [1, 2]
numbers2.extend([3, 4])

print(numbers2)

# Output:
# [1, 2, 3, 4]


# ============================================================
# 10. REMOVE()
# ============================================================

"""
remove() removes the first matching value from a list.

If the value is not found, Python raises ValueError.
"""

numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)

# Output:
# [10, 30, 20]


# ============================================================
# 11. POP()
# ============================================================

"""
pop() removes and returns an element.

Without an index:
Removes the last element.

With an index:
Removes the element at that index.
"""

numbers = [10, 20, 30, 40]

removed_item = numbers.pop()

print(removed_item)  # 40
print(numbers)       # [10, 20, 30]

removed_item = numbers.pop(0)

print(removed_item)  # 10
print(numbers)       # [20, 30]


# ============================================================
# 12. DEL STATEMENT
# ============================================================

"""
del removes an element, a slice, or the entire list variable.
"""

numbers = [10, 20, 30, 40]

del numbers[1]

print(numbers)

# Output:
# [10, 30, 40]


# ============================================================
# 13. CLEAR()
# ============================================================

"""
clear() removes all elements from a list.

The list itself still exists, but it becomes empty.
"""

numbers = [10, 20, 30]

numbers.clear()

print(numbers)

# Output:
# []


# ============================================================
# 14. INDEX()
# ============================================================

"""
index() returns the index of the first matching value.

If the value is not found, Python raises ValueError.
"""

fruits = ["Apple", "Banana", "Mango"]

print(fruits.index("Banana"))

# Output:
# 1


# ============================================================
# 15. COUNT()
# ============================================================

"""
count() returns the number of times a value appears.
"""

numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))

# Output:
# 3


# ============================================================
# 16. SORT()
# ============================================================

"""
sort() sorts the original list in ascending order by default.

It modifies the original list and returns None.
"""

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

# Output:
# [10, 20, 30, 40]


# ============================================================
# SORT IN DESCENDING ORDER
# ============================================================

numbers = [40, 10, 30, 20]

numbers.sort(reverse=True)

print(numbers)

# Output:
# [40, 30, 20, 10]


# ============================================================
# 17. SORTED()
# ============================================================

"""
sorted() returns a new sorted list.

The original list remains unchanged.
"""

numbers = [40, 10, 30, 20]

new_numbers = sorted(numbers)

print(new_numbers)
# [10, 20, 30, 40]

print(numbers)
# [40, 10, 30, 20]


# ============================================================
# SORT() VS SORTED()
# ============================================================

"""
sort():

- List method
- Modifies the original list
- Returns None

sorted():

- Built-in function
- Returns a new sorted list
- Leaves the original iterable unchanged
"""


# ============================================================
# 18. REVERSE()
# ============================================================

"""
reverse() reverses the current order of elements.

It does not sort the list.
"""

numbers = [10, 30, 20, 40]

numbers.reverse()

print(numbers)

# Output:
# [40, 20, 30, 10]


# ============================================================
# 19. COPYING A LIST
# ============================================================

"""
Use copy() to create a shallow copy of a list.
"""

original = [10, 20, 30]

copied = original.copy()

copied.append(40)

print(original)
# [10, 20, 30]

print(copied)
# [10, 20, 30, 40]


# ============================================================
# 20. IMPORTANT: LIST ASSIGNMENT VS COPYING
# ============================================================

"""
Assigning one list variable to another does not create
an independent copy.

Both variables refer to the same list object.
"""

list1 = [10, 20, 30]

list2 = list1

list2.append(40)

print(list1)
# [10, 20, 30, 40]

print(list2)
# [10, 20, 30, 40]


# To create a shallow copy:
list1 = [10, 20, 30]

list2 = list1.copy()

list2.append(40)

print(list1)
# [10, 20, 30]

print(list2)
# [10, 20, 30, 40]


# ============================================================
# 21. MEMBERSHIP OPERATORS
# ============================================================

"""
in:

Checks whether an element exists in the list.

not in:

Checks whether an element does not exist in the list.
"""

numbers = [10, 20, 30, 40]

print(20 in numbers)
# True

print(50 in numbers)
# False

print(50 not in numbers)
# True


# ============================================================
# 22. LOOPING THROUGH A LIST
# ============================================================

"""
A for loop can access each element of a list one by one.
"""

numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)


# ============================================================
# 23. LOOPING WITH INDEX
# ============================================================

"""
range(len(list)) can be used when we need list indices.

enumerate() is often a cleaner option when we need
both the index and the value.
"""

fruits = ["Apple", "Banana", "Mango"]

for index in range(len(fruits)):
    print(index, fruits[index])

# Alternative using enumerate():

for index, fruit in enumerate(fruits):
    print(index, fruit)


# ============================================================
# 24. LIST CONCATENATION
# ============================================================

"""
The + operator combines two lists into a new list.
"""

list1 = [10, 20]
list2 = [30, 40]

combined = list1 + list2

print(combined)

# Output:
# [10, 20, 30, 40]


# ============================================================
# 25. LIST REPETITION
# ============================================================

"""
The * operator repeats the elements of a list.
"""

numbers = [1, 2]

print(numbers * 3)

# Output:
# [1, 2, 1, 2, 1, 2]


# ============================================================
# 26. NESTED LISTS
# ============================================================

"""
A nested list is a list that contains other lists.
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])
# [1, 2, 3]

print(matrix[1][2])
# 6


# ============================================================
# 27. COMMON LIST ERRORS
# ============================================================

"""
IndexError:

Occurs when accessing an index that does not exist.
"""

numbers = [10, 20, 30]

# print(numbers[5])  # IndexError


"""
ValueError:

Can occur when remove() or index() cannot find
the requested value.
"""

numbers = [10, 20, 30]

# numbers.remove(50)  # ValueError


"""
Empty list:

Check whether a list contains items before accessing
an element when the list may be empty.
"""

data = []

if data:
    print(data[0])
else:
    print("List is empty")


# ============================================================
# 28. IMPORTANT: APPEND RETURNS NONE
# ============================================================

"""
Methods such as append(), sort(), reverse(), and extend()
modify the original list and return None.

Do not assign their return values when you want to keep
the modified list.
"""

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
# [10, 20, 30, 40]

# Incorrect:
# numbers = numbers.append(50)

# The assignment above makes numbers equal to None.


# ============================================================
# 29. IMPORTANT: MUTABLE OBJECTS
# ============================================================

"""
A list is mutable.

This means its elements can be changed after creation.

When a list is passed to a function, the function can
modify that same list object.
"""

def add_item(items):
    items.append(40)

numbers = [10, 20, 30]

add_item(numbers)

print(numbers)

# Output:
# [10, 20, 30, 40]


# ============================================================
# 30. AI ENGINEER EXAMPLE: PROCESSING DATA
# ============================================================

"""
Lists can store data values that need to be processed.
"""

temperatures = [25.5, 30.0, 28.5, 35.0]

for temperature in temperatures:
    if temperature > 30:
        print("High temperature:", temperature)


# ============================================================
# 31. AI ENGINEER EXAMPLE: FILTERING PREDICTIONS
# ============================================================

"""
An AI application may receive confidence scores
from a model and keep only scores above a threshold.
"""

confidence_scores = [0.95, 0.45, 0.87, 0.30, 0.91]

high_confidence = [
    score for score in confidence_scores
    if score >= 0.80
]

print(high_confidence)

# Output:
# [0.95, 0.87, 0.91]


# ============================================================
# 32. AI ENGINEER EXAMPLE: CLEANING DATA
# ============================================================

"""
A simple list comprehension can filter out None values.

Real data cleaning may require more detailed validation.
"""

values = [10, None, 20, None, 30]

cleaned_values = [
    value for value in values
    if value is not None
]

print(cleaned_values)

# Output:
# [10, 20, 30]


# ============================================================
# 33. IMPORTANT LIST METHODS: QUICK REVISION
# ============================================================

"""
append(x)       → Adds one item to the end.
insert(i, x)   → Inserts an item at an index.
extend(iterable) → Adds elements from an iterable.
remove(x)      → Removes the first matching value.
pop(i)         → Removes and returns an item.
clear()        → Removes all elements.
index(x)       → Returns the first matching index.
count(x)       → Counts occurrences of a value.
sort()         → Sorts the original list.
reverse()      → Reverses the current order.
copy()         → Creates a shallow copy.
len(list)      → Returns the number of elements.
sorted(list)   → Returns a new sorted list.
"""


# ============================================================
# 34. LIST IMPORTANT POINTS
# ============================================================

"""
1. Lists are ordered.
2. Lists are mutable.
3. Lists allow duplicate values.
4. Lists can contain different data types.
5. Indexing starts from 0.
6. Negative indexing starts from -1.
7. Slicing can access a portion of a list.
8. append() adds one item.
9. extend() adds elements from an iterable.
10. sort() modifies the original list.
11. sorted() returns a new sorted list.
12. Assignment does not create a copy.
13. copy() creates a shallow copy.
14. Lists are commonly used for data processing.
15. List comprehensions are useful for concise transformations.
"""


# ============================================================
# 35. AI ENGINEER RELEVANCE
# ============================================================

"""
Lists are useful for:

1. Storing collections of data.
2. Processing input records.
3. Filtering values.
4. Storing predictions.
5. Working with API response data.
6. Preparing data before model processing.
7. Creating batches or collections of examples.
8. Learning data structures and algorithms.

IMPORTANT:

Python lists are general-purpose collections.

For large numerical computations, NumPy arrays are often
more efficient and support vectorized operations.

Pandas is commonly used for tabular data.

PyTorch and TensorFlow provide tensors for machine learning
and deep learning computations.
"""