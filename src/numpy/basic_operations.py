import numpy as np


array = np.array([[1, 2], [3, 4]])

print(f"sum: {array.sum()}")
print(f"sum by column: {array.sum(axis=1)}")
print(f"sum by row: {array.sum(axis=1)}")
print(f"cumulative sum: {array.cumsum()}")
print(f"cumulative sum over row: {array.cumsum(axis=1)}")
print(f"cumulative sum over column: {array.cumsum(axis=0)}")

print(f"product: {array.prod()}")
print(f"cumulative product: {array.cumprod()}")
print(f"cumulative product over row: {array.cumprod(axis=1)}")
print(f"cumulative product over column: {array.cumprod(axis=0)}")

array_a = np.array([[1, 2], [3, 4]])
array_b = np.array([[5, 6], [7, 8]])

print(f"sum of two arrays: { array_a + array_b}")
# the same works for all basic operations
