import matplotlib.pyplot as plt
import numpy as np
# Sample data
x = [1, 2, 3, 4, 5]
y = [10,20,15,25,30]
# Create a scatter plot
plt.style.use('ggplot')
plt.scatter(x, y, color='blue',s=100, alpha=0.5,marker='*')  
# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Scatter Plot')
# Show the plot
plt.show()