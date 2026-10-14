import numpy as np

# Create an array of floating-point numbers
arr = np.array([1.2, 2.3, 3.4, 4.5])
print(arr.dtype)  # Output: float64 (data type)

# Convert float values to integers
int_arr = arr.astype(int)
print(int_arr)  # Output: [1 2 3 4] (decimal parts are truncated)

# Check the new data type
print(int_arr.dtype)  # Output: int64 (may vary by platform)
