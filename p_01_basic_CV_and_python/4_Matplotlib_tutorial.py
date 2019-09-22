#%% [markdown]
# #Python Workshop: Matplotlib
#
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YoniChechik/AI_is_Math/blob/master/p_01_basic_CV_and_python/4_Matplotlib_tutorial.ipynb)
#
# <hr>
# 
# Based on:
# 
# This [git](https://github.com/zhiyzuo/python-tutorial) of Zhiya Zuo
# 
# <hr>
#%%
import numpy as np
import matplotlib.pyplot as plt

fig_size = (10, 10)

#%% [markdown]
# ## Introduction
# Visualization is one of the most important things of data analysis. Besides just producing ___readable___ plots, we should make an effort to improve the overall attractiveness of the plots. `matplotlib` is a powerful package for ___Python___ users. Let's start with an example.
# ### Anatomy of a Figure
# Before we go deeper, let's take a look at the structure of a figure in `matplotlib`:
# 
# <img width=700 src="https://matplotlib.org/_images/anatomy1.png">
#
# ## Line plot
# First we generate sample data

#%%
X_arr = np.arange(10)
Y_arr = 3*X_arr + 2 + np.random.random(size=X_arr.size) # linear with some noise
print(X_arr)
print(Y_arr)

#%% [markdown]
# To plot a simple scatter plot, we can use `plt.scatter()` function

#%%
plt.figure(figsize=fig_size)
plt.plot(X_arr, Y_arr)

#%% [markdown]
# ## Scatter plot

#%%
plt.figure(figsize=fig_size)
# Use `+` as marker; color set as `g` (green); size proportion to Y values
plt.scatter(X_arr, Y_arr, marker='+', c='g') 
# How about adding a line to it? Let's use `plt.plot()`
# set line style to dashed; color as `r` (red) 
plt.plot(X_arr, Y_arr,'--r')
# set x/y axis limits: first two are xlow and xhigh; last two are ylow and yhigh
plt.axis([0, 10, 0, 35])
# set x/y labels
plt.xlabel('My X Axis')
plt.ylabel('My Y Axis')
# set title
plt.title('My First Plot')
plt.legend(['line','datapoints'])

#%% [markdown]
# ## Coding style
# Another possible way to work with figures in `matplotlib`:

#%%
# `plt.subplots()` returns a figure object (which is the whole thing as shown above)
# and `axes` that control specific plots in the figure.
# Here our "subplots" layout is by default 1 row and 1 col and therefore 1 plot
fig, ax = plt.subplots(figsize=fig_size)


# plot should be done on the `axis`: ax
ax.plot(X_arr, Y_arr)

#%% [markdown]
# Applying what we did earlier:

#%%
fig, ax = plt.subplots(figsize=fig_size)
# What we just did, applying to `ax`
ax.scatter(X_arr, Y_arr, marker='+', c='g', s=Y_arr*10) 
ax.plot(X_arr, Y_arr, linestyle='dashed', color='k')
ax.axis([0, 10, 0, 35])
ax.set_xlabel('My X Axis')
ax.set_ylabel('My Y Axis')
ax.set_title('My First Plot')

#%% [markdown]
# This is especially useful when handling multiple plots in one figure.

#%%
# Now the returned `ax_arr` would be np array with a shape a 2x3
fig, ax_arr = plt.subplots(2,3,figsize=fig_size)
ax_arr[0,0].plot(X_arr, Y_arr)
ax_arr[0,1].scatter(X_arr, Y_arr)
fig.suptitle("my subplots")

#%% [markdown]
# ## Histogram
# Let's use a Gaussian distribution for illustration

#%%
mu, sigma = 15, 1
gaussian_arr = np.random.normal(mu, sigma, size=10000)
np.mean(gaussian_arr), np.std(gaussian_arr, ddof=1)

#%%
fig, ax = plt.subplots(figsize=fig_size)
# `hist()` will return something but we usually do not need.
freq_arr, bin_arr, _ = ax.hist(gaussian_arr)

#%% [markdown]
# We can actually customize and make it prettier

#%%
fig, ax = plt.subplots(figsize=fig_size)
# Facecolor set to green; transparency (`alpha`) level: 30%
freq_arr, bin_arr, _ = ax.hist(gaussian_arr, facecolor='g', alpha=0.3)
# Add grid
ax.grid()

#%% [markdown]
# ## 3D plots

#%%
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure(figsize=fig_size)
ax = fig.gca(projection='3d') # get current axis
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
ax.plot(x, y, z, label='parametric curve')
ax.legend()

#%% [markdown]
# ## Note on IDE plotting
# In regular IDE plotting, after each plot one should put
# 
# ```
# plt.show()
# ```
# to show the pop-up plot window in which one can interact with the plots (zoom, rotate, etc.), and this will stop the run of your program until closed.
# 
# A way to overcome this is running:
# 
# ```
# plt.show(block=False)
# ```
# but then when the script completes, all figures are closed...
# 
# My preferred solution is running with `block=False` to all figures except the last one.
# 