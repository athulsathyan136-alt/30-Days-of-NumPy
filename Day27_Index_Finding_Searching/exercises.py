
import numpy as np

temperatures = np.array([32, 28, 40, 25, 35])

print("Temperature: ",temperatures)

print("Highest index: ",np.argmax(temperatures))
print("Highest index: ",np.argmin(temperatures))

prices = np.array([500, 200, 800, 100, 400])
print("Prices: ",prices)

print("Sorted Prices: ",np.sort(prices))
print("Sorted indices: ",np.argsort(prices))

print("Insertion postion of 400: ",np.searchsorted(prices,400))