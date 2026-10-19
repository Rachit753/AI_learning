# ============================================================
# STRINGS IN PYTHON
# ============================================================

"""
STRING:

A string is a sequence of characters used to represent text.

Strings are written using single quotes, double quotes,
or triple quotes.

Strings are immutable, meaning their characters cannot
be changed directly after creation.
"""


# ============================================================
# 1. CREATING STRINGS
# ============================================================

name = "Rachit"
language = 'Python'
message = """Welcome to Python"""

print(name)
print(language)
print(message)


# ============================================================
# 2. ACCESSING CHARACTERS
# ============================================================

"""
Indexing starts from 0.
Negative indexing starts from -1.
"""

text = "Python"

print(text[0])   # P
print(text[2])   # t
print(text[-1])  # n


# ============================================================
# 3. STRING SLICING
# ============================================================

"""
Syntax: string[start:stop:step]

The stop index is excluded.
"""

text = "Python"

print(text[0:3])  # Pyt
print(text[2:])   # thon
print(text[::-1]) # nohtyP


# ============================================================
# 4. STRING LENGTH
# ============================================================

"""
len() returns the number of characters in a string.
"""

text = "Python"

print(len(text))  # 6


# ============================================================
# 5. COMMON STRING METHODS
# ============================================================

text = "  Hello Python  "

print(text.upper())       # "  HELLO PYTHON  "
print(text.lower())       # "  hello python  "
print(text.strip())       # "Hello Python"
print(text.replace("Python", "AI"))
print(text.find("Python"))  # 8


# ============================================================
# 6. SPLIT AND JOIN
# ============================================================

"""
split() converts a string into a list.
join() combines strings using a separator.
"""

text = "Python is easy"

words = text.split()
print(words)
# ['Python', 'is', 'easy']

result = "-".join(words)
print(result)
# Python-is-easy


# ============================================================
# 7. STRING CONCATENATION
# ============================================================

"""
The + operator joins strings together.
"""

first_name = "Rachit"
last_name = "Chauhan"

full_name = first_name + " " + last_name

print(full_name)
# Rachit Chauhan


# ============================================================
# 8. STRING REPETITION
# ============================================================

text = "Hi "

print(text * 3)

# Output:
# Hi Hi Hi


# ============================================================
# 9. MEMBERSHIP OPERATORS
# ============================================================

"""
in checks whether a substring exists in a string.
"""

text = "Python for AI"

print("Python" in text)      # True
print("Java" not in text)    # True


# ============================================================
# 10. STRING FORMATTING
# ============================================================

"""
f-strings allow variables and expressions inside strings.
"""

name = "Rachit"
age = 22

print(f"My name is {name} and I am {age} years old.")


# ============================================================
# 11. STRING IMMUTABILITY
# ============================================================

"""
Strings are immutable.
Individual characters cannot be changed directly.
"""

text = "Python"

# text[0] = "J"  # TypeError

# Create a new string instead:
text = "J" + text[1:]

print(text)  # Jython


# ============================================================
# 12. LOOPING THROUGH A STRING
# ============================================================

text = "AI"

for character in text:
    print(character)

# Output:
# A
# I


# ============================================================
# 13. AI ENGINEER RELEVANCE
# ============================================================

"""
Strings are important in AI applications for:

1. Processing user prompts.
2. Cleaning text data.
3. Working with API responses.
4. Preparing text for NLP.
5. Handling model outputs.
"""

prompt = "  Explain Machine Learning  "

clean_prompt = prompt.strip()

print(clean_prompt)
# Explain Machine Learning


# ============================================================
# QUICK REVISION
# ============================================================

"""
1. Strings represent text.
2. Strings are immutable.
3. Indexing starts from 0.
4. Slicing extracts part of a string.
5. len() returns the string length.
6. upper() and lower() change letter case.
7. strip() removes surrounding whitespace.
8. split() converts a string into a list.
9. join() combines strings.
10. f-strings insert values into strings.
"""