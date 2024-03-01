import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)


y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, label='Sine')
plt.plot(x, y_cos, label='Cosine')


plt.fill_between(x, y_sin, y_cos, color='gray', alpha=0.3)


plt.xlabel('Angle (radians)')
plt.ylabel('Value')
plt.title('Sine and Cosine Plot with Hatched Shading')
plt.legend()

plt.show()