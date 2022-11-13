import numpy as np
import hashlib

a = [    
      [1, 0, 1, 1],  
      [1, 1, 1, 0],  
      [0, 0, 1, 0],  
      [1, 1, 0, 0],  
    ]  

b = [    
      [1, 0, 1, 1],  
      [1, 1, 1, 0],  
      [0, 0, 1, 0],  
      [1, 1, 0, 1],  
    ]  

def list_sum(list):
  sum = 0
  for i in range(len(list)):
    sum += list[i]
  return sum


def hash_arr(two_d_arr):
  two_d_arr = np.matrix(two_d_arr)
  return hashlib.sha1(two_d_arr).hexdigest()


def arr_gen():
  row, col = 4, 4
  matrix = np.random.randint(2, size=(row,col))
  return matrix


def verctors(two_d_arr):
  v1, v2 = [], []
  for i in range(len(two_d_arr)):
    v1.append(list_sum(two_d_arr[i]))
    sum_col = 0
    for j in range(len(two_d_arr[i])):
      sum_col += two_d_arr[j][i]
    v2.append(sum_col)

  return v1, v2


if __name__ == "__main__":

  a_v1, a_v2 = verctors(a)
  a_hash = hash_arr(a)
  x = True
  while x:
    b = arr_gen()
    # print(np.matrix(b))
    b_v1, b_v2 = verctors(b)
    if b_v1 == a_v1 and b_v2 == a_v2:
      print("***** Same Vectors *****")
      print(np.matrix(b))
      if a_hash == hash_arr(b):
        print("***** Same Vectors and Hash *****")
        print(np.matrix(b))
        print(f"v1: {b_v1} \nv2: {b_v2}")
        x = False

