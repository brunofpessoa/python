import numpy as np


array_a = np.array([[1, 1, 1, 1],  [2, 2, 2, 2],  [3, 3, 3, 3]])
array_b = np.array([[0, 1, 2, 3]])
array_c = np.array([[[1], [2], [3]]])

# number of rows OR number of columns has to be the same
print(f"same nº of columns result:\n {array_a + array_b}")
print(f"same nº of rows result:\n {array_a + array_c}")
