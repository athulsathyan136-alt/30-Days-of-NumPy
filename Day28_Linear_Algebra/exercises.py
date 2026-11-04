
import numpy as np

# Exercise 1
# Create a 2x2 matrix containing:
# 10, 20
# 30, 40
mat = np.array([[10,20],[30,40]])
# Find its transpose.
print("\nTranspose: ")
print(mat.T)
# Exercise 2
# Create two 2x2 matrices.
A = np.array([[3,5],[9,1]])
B = np.array([[1,2],[1,3]])
# Find their matrix multiplication.
print("\nMatrix Multipilcation: ")
print(np.matmul(A,B))
# Exercise 3
# Create a matrix:
# [[3, 2],
#  [1, 4]]
matrix = np.array([[3,2],[1,4]])
# Find its determinant.
print("\nDeterminant:")
print(np.linalg.det(matrix))
# Exercise 4
# Create a 3x3 identity matrix.
print("Identity Matrix:")
print(np.eye(3))
# Exercise 5
# Find the rank of:
# [[1, 2],
#  [2, 4]]
rank = np.array([[1,2],[2,4]])
print("\nRank of Matrix:")
print(np.linalg.matrix_rank(rank))
# Exercise 6
# Solve these equations using np.linalg.solve:
# 3x + y = 10
# x + 2y = 8
x = np.array([[3,1],[1,4]])
y = np.array([10,8])

solution = np.linalg.solve(x,y)

print("\nSolve these equations using np.linalg.solve: 3x + y = 10 ,x + 2y = 8: ")
print("x = ",solution[0])
print("y = ",solution[1])