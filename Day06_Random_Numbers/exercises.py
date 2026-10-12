import numpy as np

print('\n======RANDOM=======  ')
num1 = np.random.randint(1,50,size=10)
print(num1)

print('\n =======3x3 Array========')
array = np.random.random(size=(3,3))
print(array)


print('\n=====LIST==========')
fruits = np.array([
    "Apple", "Mango", "Orange", "Grapes", "Banana"
])
selected = np.random.choice(fruits,size=3,replace=False)
print(selected)