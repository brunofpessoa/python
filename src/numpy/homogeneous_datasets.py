import numpy as np


python_list = [1, 2, 3, 'string']
np_array = np.array([1, 2, 3, 'string'])
dtype_array = np.array([1, 2, 3], dtype=float)

print(f"python list: {python_list}")
print(f"inferred numpy array: {np_array}")
print(f"typed numpy array: {dtype_array}")

# dtype_array = np.array([-1, 0, 1], dtype=np.uint16)
# print(f"overflow: {dtype_array}\n")
