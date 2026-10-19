# ============================================================
# LIST COMPREHENSION
# ============================================================

"""
LIST COMPREHENSION:

List comprehension provides a short way to create a new list
using an iterable, such as a list or range.

Syntax:

[expression for item in iterable]
"""


# ============================================================
# 1. BASIC LIST COMPREHENSION
# ============================================================

numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers]

print(squares)

# Output:
# [1, 4, 9, 16, 25]


# ============================================================
# 2. LIST COMPREHENSION WITH IF
# ============================================================

"""
The if condition filters which items are included.
"""

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)

# Output:
# [2, 4, 6]


# ============================================================
# 3. LIST COMPREHENSION WITH IF-ELSE
# ============================================================

"""
if-else chooses the output value for each item.

Syntax:

[true_value if condition else false_value
 for item in iterable]
"""

numbers = [1, 2, 3, 4, 5]

results = [
    "Even" if num % 2 == 0 else "Odd"
    for num in numbers
]

print(results)

# Output:
# ['Odd', 'Even', 'Odd', 'Even', 'Odd']


# ============================================================
# 4. LIST COMPREHENSION WITH RANGE()
# ============================================================

squares = [num ** 2 for num in range(1, 6)]

print(squares)

# Output:
# [1, 4, 9, 16, 25]


# ============================================================
# DICTIONARY COMPREHENSION
# ============================================================

"""
DICTIONARY COMPREHENSION:

Dictionary comprehension provides a short way to create
a dictionary using an iterable.

Syntax:

{key_expression: value_expression for item in iterable}
"""


# ============================================================
# 5. BASIC DICTIONARY COMPREHENSION
# ============================================================

numbers = [1, 2, 3, 4, 5]

squares = {num: num ** 2 for num in numbers}

print(squares)

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ============================================================
# 6. DICTIONARY COMPREHENSION WITH IF
# ============================================================

"""
The if condition filters which key-value pairs are included.
"""

numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    num: num ** 2
    for num in numbers
    if num % 2 == 0
}

print(even_squares)

# Output:
# {2: 4, 4: 16, 6: 36}


# ============================================================
# 7. DICTIONARY COMPREHENSION FROM TWO LISTS
# ============================================================

"""
zip() combines corresponding elements from iterables.
"""

names = ["Rachit", "Aman", "Rahul"]
scores = [90, 85, 88]

result = {
    name: score
    for name, score in zip(names, scores)
}

print(result)

# Output:
# {'Rachit': 90, 'Aman': 85, 'Rahul': 88}


# ============================================================
# 8. AI ENGINEER EXAMPLE
# ============================================================

"""
List comprehension:
Filter high-confidence predictions.

Dictionary comprehension:
Store predictions with their confidence scores.
"""

confidence_scores = [0.95, 0.45, 0.87, 0.30, 0.91]

high_confidence = [
    score for score in confidence_scores
    if score >= 0.80
]

print(high_confidence)

# Output:
# [0.95, 0.87, 0.91]


predictions = ["cat", "dog", "bird"]
scores = [0.95, 0.87, 0.91]

prediction_scores = {
    label: score
    for label, score in zip(predictions, scores)
}

print(prediction_scores)


# ============================================================
# QUICK REVISION
# ============================================================

"""
LIST COMPREHENSION:

Creates a list using [].

Syntax:
[expression for item in iterable if condition]


DICTIONARY COMPREHENSION:

Creates a dictionary using {} with key-value pairs.

Syntax:
{key: value for item in iterable if condition}


IMPORTANT:

- List comprehension creates a list.
- Dictionary comprehension creates a dictionary.
- The if condition filters elements.
- An if-else expression chooses an output value.
- Use readable loops when comprehension becomes complex.
"""