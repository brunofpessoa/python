import numpy as np


array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(f"second column: {array[1]}")
print(f"second column second value: {array[1, 1]}")
print(f"every first value: {array[:, 0]}")
print(f"last column last but one value: {array[-1, -2]}")
