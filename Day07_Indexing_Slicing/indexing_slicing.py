import numpy as np

print("===== DAY 7: INDEXING AND SLICING =====")

number = np.array([10,20,30,40,50,60])

print('\n=====ORIGINAL ARRAY=========')
print(number)

print("\n2. Indexing:")
print('First element: ',number[0])
print('Third element: ',number[2])
print('Last element: ',number[-1])

print("\n3. Slicing:")
print('index 1 to 3: ',number[1:4])
print('First three: ',number[:3])
print('From 2 : ',number[2:])
print('Every second element: ',number[::2])
print('Reversed array: ',number[::-1])

print("\n4. Modify an element:")
number[1] = 99
print(number)

print("\n5. Two-dimensional indexing:")
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original matrix:")
print(matrix)

print('First row: ',matrix[0])
print('Second row: ',matrix[1])
print('Element at a row 0 ,column 1: ',matrix[0,1])
print('Element at row 2 ,colum 2: ',matrix[2,2])

print("\n6. Two-dimensional slicing:")
print("First two rows:")
print(matrix[:2,:])
print('First two columns')
print(matrix[:,:2])
print('First two rows and colums')
print(matrix[:2,:2])

print('\n7.Modify a matrix element:')
matrix[0,0] = 999
print(matrix)

print("\n8. Array properties:")
print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Size:", matrix.size)