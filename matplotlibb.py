import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]

y = [10, 20, 25, 30, 35]

plt.plot(x, y,color="red", marker="o", linestyle="--")
plt.title("Simple Line Plot", color="blue")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")   
plt.show()
