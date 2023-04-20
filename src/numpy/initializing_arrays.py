import numpy as np


array_range = np.arange(0, 100, 20)
array_zeros = np.zeros((2, 2))
array_ones = np.ones((2, 2))
array_full = np.full((2, 2), "OK")
array_random = np.random.random((2, 2))

print(f"np.arange():\n {array_range}")
print(f"np.zeros():\n {array_zeros}")
print(f"np.ones():\n {array_ones}")
print(f"np.full():\n {array_full}")
print(f"np.random.random():\n {array_random}")
