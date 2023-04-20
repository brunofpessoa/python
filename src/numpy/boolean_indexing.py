import numpy as np


array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
bool_matrix = array < 3
filtered_values = array[bool_matrix]

print(f"boolean matrix:\n {bool_matrix}")
print(f"filtered values:\n {filtered_values}")

# logical_and
bool_matrix = np.logical_and(array > 3, array < 6)
filtered_values = array[bool_matrix]

print(f"filtered values:\n {filtered_values}")
