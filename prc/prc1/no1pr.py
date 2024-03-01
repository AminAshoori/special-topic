import numpy as np
import matplotlib.pyplot as plt

# Generate numbers between 0 and 2π
x = np.linspace(0, 2*np.pi, 100)

# Calculate sine and cosine values for the generated numbers
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot the sine and cosine functions
plt.plot(x, y_sin, label='Sine')
plt.plot(x, y_cos, label='Cosine')

# Add hatched shading to the plot
plt.fill_between(x, y_sin, y_cos, color='gray', alpha=0.3)

# Other plot settings
plt.xlabel('Angle (radians)')
plt.ylabel('Value')
plt.title('Sine and Cosine Plot with Hatched Shading')
plt.legend()

# Show the plot
plt.show()