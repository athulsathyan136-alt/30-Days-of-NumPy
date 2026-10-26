import numpy as np

class_a = np.array([70, 80, 90])
class_b = np.array([60, 75, 85])

print("Vertical stacking: ")
print(np.vstack((class_a,class_b)))

print("Horizontal stacking: ")
print(np.hstack((class_a,class_b)))
