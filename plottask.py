# plottask.py
# Weekly Tasks 08
# This code generates a histogram of a normal distribution with a mean of 5 and a standard deviation of 2, and plots the function h(x) = x^3 in the range [0, 10] on the same set of axes.
# author: Galal Abdelaziz

import numpy as np                  # Import the numpy library as np.
import matplotlib.pyplot as plt     # Import the matplotlib.pyplot library as plt.

data = np.random.normal(5, 2, 1000) # Generate 1000 random numbers from a normal distribution with mean=5 and standard deviation=2.

plt.hist(data, label='Histogram (mean=5, std=2)') # Plot a histogram of the data, setting a label to show on legend.

#                               # Setting the function h(x) = x^3 in the range [0, 10].
x = np.linspace(0, 10, 1000)    # Create a numpy array of 1000 evenly spaced values between 0 and 10.
y = x ** 3                      # Calculate the corresponding y-values using the formula y = x^3.

plt.plot(x, y, 'r-', label='Plot (h(x)=x^3)') # Plot the function on the same axes, color red, setting a label to show on legend.


plt.xlabel('x') # Setting the x-axis label.
plt.ylabel('y') # Setting the x-axis label.

plt.legend() # Adding a legend to the plot.


plt.show() # Display the histogram and the plot.