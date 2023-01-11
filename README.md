# Matrix Matching

This repository contains the code for a Python script that takes an input matrix from the user, and finds a matching matrix with the same row and column sums using a hash function. The script uses the `hashlib` library to hash the input matrix and its row and column sums, and uses the `random` library to generate random matrices to compare against the input matrix hash.

## Usage

The script includes the following functions:

-   `get_matrix()`: Prompts the user to enter the number of rows and columns, and then prompts the user to enter the elements of the matrix, one row at a time. Returns the matrix as a 2D list of integers.
-   `get_matrix_hash(matrix, v1, v2)`: Takes a matrix, and lists of row and column sums as input and returns the SHA-256 hash of the matrix and its row and column sums as a hexadecimal string.
-   `get_v1_v2(matrix)`: Takes a matrix as input, and returns lists of the row and column sums.
-   `generate_random_matrix(n, m)`: Generates a random matrix of size n x m where the elements are either 0 or 1.
-   `find_matching_matrix(matrix)`: Takes an input matrix, and returns a randomly generated matrix that has the same row and column sums as the input matrix. The function uses the get_v1_v2 and get_matrix_hash functions to compare the input matrix and the randomly generated matrices.

### `Example usage`

```python
matrix = get_matrix()
matching_matrix = find_matching_matrix(matrix)
print(matching_matrix)
```

## Limitations

Keep in mind that the script might not find a matching matrix fastly depending on the size of the matrix because the script keeps generating random matrices until it finds a match, the script may take a while to find a matching matrix if the matrix is big enough.
