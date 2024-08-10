import numpy as np

def rotate_3d_array_90_degrees(array_3d):
    # Rotate each 2D matrix within the 3D array
    rotated_array = np.rot90(array_3d, k=1, axes=(1, 2))  # Rotates 90 degrees counterclockwise
    return rotated_array

# Example 3D array (2 layers of 3x3 matrices)
array_3d = np.array([
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]],

    [[10, 11, 12],
     [13, 14, 15],
     [16, 17, 18]]
])

# Rotate the 3D array by 90 degrees
rotated_array = rotate_3d_array_90_degrees(array_3d)
print("Original Array:")
print(array_3d)
print("\nRotated Array (90 degrees):")
print(rotated_array)
