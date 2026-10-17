# Broadcasting and Vectorization in NumPy
import numpy as np

# 1. Without Broadcasting and Vectorization
# Calculate the final price after a 10% discount using a loop.
prices = [100, 200, 300, 400, 500]
discounts_percent = 10
final_prices = []

for price in prices:
    final_prices.append(price - (price * discounts_percent / 100))

print(final_prices)
# Output: [90.0, 180.0, 270.0, 360.0, 450.0]
# Explanation: A loop calculates the discount for each price individually.


# 2. With Broadcasting and Vectorization
# Calculate discounts for all prices using NumPy operations.
prices = np.array([100, 200, 300, 400, 500])
discounts_percent = 10

final_prices = prices - (prices * discounts_percent / 100)
print(final_prices)
# Output: [ 90. 180. 270. 360. 450.]
# Explanation: NumPy applies the calculation to every element without an
# explicit Python loop (vectorization).
# The scalar 10 is automatically applied to every element (broadcasting).


# 3. Scalar Broadcasting
# Multiply every array element by a single value.
arr = np.array([100, 200, 300, 400, 500])
result = arr * 300

print(result)
# Output: [ 30000  60000  90000 120000 150000]
# Explanation: The scalar 300 is broadcast to every element of the array.


# 4. Broadcasting Between a Matrix and a Vector
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

vector = np.array([1, 2, 3])
result = matrix + vector

print(result)
# Output:
# [[ 2  4  6]
#  [ 5  7  9]
#  [ 8 10 12]]
# Explanation: The vector is added to every row of the matrix.
# Shapes: matrix = (3, 3), vector = (3,).
# Broadcasting makes these shapes compatible.


# 5. Without NumPy Vectorization
# Add corresponding elements using a list comprehension.
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

result = [x + y for x, y in zip(list1, list2)]
print(result)
# Output: [11, 22, 33, 44, 55]
# Explanation: zip() pairs corresponding elements, and the list
# comprehension adds each pair.


# 6. With NumPy Vectorization
# Add corresponding elements directly.
list1 = np.array([1, 2, 3, 4, 5])
list2 = np.array([10, 20, 30, 40, 50])

result = list1 + list2
print(result)
# Output: [11 22 33 44 55]
# Explanation: NumPy adds corresponding elements without an explicit loop.


# 7. Vectorized Multiplication
arr = np.array([1, 2, 3, 4, 5])
multiplied_arr = arr * 2

print(multiplied_arr)
# Output: [ 2  4  6  8 10]
# Explanation: Multiplies each element by 2 using a single operation.


# --------------------------------------------------
# REVISION NOTES
# --------------------------------------------------
# Broadcasting -> NumPy automatically expands compatible shapes
#                 conceptually to perform an operation.
# Scalar broadcasting -> Applies one scalar value to every array element.
# Vectorization -> Performs operations on whole arrays without explicit
#                  Python loops over individual elements.
# Matrix + vector -> A vector of shape (3,) can be added to each row
#                    of a matrix of shape (3, 3).
# NumPy operations are often faster for large numerical datasets.
# Broadcasting requires compatible shapes; incompatible shapes raise
# a ValueError.
# Broadcasting and vectorization are related but different concepts.



# 8. Incompatible Shapes in Broadcasting
import numpy as np

# Example 1: Arrays with different lengths
arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 20])

# result = arr1 + arr2
# ValueError: operands could not be broadcast together with shapes (3,) (2,)
# Explanation: Both arrays have different lengths (3 and 2).
# Neither dimension is equal to the other, nor is either dimension 1.


# Example 2: Incompatible 2D arrays
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])       # Shape: (2, 3)

arr2 = np.array([[10, 20],
                 [30, 40]])        # Shape: (2, 2)

# result = arr1 + arr2
# ValueError: operands could not be broadcast together with shapes (2,3) (2,2)
# Explanation: The last dimensions (3 and 2) are incompatible.


# Example 3: Incompatible matrix and vector
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])     # Shape: (2, 3)

vector = np.array([10, 20])        # Shape: (2,)

# result = matrix + vector
# ValueError: operands could not be broadcast together with shapes (2,3) (2,)
# Explanation: The last dimensions (3 and 2) do not match.


# 9. How to Check Broadcasting Compatibility
# Compare shapes from RIGHT TO LEFT.
# Two dimensions are compatible if:
# 1. They are equal, OR
# 2. One of them is 1.
# Missing dimensions are treated as 1.
#
# Compatible examples:
# (3, 3) + (3,)    -> Valid
# (2, 3) + (1, 3)  -> Valid
# (2, 3) + (2, 1)  -> Valid
#
# Incompatible examples:
# (3,) + (2,)      -> Invalid
# (2, 3) + (2, 2)  -> Invalid
# (2, 3) + (2,)    -> Invalid


# --------------------------------------------------
# REVISION NOTES
# --------------------------------------------------
# Broadcasting works when corresponding dimensions are equal
# or one of them is 1.
# Compare dimensions from right to left.
# Missing dimensions are treated as 1.
# Incompatible shapes raise a ValueError.
# Use arr.shape to check an array's shape before an operation.
