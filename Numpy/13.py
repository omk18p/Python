
# Handling Missing Values and Infinite Values in NumPy
import numpy as np

# 1. Create an array containing a missing value (NaN)
arr = np.array([1, 2, np.nan, 4, 5])

# Check which elements are NaN
print(np.isnan(arr))
# Output: [False False  True False False]
# Explanation: np.isnan() returns True for NaN values and False otherwise.


# 2. Comparing NaN values
print(np.nan == np.nan)
# Output: False
# Explanation: NaN is not equal to itself.
# Use np.isnan() to check for NaN instead of ==.


# 3. Replace NaN with a specific value
arr = np.nan_to_num(arr, nan=110)
print(arr)
# Output: [  1.   2. 110.   4.   5.]
# Explanation: Replaces NaN with 110.
# np.nan_to_num() returns a cleaned array; by default, it does not
# modify the original array.


# 4. Detect Infinite Values
arr = np.array([1, 2, np.inf, -np.inf, 5])

print(np.isinf(arr))
# Output: [False False  True  True False]
# Explanation: np.isinf() returns True for positive or negative infinity.


# 5. Replace Infinite Values
cleaned_arr = np.nan_to_num(arr, posinf=100, neginf=-100)
print(cleaned_arr)
# Output: [   1.    2.  100. -100.    5.]
# Explanation:
# posinf=100 replaces positive infinity with 100.
# neginf=-100 replaces negative infinity with -100.


# --------------------------------------------------
# REVISION NOTES
# --------------------------------------------------
# np.nan        -> Represents a missing/undefined numerical value.
# np.isnan(arr) -> Detects NaN values.
# np.nan == np.nan -> False; use np.isnan() instead.
# np.nan_to_num(arr, nan=110) -> Replaces NaN with 110.
# np.inf        -> Positive infinity.
# -np.inf       -> Negative infinity.
# np.isinf(arr) -> Detects positive and negative infinity.
# posinf=100    -> Replaces positive infinity with 100.
# neginf=-100   -> Replaces negative infinity with -100.
# Note: np.nan_to_num() returns a new array by default.
