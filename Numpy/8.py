
import numpy as np

# 1. Reshaping an Array
# Converts a 1D array into a 2D array with 2 rows and 3 columns.
arr = np.array([1, 2, 3, 4, 5, 6])

reshaped_arr = arr.reshape(2, 3)
print(reshaped_arr)

# Output:
# [[1 2 3]
#  [4 5 6]]
# Note: The total number of elements must remain the same (2 * 3 = 6).


# 2. Flattening an Array
# Converts a multidimensional array into a 1D array.
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6]])

flattened_arr = array_2d.flatten()
print(flattened_arr)

# Output: [1 2 3 4 5 6]
# Note: flatten() always returns a copy of the array.


# 3. Raveling an Array
# Converts a multidimensional array into a 1D array.
raveled_arr = array_2d.ravel()
print(raveled_arr)

# Output: [1 2 3 4 5 6]
# Note: ravel() returns a view when possible; otherwise, it returns a copy.
# Changes to a view can affect the original array.
