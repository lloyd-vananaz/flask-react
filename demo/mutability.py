# Mutability in Python

x = 1000
# Python creates an 'INT 1000' object and reference 'x' to that 'INT 1000' object.
print(id(x), ' - ID of x = 1000')

x = 500
# Since integers are immutable, Python creates a new 'INT 500' object and reference 'x' to the new 'INT 500' object.
# The old 'INT 1000' will be garbage collected at some point.
print(id(x), ' - ID of reassigned x = 500')

y = x
# Python will have 'y' reference to the same object as 'x'.
print(id(y), ' - ID of y = x')
print('Is the ID of y and x the same?', id(y) == id(x))

x = 3000
# Python creates a new 'INT 3000' object and reference 'x' to the new 'INT 3000' object.
# The old 'INT 500' will not be garbage collected yet since 'y' is still referencing to that object.
print(id(x), ' - ID of reassigned x = 3000')
print('Is the ID of y and x the same?', id(y) == id(x))

r = [2, 4, 6]
# Python creates a new list object having 2, 4 and 6 and reference 'r' to the new list object.
print(id(r), ' - ID of r = [2, 4, 6]')

s = r
# Python will have 's' reference to the same object as 'r'.
print(id(s), ' - ID of s = r')

s[1] = 17
# Since lists are mutable, Python updates the index 1 of the list making the list [2, 17, 6].
# 'r' will also be affected since 's' and 'r' are referencing to the same list object.
print(s, ' - Data in s')
print(r, ' - Data in r')
print('Is the ID of r and s the same?', id(r) == id(s))
print('Are the data in r and s the same?', r == s)