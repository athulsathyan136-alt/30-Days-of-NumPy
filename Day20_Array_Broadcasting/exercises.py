import numpy as np

temperatures = np.array([25, 30, 35, 40])

# Exercise 1: Add 5 to every temperature.

temp = temperatures + 5
print("Add 5 to every temperature")
print(temp)
# Exercise 2: Subtract 10 from every temperature.
sub = temperatures - 10
print("Sub 10 to every temperature")
print(sub)
# Exercise 3: Multiply every temperature by 2.
print("Multiply by 2 to every temperature")
print(temperatures*2)
# Exercise 4: Print the original array to confirm it has not changed.
print("Original temperature: ")
print(temperatures)