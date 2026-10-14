import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# 1. Fancy Indexing
# Access multiple elements using a list of indices.
print(arr[[0, 3, 5]])  # Output: [10 40 60]
# Explanation: Selects elements at indices 0, 3, and 5.
# Note: Indices start from 0.


# 2. Boolean Masking
# Select elements that satisfy a given condition.
print(arr[arr > 50])  # Output: [60 70 80 90 100]
# Explanation: arr > 50 creates a Boolean array (True/False).
# Only elements where the condition is True are selected.


# 3. Boolean Masking with Multiple Conditions
print(arr[(arr > 30) & (arr < 80)])
# Output: [40 50 60 70]
# Explanation: Selects elements greater than 30 AND less than 80.
# Use & for AND and | for OR; put each condition in parentheses.


# 4. Select Elements Using a Boolean Array
mask = arr % 20 == 0
print(mask)
# Output: [False True False True False True False True False True]
# Explanation: Checks which elements are divisible by 20.

print(arr[mask])
# Output: [20 40 60 80 100]
# Explanation: Selects elements wherever the mask is True.
