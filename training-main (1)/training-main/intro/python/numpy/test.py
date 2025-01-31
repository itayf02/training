import numpy as np

Z = np.random.randint(0, 10, size=(6,6))
# print(Z)
# print(Z[1:-1, 1:-1])
print(np.indices((4,4,4)).shape)