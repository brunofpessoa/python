import numpy as np


def homogeneous_exemple():
    # Homogeneous datasets
    print("\n==========Homogeneous==========\n")
    python_list = [1, 2, 3, 'string']
    array = np.array([1, 2, 3, 'string'])
    print(f"python list: {python_list}\n")
    print(f"inferred numpy array: {array}\n")
    array = np.array([1, 2, 3], dtype=float)
    print(f"typed numpy array: {array}\n")
    # array = np.array([-1, 0, 1], dtype=np.uint16)
    # print(f"overflow: {array}\n")


def multidimensional_exemple():
    print("\n==========Multidimensional==========\n")
    multi_array = np.array([[1, 2, 3], [1, 2, 3]])
    rows, columns = multi_array.shape
    print(f"rows: {rows}, columns: {columns}\n")


def reshape_exemple():
    print("\n==========Reshape==========\n")
    array = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"size: {array.size}\n")
    print(f"original: {array}\n")
    reshaped = array.reshape(1, 6)
    print(f"reshaped: {reshaped}\n")


def transpose_exemple():
    print("\n==========Transpose==========\n")
    array = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"original: {array}\n")
    print(f"transposed: {array.T}\n")


def initializing_exemple():
    # Initializing arrays
    print("\n==========Initializing arrays==========\n")
    print(f"np.arange: {np.arange(0, 100, 20)}\n")
    array = np.zeros((2, 2))
    print(f"filled with zeroes: {array}\n")
    array = np.ones((2, 2))
    print(f"filled with ones: {array}\n")
    array = np.full((2, 2), "OK")
    print(f"filled with whatever you wants: {array}\n")
    array = np.random.random((2, 2))
    print(f"filled with random floats: {array}\n")


def indexing_exemple():
    print("\n==========Indexing==========\n")
    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"sec column: {array[1]}\n")
    print(f"sec column sec value: {array[1, 1]}\n")
    print(f"every first value: {array[:, 0]}\n")
    print(f"last column last but one value: {array[-1, -2]}\n")


def boolean_indexing_exemple():
    print("\n==========Boolean indexing==========\n")
    array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    bool_matrix = array < 3
    print(f"boolean matrix: {bool_matrix}\n")
    print(f"matched values: {array[bool_matrix]}\n")
    # logical_and
    bool_matrix = np.logical_and(array > 3, array < 6)
    print(f"matched values with logical and: {array[bool_matrix]}\n")
    # where
    print("\n==========Where==========\n")
    result = np.where(array < 3, 'x', 'y')
    print(f"result: {result}\n")
    result = np.where(array < 3, "replaced", array)
    print(f"result: {result}\n")


def slice_exemple():
    print("\n==========Slice==========\n")
    array = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    # [start:end:step] start is not included
    print(f"start at 0 and returns everything until index 3: {array[0:3]}\n")
    print(f"everything between index 1 and 6 with step 2: {array[1:6:2]}\n")
    array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(f"apply the rule for each row: {array[:, -1:-3:-1]}\n")


def math_exemple():
    print("\n==========Math==========\n")
    array = np.array([[1, 2], [3, 4]])
    print(f"sum: {array.sum()}\n")
    print(f"sum by column: {array.sum(axis=1)}\n")
    print(f"sum by row: {array.sum(axis=1)}\n")
    print(f"cumulative sum: {array.cumsum()}\n")
    print(f"cumulative sum over row: {array.cumsum(axis=1)}\n")
    print(f"cumulative sum over column: {array.cumsum(axis=0)}\n")

    print(f"product: {array.prod()}\n")
    print(f"cumulative product: {array.cumprod()}\n")
    print(f"cumulative product over row: {array.cumprod(axis=1)}\n")
    print(f"cumulative product over column: {array.cumprod(axis=0)}\n")

    array_a = np.array([[1, 2], [3, 4]])
    array_b = np.array([[5, 6], [7, 8]])
    print(f"sum of two arrays: { array_a + array_b}\n")
    # the same works for all basic operations


def broadcasting_exemple():
    print("\n==========Broadcasting==========\n")
    array_a = np.array([[1, 1, 1, 1],  [2, 2, 2, 2],  [3, 3, 3, 3]])
    array_b = np.array([[0, 1, 2, 3]])
    array_c = np.array([[[1], [2], [3]]])

    # number of rows OR number of columns has to be the same
    print(f"same nº of columns result: {array_a + array_b}\n")
    print(f"same nº of rows result: {array_a + array_c}\n")


if __name__ == "__main__":
    homogeneous_exemple()
    multidimensional_exemple()
    reshape_exemple()
    transpose_exemple()
    initializing_exemple()
    indexing_exemple()
    boolean_indexing_exemple()
    slice_exemple()
    math_exemple()
    broadcasting_exemple()
