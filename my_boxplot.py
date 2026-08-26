import matplotlib.pyplot as plt
import numpy as np
# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 25, 30]
# Create a box plot
plt.boxplot(values, labels=categories)
# Set labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Sample Box Plot')
# Show the plot
plt.show()