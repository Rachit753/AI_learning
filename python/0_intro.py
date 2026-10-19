# Python is a dynamically typed and interpreted language.

# Dynamically Typed:
# Python determines/checks the type of an object at runtime.
# We don't need to explicitly declare the variable's type.

# Example:
x = 10        # x refers to an int object
x = "Hello"   # now x refers to a str object
print(x)

# Interpreted:
# Python is traditionally called an interpreted language because
# Python bytecode is executed by the Python runtime/interpreter
# rather than the .py source code being directly executed as
# native machine code.


"""
FLOW OF CODE

                Python Source Code (.py)
                         |
                         | compile
                         v
                  Python Bytecode
                         |
                         v
                Python Runtime / PVM
                         |
                         | execute bytecode
                         v
             Underlying native execution
                         |
                         v
                        CPU
"""


# IMPORTANT:
# "Python executes code line-by-line" is an oversimplification.
# CPython compiles the source code into bytecode and then
# executes that bytecode.

# CPython:
# Source code -> bytecode -> CPython runtime/interpreter executes it.

# PyPy:
# Uses a JIT (Just-In-Time) compiler to compile frequently executed
# code into native machine code at runtime.


