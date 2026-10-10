import numpy as np

print('\n====ARANGE=======')
num1 = np.arange(1,20)
print('Example 1: ',num1)

num2 = np.arange(2,30,2)
print('Example 2: ',num2)

num3 = np.arange(10,0,-2)
print('Example 3: ',num3)

print('\n====LINSPACE=======')

num4 = np.linspace(0,100,6)
print('Example 4: ',num4)

num5 = np.linspace(0,1,11)
print('Example 5: ',num5)

num6 = np.linspace(-1,1,100)
print('Example 6: ',num6)

print("\n==== ARRAY PROPERTIES ====")
print("Shape:", num6.shape)
print("Size:", num6.size)
print("Dimensions:", num6.ndim)
print("Data type:", num6.dtype)