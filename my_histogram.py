import matplotlib.pyplot as plt
import numpy as np
# Sample data
x = np.random.rand(1000)
# print(x)
# y = np.random.rand(1000)
plt.hist(x, bins=8, color='green', edgecolor='black',)
# Set labels and title     
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Sample Histogram')
# Show the plot
plt.show()