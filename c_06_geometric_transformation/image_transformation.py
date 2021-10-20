# %% [markdown]
# # Image transformation
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YoniChechik/AI_is_Math/blob/master/c_06_geometric_transformation/image_transformation.ipynb)

# %%
import numpy as np
import matplotlib.pyplot as plt

figsize = (10, 10)

# %% [markdown]
# ## Start by building our basic default points to test on
# %%
x_max = 20
y_max = 10
x_arr, y_arr = np.meshgrid(np.arange(x_max), np.arange(y_max))
x_arr = x_arr.flatten().reshape(1, -1)
y_arr = y_arr.flatten().reshape(1, -1)
xy = np.concatenate((x_arr, y_arr), axis=0)

print(xy.shape)
xy
# %%
plt.figure(figsize=figsize)
plt.scatter(xy[0, :], xy[1, :])
plt.title("Original points")
plt.show()

# %% [markdown]
# ## Scale
# %%
sx = 2
sy = 3
M_scale = np.array([[sx, 0], [0, sy]])
M_scale
# %%
xy_scaled = M_scale @ xy

plt.figure(figsize=figsize)
plt.scatter(xy[0, :], xy[1, :])
plt.scatter(xy_scaled[0, :], xy_scaled[1, :], marker="*")
plt.title("Scaled points")
plt.show()

# %% [markdown]
# ## Rotate
# %%


def rot_mat(theta):
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([[c, -s], [s, c]])


rot_mat(np.pi)

# %%
theta = np.pi / 2
xy_rotate = rot_mat(theta) @ xy

plt.figure(figsize=figsize)
plt.scatter(xy[0, :], xy[1, :])
plt.scatter(xy_rotate[0, :], xy_rotate[1, :], marker="*")
plt.title("Rotated points 90 degrees")
plt.show()

# %%
theta = np.pi / 4
xy_rotate = rot_mat(theta) @ xy

plt.figure(figsize=figsize)
plt.scatter(xy[0, :], xy[1, :])
plt.scatter(xy_rotate[0, :], xy_rotate[1, :], marker="*")
plt.title("Scaled points 45 degrees")
plt.show()


# %% [markdown]
# ## Shear

# %%
shear_x = 2
shear_y = 0
M_shear = np.array([[1, shear_x], [shear_y, 1]])
M_shear
# %%
xy_sheared = M_shear @ xy

plt.figure(figsize=figsize)
plt.scatter(xy[0, :], xy[1, :])
plt.scatter(xy_sheared[0, :], xy_sheared[1, :], marker="*")
plt.title("Sheared points")
plt.show()

# %% [markdown]
# ## Translate

# %%
xy1 = np.concatenate((xy, np.ones((1, xy.shape[1]))), axis=0)

xy1

# %%
t_x = 12.5
t_y = -4
M_t = np.array([[1, 0, t_x], [0, 1, t_y], [0, 0, 1]])

M_t
# %%
xy1_translated = M_t @ xy1

plt.figure(figsize=figsize)
plt.scatter(xy1[0, :], xy1[1, :])
# no need to do hear homogenous normalization...
plt.scatter(xy1_translated[0, :], xy1_translated[1, :], marker="*")
plt.title("Translated points")
plt.show()

# %% [markdown]
# ## Matrix concatenation

# %%
s_x = 2
s_y = 3.5
M_scale = np.array([[s_x, 0, 0], [0, s_y, 0], [0, 0, 1]])

xy1_s_then_t = M_t @ M_scale @ xy1

plt.figure(figsize=figsize)
plt.scatter(xy1[0, :], xy1[1, :])
# no need to do hear homogenous normalization...
plt.scatter(xy1_s_then_t[0, :], xy1_s_then_t[1, :], marker="*")
plt.title("Scaled and then translated points")
plt.show()

# %%
xy1_t_then_s = M_scale @ M_t @ xy1

plt.figure(figsize=figsize)
plt.scatter(xy1[0, :], xy1[1, :])
# no need to do hear homogenous normalization...
plt.scatter(xy1_t_then_s[0, :], xy1_t_then_s[1, :], marker="*")
plt.title("Translated and then scaled points")
plt.show()

# %% [markdown]
# ## Projective transformation

# %%

M_p = np.array([[1, 0, 0], [0, 20, 0], [0, 2, 1]])

M_p
# %%
xy1_p = M_p @ xy1

plt.figure(figsize=figsize)
plt.scatter(xy1[0, :], xy1[1, :])
# here we MUST do homogenous normalization!!!
plt.scatter(xy1_p[0, :] / xy1_p[2, :], xy1_p[1, :] / xy1_p[2, :], marker="*")
plt.title("Projected points")
plt.show()

# %%
