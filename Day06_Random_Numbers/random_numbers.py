import numpy as np

print('\n========DAY 6 RANDOM NUMBERS==============')

print('\n1.One Random integer: ')
number = np.random.randint(1,11)
print(number)

print('\n2.Five Random integer: ')
number2 = np.random.randint(1,101,size=5)
print(number2)

print('\n3.Random Decimal numbers: ')
number3 = np.random.random(size=5)
print(number3)

print('\n4.Random 2D Array: ')
number4 = np.random.randint(1,10,size=(3,4))
print(number4)

print('\n5. Reproducibe random numbers:')
np.random.seed(42)
first = np.random.randint(1,101,size=5)
print('First: ',first)

np.random.seed(42)
second = np.random.randint(1,101,size=5)
print('Second: ',second)

print('Same results: ',np.array_equal(first,second))

print('\n6. Random Choice')
fruit = np.array(["Apple", "Mango", "Orange", "Banana"])
selected = np.random.choice(fruit,size=2,replace=False)
print(selected)

print("\n7. Array Properties:")
print("Shape:", number4.shape)
print("Dimensions:", number4.ndim)
print("Size:", number4.size)
print("Data type:", number4.dtype)