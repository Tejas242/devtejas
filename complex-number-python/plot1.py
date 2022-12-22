import matplotlib.pyplot as plt
import numpy as np

# Calculate r and theta
r = np.sqrt((3-0)**2 + (4-0)**2)
theta = np.arctan(4/3)

# Set up the polar axis
ax = plt.subplot(111, projection='polar')

# Plot the point
ax.plot(theta, r, 'ro')

# Add a label showing the coordinates
plt.text(theta, r, '3+4i', ha='center', va='bottom')

# Add a line showing the distance from the origin
ax.plot([0, theta], [0, r], 'k-')

# Add a arc showing the angle with the x-axis
ax.plot(np.linspace(0, theta, 100), np.ones(100)*r, 'r--')

# Show the plot
plt.show()
