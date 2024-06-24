import numpy as np

# Example 2D arrays (simulating data from FITS files)
array1 = np.array([[1, 2],
                   [3, 4]])

array2 = np.array([[5, 6],
                   [7, 8]])

array3 = np.array([[9, 10],
                   [11, 12]])

# Stack the arrays along a new third dimension
FITS_list = [array1, array2, array3]
FITS_stack = np.dstack(FITS_list)
print("Stacked Array (FITS_stack):\n", FITS_stack)

# Calculate the median along the third dimension (axis=2)
median = np.median(FITS_stack, axis=2)
print("Median Array:\n", median)
