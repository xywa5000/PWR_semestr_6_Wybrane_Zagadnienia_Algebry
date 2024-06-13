import numpy as np
import matplotlib.pyplot as plt

# Generate data points
u = np.linspace(-2, 2, 1000)
v = np.linspace(-2, 2, 1000)
u, v = np.meshgrid(u, v)

x = u * v
y = v
z = u ** 2

# Plot the surface
fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(x, y, z, cmap='viridis')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Whitneys Umbrella')


x = np.linspace(-2, 2, 5000)
y = np.linspace(-2, 2, 5000)
x_v, y_v = np.meshgrid(x, y)

def variety(x, y):
    return x**2 / y**2

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(x_v, y_v, variety(x_v, y_v), cmap='viridis')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('$V(x^2 - y^2 * z)$')

plt.show()
