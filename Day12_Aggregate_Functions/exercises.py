
import numpy as np

scores = np.array([45, 80, 65, 90, 70])

# Exercise 1: Find the total of all scores
print("Total Score: ",np.sum(scores))
# Exercise 2: Find the average score
print("Average Score: ",np.mean(scores))

# Exercise 3: Find the highest score
print("Highest Score: ",np.max(scores))
# Exercise 4: Find the lowest score
print("Lowest Score: ",np.min(scores))

# Exercise 5: Find the difference between
# the highest and lowest scores
high = np.max(scores)
low = np.min(scores)
diff = high- low
print("Difference in high and low: ",diff)