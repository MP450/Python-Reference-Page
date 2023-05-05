# Sources: docs.python.org, automatetheboringstuffwithpython.com

# Basic Data Types

# Integer: 1
# Float: 1.94
# String: "Python!"
# Empty String: ""

# Print string to console
print("Hello World")

##########

# Basic math functions
print(1 + 2)
print(1 - 2)
print(10 * 5)
print(10 / 5)
print(10 ** 5) # Exponent
print(10 // 5) # Integer division
print(10 % 5) # Modulus/remainder

print(5 + 9.55 * (5 - 2) / 5 + 2 ** 2)

##########
# Variable Rules
# - No spaces
# - Letters, numbers, and underscore (_) only
# - Cannot begin with number
# - Case sensitive

##########
# Concatenate strings
FirstName = "John"
LastName = "Doe"
print(FirstName + LastName)
print(FirstName + " " + LastName) # With space in between names
print(FirstName * 5) # Print name 5 times

##########
# Basic Functions
"""
print()
input()
len()
str()
int()
float()
round()
abs()
"""
##########
"""
Boolean Values:
True
False

Comparison Operators:
==
!=
<
>
<=
>=

"""
print(42 == 42)
print(42 =="42")

print(2 != 5)
print(2 != 2)

print(5 < 10)
print(5 <= 5.0)

"""
Logical Operators:
and
or
not

"""
print((4 < 6) and (6 < 7))
print((4 < 6) and (8 < 7))

##########

# Fibonacci sequence
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b

