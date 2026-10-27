import numpy as np

numbers  =  np.array([10,20,30,40,50,60])

parts = np.split(numbers,3)

print("original Array: ")
print(numbers)

print("\nFirst part: ")
print(parts[0])

print("\nSecond part: ")
print(parts[1])


print("\nThird part: ")
print(parts[2])