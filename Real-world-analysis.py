import matplotlib.pyplot as plt
import numpy as np

days = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sales_in_car = np.array([2.5, 3.0, 3.5, 4.0, 
                         4.5, 5.0, 5.5, 3.0, 6.5, 9.0])
plt.figure(figsize=(10, 6))

plt.style.use('fast')
plt.plot(days, sales_in_car, marker='o', color='blue', 
         linestyle='-', linewidth=2, markersize=8)
plt.grid(True)
plt.xlabel('Days')
plt.ylabel('Sales in Crores')
plt.savefig('sales_analysis.png', format='png')
plt.title('Sales Analysis')
plt.show()
