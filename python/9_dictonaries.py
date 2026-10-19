# ============================================================
# DICTIONARIES IN PYTHON
# ============================================================

"""
DICTIONARY:

A dictionary is a mutable collection that stores data
in key-value pairs.

Key:
Used to access a value.

Value:
The data associated with a key.

Dictionaries are written using curly braces {}.

Keys must be unique and hashable.
Values can be of different data types.
"""


# ============================================================
# 1. CREATING A DICTIONARY
# ============================================================

student = {
    "name": "Rachit",
    "age": 22,
    "course": "BTech CSE"
}

print(student)


# ============================================================
# 2. ACCESSING VALUES
# ============================================================

"""
Use the key to access its associated value.
"""

print(student["name"])  # Rachit
print(student["age"])   # 22

# get() returns None by default if the key is missing.
print(student.get("city"))  # None


# ============================================================
# 3. ADDING AND UPDATING VALUES
# ============================================================

student["city"] = "Kharar"  # Add a new key-value pair
student["age"] = 23          # Update an existing value

print(student)


# ============================================================
# 4. REMOVING ITEMS
# ============================================================

student = {"name": "Rachit", "age": 22, "city": "Kharar"}

student.pop("age")  # Removes the key and returns its value

del student["city"]  # Deletes the key-value pair

print(student)


# ============================================================
# 5. IMPORTANT DICTIONARY METHODS
# ============================================================

student = {
    "name": "Rachit",
    "age": 22,
    "course": "BTech CSE"
}

print(student.keys())    # All keys
print(student.values())  # All values
print(student.items())   # Key-value pairs

# update() adds or updates key-value pairs.
student.update({"age": 23, "city": "Kharar"})

# clear() removes all items.
# student.clear()


# ============================================================
# 6. LOOPING THROUGH A DICTIONARY
# ============================================================

student = {"name": "Rachit", "age": 22}

# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through keys and values
for key, value in student.items():
    print(key, value)


# ============================================================
# 7. CHECKING WHETHER A KEY EXISTS
# ============================================================

"""
'in' checks keys by default, not values.
"""

student = {"name": "Rachit", "age": 22}

print("name" in student)  # True
print("city" in student)  # False

print("Rachit" in student.values())  # True


# ============================================================
# 8. NESTED DICTIONARIES
# ============================================================

"""
A dictionary can contain another dictionary.
"""

student = {
    "name": "Rachit",
    "marks": {
        "Python": 90,
        "SQL": 85
    }
}

print(student["marks"]["Python"])  # 90


# ============================================================
# 9. IMPORTANT POINTS
# ============================================================

"""
1. Dictionaries store key-value pairs.
2. Keys must be unique and hashable.
3. Values can have different data types.
4. Dictionaries are mutable.
5. Access values using keys.
6. Missing keys with [] raise KeyError.
7. get() safely handles missing keys by returning None
   by default, or a supplied default value.
8. in checks keys by default.
9. Dictionaries preserve insertion order in Python 3.7+.
10. Keys must be hashable; strings and integers are common keys.
"""


# ============================================================
# 10. AI ENGINEER RELEVANCE
# ============================================================

"""
Dictionaries are commonly used for:

1. API responses in JSON-like formats.
2. Model configuration.
3. Storing prediction results.
4. Organizing structured data.
5. Tracking labels and values.
"""

prediction = {
    "label": "cat",
    "confidence": 0.95
}

print(prediction["label"])       # cat
print(prediction["confidence"])  # 0.95

if prediction["confidence"] >= 0.90:
    print("High-confidence prediction")