# 1. Creating a Python List
# Output: [1, 2, 3, 4, 5]
# Explanation: A Python list stores multiple elements in a single variable.
python_list = [1, 2, 3, 4, 5]
print("Python List:", python_list)


# 2. Creating a NumPy Array
# Output: [1 2 3 4 5]
# Explanation: np.array() converts a list into a NumPy array.
# NumPy arrays support efficient mathematical and numerical operations.
import numpy as np

numpy_array = np.array([1, 2, 3, 4, 5])
print("Numpy Array:", numpy_array)


# 3. Creating an Array of Zeros
# Output: [0. 0. 0.]
# Explanation: np.zeros(3) creates a 1D array containing 3 zeros.
# By default, the elements are floating-point numbers (usually float64).
import numpy as np

zeros_array = np.zeros(3)
print("Zeros Array:", zeros_array)


# 4. Creating a 3x3 Array of Ones
# Output:
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]
# Explanation: np.ones((3, 3)) creates a 2D array with 3 rows and 3 columns.
# Every element is initialized to 1.
import numpy as np

ones_array = np.ones((3, 3))
print("Ones Array:", ones_array)


# 5. Creating an Array Filled with a Specific Value
# Output:
# [[7 7]
#  [7 7]]
# Explanation: np.full((2, 2), 7) creates a 2D array with 2 rows and 2 columns.
# Every element is initialized to 7.
import numpy as np

filled_array = np.full((2, 2), 7)
print("Filled Array:", filled_array)


# 1. Creating an Array Using np.arange()
# Output: [1 3 5 7 9]
# Explanation:
# np.arange(start, stop, step) generates values in a sequence.
# start = 1  -> Starting value (included)
# stop = 10  -> Ending limit (excluded)
# step = 2   -> Increment by 2 each time
# Therefore, the array contains 1, 3, 5, 7, 9.

import numpy as np

arr = np.arange(1, 10, 2)  # start, stop, step
print("Array:", arr)


# 2. Creating an Identity Matrix Using np.eye()
# Output:
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]
# Explanation:
# np.eye(5) creates a 5x5 identity matrix.
# The diagonal elements are 1, and all other elements are 0.
# By default, the elements are floating-point numbers.
# Identity matrices are useful in linear algebra and machine learning.

import numpy as np

identity_matrix = np.eye(5)
print(identity_matrix)
