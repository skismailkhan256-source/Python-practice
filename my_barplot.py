import matplotlib.pyplot as plt
import numpy as np
# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 25, 30]
# Create a bar plot
plt.bar(categories, values, color='orange', alpha=0.7)
# Set labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Sample Bar Plot')
# Show the plot
plt.show()