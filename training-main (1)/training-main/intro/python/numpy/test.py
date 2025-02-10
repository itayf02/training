import pandas as pd
import numpy as np

x = np.arange(1,11).reshape(2,5)
x[0:2,2:4] = 99
print(x)