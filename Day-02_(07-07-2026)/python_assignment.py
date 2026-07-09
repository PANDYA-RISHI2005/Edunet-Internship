import numpy as np
 
d_0 = np.array(42)
 
d_1 = np.array([42, 421, 423, 424])
 
d_2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
 
d_3 = np.array([
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ]
])
 
 
 
print(np.ndim(d_0), "\n", d_0)
print(np.ndim(d_1), "\n", d_1)
print(np.ndim(d_2), "\n", d_2)
print(np.ndim(d_3), "\n", d_3)

print(f" d_3[0,2,2] {d_3[0,2,2]} + d_3[1,1,2] {d_3[1,1,2]} = {d_3[1,1,2] +  d_3[0,2,2]}")

d_03 = d_3.reshape(9, -1)
print("reshaped",d_03)
print(d_03)

print("Size of array, total elements", d_3.size)
print("Dimensions of array", d_3.ndim)
print("Shape of array", d_3.shape)
d_013 = d_2.flatten()
print(f" last Print statement \n Flattened Array, dimension now : 
np.ndim(d_013)} \n, Shape Now {d_013.shape} , \n Array itself {d_013}")
