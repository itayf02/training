import copy
a = [[1,2,3]]
b = copy.copy(a)
print(id(a))
print(id(b))

c = A()
d = copy.copy(c)

print(id(c))
print(id(d))

c.x = 20
print(c.x)
print(d.x)