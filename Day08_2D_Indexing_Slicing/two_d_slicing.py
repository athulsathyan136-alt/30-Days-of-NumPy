
import numpy as np

print("===== DAY 8: 2D INDEXING AND SLICING =====")

marks = np.array([
    [85, 90, 78, 95],
    [72, 88, 91, 84],
    [93, 81, 87, 98]
])

print('\n1.Original Array: ')
print(marks)
print('\n2.Individual Elements: ')
print('Row 0 ,column 0: ',marks[0,0])
print('Row 1 ,column 2: ',marks[1,2])
print('last row , last column: ',marks[-1,-1])

print("\n3. Rows:")
print('First Row: ',marks[0])
print('Second Row: ',marks[1])
print('Last Row: ',marks[-1])

print("\n4. Columns:")
print('First column: ',marks[:,0])
print('Second column: ',marks[:,1])
print('Last column: ',marks[:,-1])

print("\n5. Multiple rows:")
print('First two rows:')
print(marks[:2,:])
print("\n6. Multiple columns:")
print("First three columns:")
print(marks[:,:3])
print("\n7. A section of the array:")
print(marks[:2,1:3])
print("\n8. Modify one mark:")
marks[0, 0] = 100
print(marks)
print("\n9. Modify the last row:")
marks[:-1,:] = [90, 90, 90, 90]
print(marks) 
print("\n10. Array properties:")
print("Shape:", marks.shape)
print("Dimensions:", marks.ndim)
print("Total elements:", marks.size)
