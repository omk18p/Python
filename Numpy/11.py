import numpy as np

# 1. Vertical Stacking (vstack)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(np.vstack((arr1, arr2)))
# Output:
# [[1 2 3]
#  [4 5 6]]
# Explanation: Stacks arrays vertically (row-wise).
# Converts the two 1D arrays into a 2D array with 2 rows.


# 2. Horizontal Stacking (hstack)
print(np.hstack((arr1, arr2)))
# Output: [1 2 3 4 5 6]
# Explanation: Joins arrays horizontally.
# For 1D arrays, it concatenates their elements into one array.


# 3. Splitting an Array into Equal Parts
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print(np.split(arr, 5))
# Output:
# [array([10, 20]), array([30, 40]), array([50, 60]),
#  array([70, 80]), array([ 90, 100])]
# Explanation: Splits the array into 5 equal-sized sub-arrays.
# Each sub-array contains 2 elements because 10 / 5 = 2.


# --------------------------------------------------
# REVISION NOTES
# --------------------------------------------------
# np.vstack((arr1, arr2)) -> Stacks arrays vertically (row-wise).
# np.hstack((arr1, arr2)) -> Stacks arrays horizontally.
# np.split(arr, n)        -> Splits an array into n equal sections.
# np.split() requires equal division when an integer section count is used.
# vstack() and hstack() return new arrays; original arrays remain unchanged.
