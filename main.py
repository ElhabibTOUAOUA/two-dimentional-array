import numpy as np
import hashlib

# a = [    
#       [1, 0, 1, 1],  
#       [1, 1, 1, 0],  
#       [0, 0, 1, 0],  
#       [1, 1, 0, 0],  
#     ]  

def inputMatrixFromUser(rows, cols):
  matrix = []
  for i in range(rows):
    matrix.append([])
    for j in range(cols):
      matrix[i].append(int(input(f"Enter the value of row {i+1} and column {j+1}: ")))
  return matrix


def arraySum(list):
  sum = 0
  for i in range(len(list)):
    sum += list[i]
  return sum


def matrixHash(two_d_arr):
  two_d_arr = np.matrix(two_d_arr)
  return hashlib.sha1(two_d_arr).hexdigest()


def matrixGenerator(rows, cols):
  matrix = np.random.randint(2, size=(rows,cols))
  return matrix


def verctorsExtraction(two_d_arr):
  v1, v2 = [], []
  for i in range(len(two_d_arr)):
    v1.append(arraySum(two_d_arr[i]))
    sum_col = 0
    for j in range(len(two_d_arr[i])):
      sum_col += two_d_arr[j][i]
    v2.append(sum_col)

  return v1, v2


if __name__ == "__main__":
  rows, cols = int(input("Enter the number of rows: ")), int(input("Enter the number of columns: "))
  inputMatrix = inputMatrixFromUser(rows, cols)
  a_v1, a_v2 = verctorsExtraction(inputMatrix)
  inputMatrixHash = matrixHash(inputMatrix)
  numOfGeneratedMatrix = 0
  numOfGeneratedMatrixWithSameVectors = 0
  x = True
  while x:
    generatedMatrix = matrixGenerator(rows, cols)
    # print(np.matrix(generatedMatrix))
    numOfGeneratedMatrix += 1
    b_v1, b_v2 = verctorsExtraction(generatedMatrix)
    if b_v1 == a_v1 and b_v2 == a_v2:
      numOfGeneratedMatrixWithSameVectors += 1
      # print("***** Same Vectors *****")
      # print(np.matrix(generatedMatrix))
      if inputMatrixHash == matrixHash(generatedMatrix):
        print("***** Same Vectors and Hash *****")
        print(np.matrix(generatedMatrix))
        print(f"v1: {b_v1} \nv2: {b_v2}")
        print(f"Input Matrix hash: {inputMatrixHash} \nGenerated Matrix hash: {matrixHash(generatedMatrix)}")
        x = False
    #   else:
    #     # print("***** Same Vectors but Different Hash *****")
    # else:
    #   # print("***** Different Vectors *****")
    
  print(f"Number of Generated Matrix: {numOfGeneratedMatrix}")
  print(f"Number of Generated Matrix with Same Vectors: {numOfGeneratedMatrixWithSameVectors}")