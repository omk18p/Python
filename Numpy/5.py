import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Calculate the sum of all elements
print(np.sum(arr))     # Output: 550

# Calculate the average of all elements
print(np.mean(arr))    # Output: 55.0

# Find the middle value of the sorted elements
print(np.median(arr))  # Output: 55.0

# Measure the spread of values around the mean
print(np.std(arr))     # Output: 28.722813232690143

# Calculate the average squared deviation from the mean
print(np.var(arr))     # Output: 825.0

# Find the smallest element
print(np.min(arr))     # Output: 10

# Find the largest element
print(np.max(arr))     # Output: 100
