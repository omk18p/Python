import numpy as np

# 1. Creating a 2D NumPy Array
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# Explanation:
# np.array() creates a NumPy array from the given nested lists.
# This array contains 3 rows and 3 columns, so it is a 2D array.

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])


# 2. Checking the Shape of an Array
# Output: (3, 3)
# Explanation:
# shape returns the size of the array along each dimension.
# Here, (3, 3) means 3 rows and 3 columns.

print(arr.shape)


# 3. Checking the Shape of the First Row
# Output: (3,)
# Explanation:
# arr[0] selects the first row: [1, 2, 3].
# Its shape is (3,), meaning it is a 1D array containing 3 elements.
# The comma indicates that the shape is a tuple.

print(arr[0].shape)


# 4. Checking the Total Number of Elements
# Output: 9
# Explanation:
# size returns the total number of elements in the array.
# Here, 3 rows × 3 columns = 9 elements.

print(arr.size)


# 5. Checking the Number of Dimensions
# Output: 2
# Explanation:
# ndim returns the number of dimensions (axes) of the array.
# This array has two dimensions: rows and columns.

print(arr.ndim)


# 6. Creating a 3D NumPy Array
# Output:
# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]
# Explanation:
# This array contains 2 matrices.
# Each matrix has 2 rows and 2 columns.
# Its shape is (2, 2, 2), and it has 3 dimensions.

arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])


# 7. Checking the Dimensions of a 3D Array
# Output: 3
# Explanation:
# ndim returns 3 because arr3 has three axes:
# 1. Matrix index
# 2. Row index
# 3. Column index

print(arr3.ndim)


# 8. Checking the Data Type of Array Elements
# Output: int64 (may vary depending on the platform)
# Explanation:
# dtype tells us the data type of the elements stored in the array.
# Since all the values are integers, NumPy typically uses an integer dtype.

print(arr3.dtype)
