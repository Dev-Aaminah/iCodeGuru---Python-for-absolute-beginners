# Identity operators in Python are used to compare the memory locations of two objects. There are two identity operators in Python:

# is
# is not
# 1. is Operator
# The is operator checks if two variables point to the same object in memory. It returns True if they do, and False otherwise.
x = 10.0
y= 10.0
print(y is x)


# 2. is not Operator
# The is not operator checks if two variables do not point to the same object in memory. It returns True if they do not, and False otherwise.
anotherX = 10.0
anotherY = 10.5
print(anotherX is not anotherY)