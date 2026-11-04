import numpy as np

print("NUMPY LINEAR ALGEBRA ANALYZER")
print("="*40)

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMatrix Addition:")
print(A+B)

print("\nMatrix Substraction:")
print(A-B)

print("\nElement-wise Mutliplication:")
print(A*B)

print("\nMatrix Mutliplication:")
print(np.matmul(A,B))

print("\nTranspose of A:")
print(A.T)
print("\nTranspose of B:")
print(B.T)

print("\nDeterminant of A:")
print(np.linalg.det(A))

print("\nInverse of A:")
print(np.linalg.inv(A))

print("\nRank of A:")
print(np.linalg.matrix_rank(A))

print("\nIdentity Matrix:")
print(np.eye(3))


cofficients = np.array([[2,1],[1,3]])

constant = np.array([8,13])

soln = np.linalg.solve(cofficients,constant)

print("\nSolution of Linear Eqaution:")
print("x =",soln[0])
print("y =",soln[1])

vector_a = np.array([2,3,4])
vector_b = np.array([5,6,7])

print("\nVector Dot Product:")
print(np.dot(vector_a,vector_b))


