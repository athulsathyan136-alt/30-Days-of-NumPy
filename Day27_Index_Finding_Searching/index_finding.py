import numpy as np

score = np.array([78,85,96,58,85])

print("Students scores: ",score)

high = np.max(score)
low = np.min(score)

print("\nHighest: ",high)
print("Lowest : ",low)

print("Highest index: ",np.argmax(score))
print("Lowest index: ",np.argmin(score))
print("Sorted scores: ",np.sort(score))
print("Sorted indices: ",np.argsort(score))
print("Insertion position of 85: ",np.searchsorted(score,85))

top_indices = np.argpartition(score,-2)[-2:]

print("Top Two score indices: ",top_indices)
print("Top two score: ",score[top_indices])