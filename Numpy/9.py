# Advanced NumPy: Inserting and Appending Elements
import numpy as np

# 1. Create a 1D array
arr = np.array([10, 20, 30, 40, 50])
print(arr)
# Output: [10 20 30 40 50]


# 2. Insert an element into a 1D array
new_arr = np.insert(arr, 2, 23)
print(new_arr)
# Output: [10 20 23 30 40 50]
# Inserts 23 at index 2, before 30.


# 3. Create a 2D array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(arr_2d)
# Output:
# [[1 2 3]
#  [4 5 6]]


# 4. Insert a new row (axis=0)
new_arr_2d = np.insert(arr_2d, 1, [7, 8, 9], axis=0)
print(new_arr_2d)
# Output:
# [[1 2 3]
#  [7 8 9]
#  [4 5 6]]
# axis=0 refers to rows; inserts [7, 8, 9] at row index 1.


# 5. Insert a new column (axis=1)
new_arr_2d2 = np.insert(arr_2d, 1, [7, 8], axis=1)
print(new_arr_2d2)
# Output:
# [[1 7 2 3]
#  [4 8 5 6]]
# axis=1 refers to columns; inserts 7 and 8 at column index 1.


# 6. Insert elements into a flattened array (axis=None)
new_arr_flat = np.insert(arr_2d, 1, [7, 8], axis=None)
print(new_arr_flat)
# Output: [1 7 8 2 3 4 5 6]
# axis=None flattens the array before inserting elements at index 1.


# 7. Append an element to a 1D array
new_arr = np.append(arr, 60)
print(new_arr)
# Output: [10 20 30 40 50 60]
# Adds 60 to the end of the array.


# --------------------------------------------------
# REVISION NOTES
# --------------------------------------------------
# np.insert(arr, index, value) -> Inserts element(s) at a position.
# np.append(arr, value)       -> Adds element(s) to the end.
# axis=0                     -> Row direction in a 2D array.
# axis=1                     -> Column direction in a 2D array.
# axis=None                  -> Flattens the array before insertion.
# Both insert() and append() return new arrays.
# The original array remains unchanged.
