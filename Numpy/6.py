import numpy as np

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# --------------------------------------------------
# 1. INDEXING: Access individual elements
# --------------------------------------------------

print(arr[0])     # Output: 10 (first element; index starts from 0)
print(arr[5])     # Output: 60 (element at index 5)
print(arr[-1])    # Output: 100 (last element)
print(arr[-2])    # Output: 90 (second-last element)

# Positive indexing:  0   1   2   3   4   5 ...
# Elements:           10  20  30  40  50  60 ...
# Negative indexing: -10 -9  -8  -7  -6  -5 ...


# --------------------------------------------------
# 2. BASIC SLICING: Extract a portion of an array
# --------------------------------------------------

print(arr[1:5])   # Output: [20 30 40 50]
                  # Starts at index 1 and stops before index 5

print(arr[:4])    # Output: [10 20 30 40]
                  # Starts from the beginning; stops before index 4

print(arr[4:])    # Output: [50 60 70 80 90 100]
                  # Starts at index 4 and continues to the end

print(arr[:])     # Output: [10 20 30 40 50 60 70 80 90 100]
                  # Selects the entire array


# --------------------------------------------------
# 3. SLICING WITH STEP
# Syntax: arr[start:stop:step]
# --------------------------------------------------

print(arr[::2])   # Output: [10 30 50 70 90]
                  # Selects every second element, starting at index 0

print(arr[1::2])  # Output: [20 40 60 80 100]
                  # Starts at index 1 and selects every second element

print(arr[::3])   # Output: [10 40 70 100]
                  # Selects every third element

print(arr[2:7:2]) # Output: [30 50 70]
                  # Starts at index 2, stops before index 7, step = 2


# --------------------------------------------------
# 4. NEGATIVE SLICING
# --------------------------------------------------

print(arr[-4:])   # Output: [70 80 90 100]
                  # Selects the last four elements

print(arr[:-2])   # Output: [10 20 30 40 50 60 70 80]
                  # Selects all elements except the last two

print(arr[-5:-1]) # Output: [60 70 80 90]
                  # Starts at the fifth-last element and stops before
                  # the last element


# --------------------------------------------------
# 5. REVERSING AN ARRAY
# --------------------------------------------------

print(arr[::-1])
# Output: [100 90 80 70 60 50 40 30 20 10]
# A step of -1 traverses the array backwards.

print(arr[::-2])
# Output: [100 80 60 40 20]
# Traverses backwards, selecting every second element.


# --------------------------------------------------
# 6. MODIFYING ELEMENTS USING INDEXING
# --------------------------------------------------

arr[0] = 999
print(arr)
# Output: [999 20 30 40 50 60 70 80 90 100]
# Changes the element at index 0 to 999.


# --------------------------------------------------
# 7. MODIFYING A SLICE
# --------------------------------------------------

arr[1:4] = 0
print(arr)
# Output: [999 0 0 0 50 60 70 80 90 100]
# Replaces elements at indices 1, 2, and 3 with 0.

