import matplotlib.pyplot as plt
import numpy as np
# Sample data
sizes = [40, 30, 20, 10]
labels = ['A', 'B', 'C', 'D']

# Create a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
# Set title
plt.title('Sample Pie Chart')
# Show the plot
plt.show()
