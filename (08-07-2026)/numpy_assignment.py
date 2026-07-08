import numpy as np

#multidimensional array
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print("Original Array:")
print(arr)

# 2. Use index numbers to access values and perform mathematical operations
print("\nAccessing Values:")
print("Element at [0][1]:", arr[0][1])      # 20
print("Element at [2][2]:", arr[2][2])      # 90

# Mathematical operation using indexed values
sum_values = arr[0][1] + arr[2][2]
product_value = arr[1][0] * arr[0][2]
sub_value = arr[1][0] - arr[0][2]
div_value =  arr[1][0] / arr[0][1]

print("\nMathematical Operations:")
print("20 + 90 =", sum_values)
print("40 * 30 =", product_value)
print("40 - 30 =", sub_value)
print("40 / 20 =", div_value)


#Applying NumPy Methods

print("\n1. Shape:", arr.shape)

print("2. Dimensions:", arr.ndim)

print("3. Size:", arr.size)

print("4. Data Type:", arr.dtype)

print("5. Transpose:\n", arr.T)

print("6. Flatten:\n", arr.flatten())

print("7. Reshape (1x9):\n", arr.reshape(1, 9))

print("8. Sum:", np.sum(arr))

print("9. Mean:", np.mean(arr))

print("10. Maximum:", np.max(arr))

print("11. Minimum:", np.min(arr))

print("12. Standard Deviation:", np.std(arr))

print("13. Square Root:\n", np.sqrt(arr))

print("14. Sort:\n", np.sort(arr))

print("15. Unique Values:", np.unique(arr))

# Additional NumPy methods (optional)

print("\n16. Cumulative Sum:", np.cumsum(arr))

print("17. Product of all elements:", np.prod(arr))

print("18. Column-wise Sum:", np.sum(arr, axis=0))

print("19. Row-wise Sum:", np.sum(arr, axis=1))

print("20. Clip values between 25 and 75:\n", np.clip(arr, 25, 75))