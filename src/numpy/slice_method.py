import numpy as np


array = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# [start:end:step] start is not inclusive
zero_to_tree = array[0:3]
one_to_six_two_by_two = array[1:6:2]

print(f"Index zero to tree:\n {zero_to_tree}")
print(f"Index one to six two by two:\n {one_to_six_two_by_two}")

array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
last_two_num_desc = array[:, -1:-3:-1]
print(f"Apply the rule for each row:\n {last_two_num_desc}")
