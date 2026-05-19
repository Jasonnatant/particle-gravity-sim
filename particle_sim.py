import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of particles 
num_particles = 20

# Random starting postions 
positions = np.random.rand(num_particles, 2) * 10

# Random velocities
velocities = (np.random.rand(num_particles, 2)-0.5) * 0.2

# Gravity
gravity = np.array([0, -0.01])

fig, ax = plt.subplots()

scatter = ax.scatter(positions[:,0], positions[:,1])

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

def update(frame):
    global positions, velocities

    # Apply gravity 
    velocities += gravity

    # Update positions
    positions += velocities

    # Bounce off floor
    for i in range(num_particles):
        if positions[i, 1] <= 0:
            velocities[i, 1] *= -0.8
            positions[i, 1] = 0

    scatter.set_offsets(positions)

    return scatter,

animation = FuncAnimation(fig, update, frames=200, interval=30)

plt.title("2D Particle Gravity Simulation")
plt.show()