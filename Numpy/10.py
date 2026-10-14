# Advanced NumPy: Concatenation and Deletion
import numpy as np

# 1. Concatenate two 1D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

new_arr = np.concatenate((arr1, arr2))
print(new_arr)
# Output: [1 2 3 4 5 6]
# Combines two arrays into one array.
# For 1D arrays, concatenate joins elements sequentially.


# 2. Delete an element from a 1D array
arr = np.array([10, 20, 30, 40, 50])
print(arr)
# Output: [10 20 30 40 50]

new_ar = np.delete(arr, 1)
print(new_ar)
# Output: [10 30 40 50]
# Deletes the element at index 1 (value 20).
# The original array remains unchanged.


# 3. Create a 2D array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(arr_2d)
# Output:
# [[1 2 3]
#  [4 5 6]]


# 4. Delete a column (axis=1)
new_arr_2d = np.delete(arr_2d, 1, axis=1)
print(new_arr_2d)
# Output:
# [[1 3]
#  [4 6]]
# axis=1 refers to columns.
# Deletes column index 1 (values 2 and 5).


# 5. Delete a row (axis=0)
new_arr_2d = np.delete(arr_2d, 1, axis=0)
print(new_arr_2d)
# Output:
# [[1 2 3]]
# axis=0 refers to rows.
# Deletes row index 1 ([4, 5, 6]).


# --------------------------------------------------
# REVISION NOTES
# --------------------------------------------------
# np.concatenate((arr1, arr2)) -> Joins arrays together.
# np.delete(arr, index)        -> Deletes an element by index.
# np.delete(arr, index, axis=0)-> Deletes a row in a 2D array.
# np.delete(arr, index, axis=1)-> Deletes a column in a 2D array.
# axis=0 -> Row direction; axis=1 -> Column direction.
# np.delete() returns a new array; the original stays unchanged.
# For concatenation along a specified axis, array shapes must match
# along all other axes.
