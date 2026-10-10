import numpy as np

print('=====ARANGE=======')
num1 = np.arange(10)
print('Example 1: ',num1)

num2 = np.arange(1,11)
print('Example 2: ',num2)

num3 = np.arange(0,21,5)
print('Example 3: ',num3)

num4 = np.arange(10,0,-1)
print('Example 4: ',num4)

print("\n===== LINSPACE =====")

num5 = np.linspace(0,10,5)
print('Example 5: ',num5)

num6 =np.linspace(0,5,5)
print('Example 6: ',num6)

num7 = np.linspace(0,1,11)
print('Example 7: ',num7)

print('\n=====ARRAY PROPERTIES==========')

print('Shape : ',num5.shape)
print('Size : ',num5.size)
print('Dimensions : ',num5.ndim)
print('DataType : ',num5.dtype)