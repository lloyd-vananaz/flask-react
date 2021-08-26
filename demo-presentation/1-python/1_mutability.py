# Mutability in Python

x = 1000
print(id(x), ' - ID of x = 1000')

x = 500
print(id(x), ' - ID of reassigned x = 500')

y = x
print(id(y), ' - ID of y = x')
print('Is the ID of y and x the same?', id(y) == id(x))

x = 3000
print(id(x), ' - ID of reassigned x = 3000')
print('Is the ID of y and x the same?', id(y) == id(x))

r = [2, 4, 6]
print(id(r), ' - ID of r = [2, 4, 6]')

s = r
print(id(s), ' - ID of s = r')

s[1] = 17
print(s, ' - Data in s')
print(r, ' - Data in r')
print('Is the ID of r and s the same?', id(r) == id(s))
print('Are the data in r and s the same?', r == s)