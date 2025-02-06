import numpy as np
from matplotlib import pyplot as plt

positions = []
with open(file='Output/pos_repulsion.txt') as f:
    for line in f:
        try:
            splits = line.strip().split(',')
            if len(splits) == 3:
                positions.append((float(splits[0]), float(splits[1]), float(splits[2])))

        except ValueError:
            pass

filtered = [p for p in positions if p[0] == 420]
x_vals = [p[1] for p in filtered]
y_vals = [p[2] for p in filtered]

plt.scatter(x_vals, y_vals, s=1, color='black')
plt.gca().set_aspect('equal')
plt.xlabel('X in mm')
plt.ylabel('Y in mm')
plt.show()

x_max, x_min = max(x_vals), min(x_vals)
y_max, y_min = max(y_vals), min(y_vals)
# put in a grid
resolution_x = int(round((x_max - x_min)*4, 0))
resolution_y = int(round((y_max - y_min)*4, 0))

# Create a meshgrid
x_grid = np.linspace(x_min, x_max, resolution_x)
y_grid = np.linspace(y_min, y_max, resolution_y)
X, Y = np.meshgrid(x_grid, y_grid)

Z = np.zeros_like(X)

# Populate the Z grid with the accumulated count
for i in range(len(x_vals)):
    # Find the closest grid index for each x, y point
    ix = np.abs(x_grid - x_vals[i]).argmin()
    iy = np.abs(y_grid - y_vals[i]).argmin()

    # Assign the z value to the corresponding grid cell
    Z[iy, ix] += 1

plt.imshow(Z, extent=[x_min, x_max, y_min, y_max], origin='lower', cmap='plasma', aspect='auto')
lim = 8
aspect = 3
plt.ylim(-lim, lim)
x_offset = 0
plt.xlim(-lim * aspect + x_offset, lim * aspect + x_offset)
plt.title('Simulated Position')
plt.gca().set_aspect('equal')
plt.xlabel('X in mm')
plt.ylabel('Y in mm')
plt.show()
