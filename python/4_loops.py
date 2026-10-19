# ============================================================
# LOOPS IN PYTHON
# ============================================================

"""
LOOPS:

Loops are used to execute a block of code repeatedly.

Python mainly has two types of loops:

1. for loop
2. while loop

Loops are very important in AI/ML because they are commonly
used for processing data, iterating through datasets,
processing predictions, and repeating tasks.
"""


# ============================================================
# 1. FOR LOOP
# ============================================================

"""
A for loop is used to iterate over an iterable.

An iterable is an object whose elements can be accessed
one by one.

Examples of iterables:

- list
- tuple
- string
- set
- dictionary
- range
"""

numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)


# ============================================================
# 2. FOR LOOP WITH STRING
# ============================================================

"""
A for loop can iterate through each character of a string.
"""

name = "Python"

for character in name:
    print(character)


# ============================================================
# 3. RANGE()
# ============================================================

"""
range() generates a sequence of numbers.

Syntax:

range(start, stop, step)

Important:
The stop value is NOT included.
"""

for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4


# ============================================================
# RANGE WITH START AND STOP
# ============================================================

for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5


# ============================================================
# RANGE WITH STEP
# ============================================================

for i in range(0, 10, 2):
    print(i)

# Output:
# 0
# 2
# 4
# 6
# 8


# ============================================================
# 4. WHILE LOOP
# ============================================================

"""
A while loop repeatedly executes a block of code
as long as the condition is True.

Syntax:

while condition:
    # code
"""

count = 1

while count <= 5:
    print(count)
    count += 1


# ============================================================
# IMPORTANT: UPDATE THE CONDITION
# ============================================================

"""
In a while loop, make sure the condition eventually
becomes False.

Otherwise, the loop may become an infinite loop.
"""

count = 1

while count <= 5:
    print(count)
    count += 1


# ============================================================
# 5. INFINITE LOOP
# ============================================================

"""
An infinite loop occurs when the loop condition
never becomes False.

Example:

while True:
    print("Running")

This loop will continue indefinitely until it is stopped
or interrupted.
"""


# ============================================================
# 6. BREAK
# ============================================================

"""
break is used to immediately terminate the loop.

When Python encounters break:

- The loop stops immediately.
- Python moves to the statement after the loop.
"""

for i in range(1, 10):

    if i == 5:
        break

    print(i)

# Output:
# 1
# 2
# 3
# 4


# ============================================================
# BREAK WITH WHILE LOOP
# ============================================================

count = 1

while count <= 10:

    if count == 5:
        break

    print(count)
    count += 1


# ============================================================
# 7. CONTINUE
# ============================================================

"""
continue is used to skip the current iteration
and move to the next iteration of the loop.

The loop itself does NOT stop.
"""

for i in range(1, 6):

    if i == 3:
        continue

    print(i)

# Output:
# 1
# 2
# 4
# 5


# ============================================================
# BREAK vs CONTINUE
# ============================================================

"""
break:

Stops the entire loop.

continue:

Skips only the current iteration and continues
with the next iteration.
"""

# Example of break:

for i in range(5):

    if i == 3:
        break

    print(i)

# Output:
# 0
# 1
# 2


# Example of continue:

for i in range(5):

    if i == 3:
        continue

    print(i)

# Output:
# 0
# 1
# 2
# 4


# ============================================================
# 8. PASS
# ============================================================

"""
pass means "do nothing".

It is used as a placeholder when Python requires
a statement but you don't want to execute any code yet.

pass does NOT skip an iteration.
pass does NOT stop the loop.
"""

for i in range(5):

    if i == 3:
        pass

    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4


# ============================================================
# BREAK vs CONTINUE vs PASS
# ============================================================

"""
break     → Stops the entire loop.

continue  → Skips the current iteration.

pass      → Does nothing; execution continues normally.
"""


# ============================================================
# 9. NESTED LOOPS
# ============================================================

"""
A loop inside another loop is called a nested loop.

The inner loop runs completely for each iteration
of the outer loop.
"""

for i in range(3):

    for j in range(3):

        print(i, j)


# ============================================================
# 10. BREAK IN NESTED LOOPS
# ============================================================

"""
A break statement normally terminates the NEAREST
enclosing loop in which it appears.

It does not automatically stop all nested loops.
"""

for i in range(3):

    for j in range(5):

        if j == 2:
            break

        print(i, j)


# ============================================================
# 11. CONTINUE IN NESTED LOOPS
# ============================================================

"""
continue affects the nearest enclosing loop.

It skips the current iteration of that loop.
"""

for i in range(3):

    for j in range(5):

        if j == 2:
            continue

        print(i, j)


# ============================================================
# 12. LOOPING THROUGH A LIST
# ============================================================

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


# ============================================================
# 13. LOOPING THROUGH A DICTIONARY
# ============================================================

"""
By default, iterating over a dictionary gives its keys.
"""

student = {
    "name": "Rachit",
    "age": 22,
    "course": "BTech CSE"
}

for key in student:
    print(key)


# ============================================================
# DICTIONARY VALUES
# ============================================================

for value in student.values():
    print(value)


# ============================================================
# DICTIONARY KEY-VALUE PAIRS
# ============================================================

for key, value in student.items():
    print(key, value)


# ============================================================
# 14. ENUMERATE()
# ============================================================

"""
enumerate() is useful when we need both:

- index
- value
"""

languages = ["Python", "Java", "JavaScript"]

for index, language in enumerate(languages):
    print(index, language)

# Output:
# 0 Python
# 1 Java
# 2 JavaScript


# ============================================================
# 15. LOOP + CONTINUE
# ============================================================

"""
AI/ML applications often process many values.

continue can be used to skip unwanted values.
"""

numbers = [10, -5, 20, -2, 30]

for number in numbers:

    if number < 0:
        continue

    print(number)


# ============================================================
# 16. LOOP + BREAK
# ============================================================

"""
break can be useful when we have found the required
result and don't need to continue searching.
"""

numbers = [10, 20, 30, 40, 50]

for number in numbers:

    if number == 30:
        print("Found")
        break


# ============================================================
# 17. IMPORTANT DIFFERENCE
# ============================================================

"""
FOR LOOP:

Used mainly when iterating over an iterable
or when the number of iterations is known/controlled.

Example:

for item in data:
    print(item)


WHILE LOOP:

Used when repetition depends on a condition.

Example:

while condition:
    # code
"""


# ============================================================
# 18. IMPORTANT LOOP TERMS
# ============================================================

"""
ITERATION:

One execution of the loop body.

Example:

for i in range(3):
    print(i)

The loop has 3 iterations.


ITERABLE:

An object that can be iterated over.

Examples:

list
tuple
string
set
dictionary
range


LOOP BODY:

The block of code executed during each iteration.


NESTED LOOP:

A loop inside another loop.
"""


# ============================================================
# 19. QUICK REVISION
# ============================================================

"""
for       → Iterates over an iterable.

while     → Repeats while a condition is True.

range()   → Generates a sequence of numbers.

break     → Immediately stops the nearest loop.

continue  → Skips the current iteration.

pass      → Does nothing; acts as a placeholder.

enumerate → Gives index + value while iterating.

nested loop → A loop inside another loop.
"""


# ============================================================
# AI ENGINEER IMPORTANCE
# ============================================================

"""
Loops are important for AI/ML because they help with:

1. Processing data
2. Iterating through datasets
3. Processing predictions
4. Validating input
5. Searching through results
6. Processing API responses
7. Repeating tasks
8. Working with lists and dictionaries

IMPORTANT:

In real AI/ML development, you will often use libraries
such as NumPy, Pandas, PyTorch and TensorFlow that perform
many operations without writing explicit Python loops.

This is called vectorized/batched computation and is
often more efficient for numerical workloads.
"""