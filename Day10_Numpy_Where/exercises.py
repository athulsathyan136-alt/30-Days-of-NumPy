
import numpy as np

temperatures = np.array([18, 25, 32, 15, 38, 28, 10])

print("Temperatures:")
print(temperatures)

# Exercise 1: Find indexes where temperature is above 30
temp = np.where(temperatures > 30)
print(f"indexes where temperature is above 30: {temp}")
print()
# Exercise 2: Label temperatures as "Hot" if >= 30,
# otherwise label them "Normal"
temp1 = np.where(temperatures >= 30,"Hot","Normal")
print(f"temperatures as Hot if >= 30 otherwise label them Normal")
print(temp1)
# Exercise 3: Replace temperatures below 20 with 20
temp2 = np.where(temperatures<20 ,20,temperatures)
print(f"Replace temperatures below 20 with 20")
print(temp2)

# Exercise 4: Add 2 degrees to temperatures below 20,
# keeping all other temperatures unchanged
temp3 = np.where(temperatures < 20 ,temperatures + 2 ,temperatures)
print("Add 2 degrees to temperatures below 20,keeping all other temperatures unchanged")
print(temp3)