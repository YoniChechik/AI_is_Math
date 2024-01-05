import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(40)


def f_with_noise_gen():
    """A second-order polynomial function with random noise on coefficients."""
    a = np.random.normal(0, 1)
    b = np.random.normal(0, 0.2)
    return lambda x, y: (
        -(0.5 + a) * (x**2)
        - (0.3 + b) * (y**2)
        + (2) * np.sin(1.5 * x)
        + (2) * np.cos(1.5 * y)
    )


def approximate_gradient(f, x, y, eps=1e-5):
    dfdx = (f(x + eps, y) - f(x - eps, y)) / (2 * eps)
    dfdy = (f(x, y + eps) - f(x, y - eps)) / (2 * eps)
    return np.array([dfdx, dfdy])


def find_min_point(f, initial_point, alpha=0.1, n_steps=50):
    """Find a local minimum point using stochastic gradient descent."""
    x, y = initial_point
    for _ in range(n_steps):
        grad = approximate_gradient(f, x, y)
        x -= alpha * grad[0]
        y -= alpha * grad[1]
    return np.array([x, y])


# Reinitialize the starting point and path
x, y = 0, 0.1
path = [(x, y)]
# Parameters
alpha = 0.2  # Learning rate
n_steps = 15  # Number of steps in gradient descent

x_range = np.linspace(-4, 4, 400)
y_range = np.linspace(-4, 4, 400)
x_grid, y_grid = np.meshgrid(x_range, y_range)

# create fig
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Static graph
f_static = f_with_noise_gen()
z_grid_static = f_static(x_grid, y_grid)
ax1.imshow(
    z_grid_static, extent=[-4, 4, -4, 4], origin="lower", cmap="viridis", alpha=0.8
)
contour_static = ax1.contour(
    x_grid, y_grid, z_grid_static, 10, colors="black", alpha=0.5
)
ax1.clabel(contour_static, inline=True, fontsize=8)
ax1.set_title('"True" loss function of the dataset')
# Find min using SGD
min_point = find_min_point(f_static, (x, y), alpha, 25)

# Mark the minimum point
if np.all(min_point > -4) and np.all(min_point < 4):
    ax1.plot(min_point[0], min_point[1], color="white", marker="o", markersize=6)
else:
    raise Exception("problem")


def update(step):
    ax2.clear()
    f_with_noise = f_with_noise_gen()
    z_grid_random = f_with_noise(x_grid, y_grid)

    # Plot heatmap and contours
    ax2.imshow(
        z_grid_random, extent=[-4, 4, -4, 4], origin="lower", cmap="viridis", alpha=0.8
    )
    contour = ax2.contour(x_grid, y_grid, z_grid_random, 10, colors="black", alpha=0.5)
    ax2.clabel(contour, inline=True, fontsize=8)

    # Update gradient descent path for the current step
    grad = approximate_gradient(f_with_noise, path[step][0], path[step][1])
    new_x, new_y = path[step][0] - alpha * grad[0], path[step][1] - alpha * grad[1]
    path.append((new_x, new_y))

    # Find min using SGD
    min_point = find_min_point(f_with_noise, (new_x, new_y), alpha, 25)

    # Mark the minimum point
    if np.all(min_point > -4) and np.all(min_point < 4):
        ax2.plot(min_point[0], min_point[1], color="white", marker="o", markersize=6)

    # Plot gradient descent path up to current step
    current_path = np.array(path)
    for ax in (ax1, ax2):
        ax.plot(
            current_path[:, 0],
            current_path[:, 1],
            color="r",
            marker="o",
            markersize=3,
            alpha=1,
            linestyle="-",
        )
    ax2.set_title(f"Mini batch (stochastic) gradient descent- Step {step}")
    ax2.text(
        0.01,
        0.01,
        "Made by Yoni Chechik",
        transform=ax2.transAxes,
        ha="left",
        va="bottom",
        fontsize=10,
        color="white",
    )


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=n_steps, interval=1000, repeat=False)

# Save the animation as a GIF
ani.save("gradient_descent_animation.gif", writer="pillow")

plt.close()  # Close the plot to prevent it from displaying now
