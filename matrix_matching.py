import hashlib
import random

def get_matrix():
		# Get the number of rows and columns
		n = int(input('Enter the number of rows: '))
		m = int(input('Enter the number of columns: '))

		# Get the matrix
		matrix = []
		for i in range(n):
				row = [int(x) for x in input('Enter row {}: '.format(i + 1)).split()[:m]]
				row += [0] * (m - len(row))  # Pad with zeros if needed
				matrix.append(row)

		return matrix

def get_matrix_hash(matrix, v1, v2):
		# Hash the matrix, v1 and v2
		matrix_hash = hashlib.sha256()
		matrix_hash.update(str(matrix).encode('utf-8'))
		matrix_hash.update(str(v1).encode('utf-8'))
		matrix_hash.update(str(v2).encode('utf-8'))
		return matrix_hash.hexdigest()

def get_v1_v2(matrix):
		# Calculate v1 and v2
		v1 = [sum(row) for row in matrix]
		v2 = [sum(column) for column in zip(*matrix)]
		return v1, v2

def generate_random_matrix(n, m):
		# Generate a random matrix of size n x m
		return [[random.randint(0, 1) for _ in range(m)] for _ in range(n)]

def find_matching_matrix(matrix):
		# Calculate v1 and v2 for the input matrix
		v1, v2 = get_v1_v2(matrix)

		# Hash the input matrix, v1 and v2
		input_matrix_hash = get_matrix_hash(matrix, v1, v2)

		# Generate a random matrix and calculate v1 and v2 for it
		random_matrix = generate_random_matrix(len(matrix), len(matrix[0]))
		random_v1, random_v2 = get_v1_v2(random_matrix)

		# Hash the random matrix, v1 and v2
		random_matrix_hash = get_matrix_hash(random_matrix, random_v1, random_v2)

		# Compare the hashes and keep generating random matrices until
		# we find a match
		while input_matrix_hash != random_matrix_hash:
				random_matrix = generate_random_matrix(len(matrix), len(matrix[0]))
				random_v1, random_v2 = get_v1_v2(random_matrix)
				random_matrix_hash = get_matrix_hash(random_matrix, random_v1, random_v2)

		# Return the matching matrix
		return random_matrix

# Example usage
# Function that gets the input matrix from the user

matrix = get_matrix()
matching_matrix = find_matching_matrix(matrix)

print(matching_matrix)