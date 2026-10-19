# ============================================================
# MODULES, PACKAGES AND LIBRARIES IN PYTHON
# ============================================================

"""
MODULE:
A module is a Python file (.py) containing reusable code,
such as functions, variables, and classes.

PACKAGE:
A package organizes related Python modules into directories.

LIBRARY:
A library is a collection of reusable code designed
to perform specific tasks. It may contain multiple
modules and packages.
"""


# ============================================================
# 1. MODULE
# ============================================================

"""
Example:

calculator.py
"""

# calculator.py

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b


"""
Importing a module in another Python file.
"""

# main.py
"""
import calculator

print(calculator.add(10, 20))
print(calculator.multiply(5, 4))
"""

# Output:
# 30
# 20


# ============================================================
# 2. DIFFERENT WAYS TO IMPORT
# ============================================================

# Import the complete module
import math

print(math.sqrt(25))  # 5.0


# Import a specific function
from math import sqrt

print(sqrt(36))  # 6.0


# Import using an alias
import math as m

print(m.factorial(5))  # 120


# ============================================================
# 3. PACKAGE
# ============================================================

"""
Example folder structure:

my_project/
    main.py
    calculator/
        __init__.py
        basic.py
        advanced.py

Here:
- basic.py is a module.
- advanced.py is a module.
- calculator/ is a regular Python package.

__init__.py is commonly used to mark a regular package.
Modern Python also supports namespace packages without it.
"""


# Importing a function from a package module

"""
from calculator.basic import add

print(add(10, 20))
"""

# ============================================================
# 4. LIBRARIES
# ============================================================

"""
Libraries provide reusable functionality for specific tasks.

Examples:

NumPy       -> Numerical computing and arrays
Pandas      -> Data analysis and tabular data
Matplotlib  -> Data visualization
Scikit-learn -> Machine learning
PyTorch     -> Deep learning
"""

# Example: NumPy

import numpy as np

numbers = np.array([10, 20, 30])

print(numbers)


# Example: Pandas

import pandas as pd

data = {"Name": ["Aman", "Rachit"], "Score": [85, 90]}

df = pd.DataFrame(data)

print(df)


# ============================================================
# 5. INSTALLING VS IMPORTING
# ============================================================

"""
INSTALL:
Makes a third-party library available in your environment.

IMPORT:
Allows your Python program to use its code.

Standard-library modules, such as math, usually do not
need to be installed separately.
"""

# Run this command in the VS Code terminal:
# python -m pip install numpy

# Then use it in your Python file:
import numpy as np


# ============================================================
# 6. AI ENGINEER RELEVANCE
# ============================================================

"""
Modules, packages and libraries help AI Engineers:

1. Reuse existing code.
2. Organize large AI projects.
3. Process data using NumPy and Pandas.
4. Build ML models using Scikit-learn.
5. Develop deep learning models using PyTorch.
6. Avoid rewriting functionality from scratch.
"""


# ============================================================
# QUICK REVISION
# ============================================================

"""
MODULE:
A Python file containing reusable code.

PACKAGE:
Organizes related modules into a directory structure.

LIBRARY:
A broader collection of reusable functionality.

import:
Used to access code from modules and packages.

pip:
A tool commonly used to install Python packages.

IMPORTANT:
A library may contain multiple packages and modules.
The terms library and package are sometimes used loosely.
"""