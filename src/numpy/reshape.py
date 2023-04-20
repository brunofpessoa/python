import numpy as np


array = np.array([[1, 2, 3], [4, 5, 6]])

print(f"array size: {array.size}")
print(f"original array:\n {array}")

reshaped = array.reshape(1, 6)

print(f"reshaped array:\n {reshaped}")
