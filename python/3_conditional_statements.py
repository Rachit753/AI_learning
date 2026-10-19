# ============================================================
# CONDITIONAL STATEMENTS
# ============================================================

"""
CONDITIONAL STATEMENTS:

Conditional statements are used to make decisions in a program
based on whether a condition is True or False.

Basic flow:

Condition
   ↓
True  → Execute one block
False → Execute another block
"""


# ============================================================
# 1. IF STATEMENT
# ============================================================

"""
The if statement executes a block of code only when
the given condition is True.

Syntax:

if condition:
    # code to execute
"""

age = 20

if age >= 18:
    print("Adult")


# ============================================================
# 2. IF-ELSE STATEMENT
# ============================================================

"""
if-else is used when there are two possible outcomes.

If the condition is True → if block executes.
If the condition is False → else block executes.
"""

age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not eligible")


# ============================================================
# 3. IF-ELIF-ELSE STATEMENT
# ============================================================

"""
if-elif-else is used when there are multiple conditions.

Python checks the conditions from top to bottom.
As soon as one condition becomes True, its block executes
and the remaining conditions are skipped.
"""

marks = 75

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("D")


# ============================================================
# 4. NESTED IF
# ============================================================

"""
A nested if means an if statement inside another if statement.
"""

age = 22
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")



# ============================================================
# 5. TRUTHY AND FALSY VALUES
# ============================================================

"""
Python can use objects directly in conditions.

Common Falsy values:

False
None
0
0.0
""
[]
()
{}
set()

Most other values are Truthy.
"""

name = ""

if name:
    print("Name exists")
else:
    print("Name is empty")


# ============================================================
# 6. CHECKING NONE
# ============================================================

"""
None represents the absence of a value.

Use 'is None' or 'is not None' when specifically
checking for None.
"""

result = None

if result is None:
    print("No result available")



# ============================================================
# 7. PASS
# ============================================================

"""
pass means "do nothing".

It is used as a placeholder when a block is required
but no code needs to be executed yet.
"""

age = 22

if age >= 18:
    pass


# ============================================================
# AI ENGINEER EXAMPLE
# ============================================================

"""
Conditional statements are commonly used in AI applications
for:

- Input validation
- API response handling
- Model prediction decisions
- Confidence thresholds
- Error handling
- Checking whether data exists
"""

confidence = 0.87

if confidence >= 0.80:
    print("High confidence")
elif confidence >= 0.50:
    print("Medium confidence")
else:
    print("Low confidence")