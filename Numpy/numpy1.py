
import numpy as np

# Creating a NumPy array
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# Performing operations on arrays
# Addition
addition_result = arr1 + arr2
print("Addition Result: ", addition_result)

# Creating arrays of zeros with np.zeros()
zeros_array1 = np.zeros((2,3)) # 2 rows and 3 columns
print("Zeros Array: ",zeros_array1)

# Element-wise operations
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

sum_array = arr1 + arr2
product_array = arr1 * arr2

print("Sum Array: ",sum_array)
print("Product Array: ",product_array)
