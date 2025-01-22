def gen():
    yield from range(5)

g = gen()
print(next(g))
print(next(g))