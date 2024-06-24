import numpy as np
# Example 2D arrays
array1 = np.array([[1, 2],
                   [3, 4]])

array2 = np.array([[5, 6],
                   [7, 8]])

array3 = np.array([[9, 10],
                   [11, 12]])

# List of arrays
FITS_list = [array1, array2, array3]

# Get the shape of the first array (assuming all have the same shape)
shape = FITS_list[0].shape

# Create an empty array to store medians with the same shape
medians = np.empty(shape)

# Iterate through each row and column
for i in range(shape[0]):
  for j in range(shape[1]):
    # Extract elements at current index from each array
    elements = [arr[i, j] for arr in FITS_list]
    # Calculate the median of the extracted elements
    median_value = np.median(elements)
    # Assign the median to the corresponding position in the medians array
    medians[i, j] = median_value

print("Medians of Each Index:\n", medians)
