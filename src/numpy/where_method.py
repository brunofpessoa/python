import numpy as np


array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

result = np.where(array < 3, 'x', 'y')
print(f"result:\n {result}")

result = np.where(array < 3, "replaced", array)
print(f"result:\n {result}")
