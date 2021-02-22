# %% [markdown]
# #Python Workshop: NumPy
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YoniChechik/AI_is_Math/blob/master/c_01_intro_to_CV_and_Python/NumPy_tutorial.ipynb)
#
# <hr>
#
# Based on:
#
# This [git](https://github.com/zhiyzuo/python-tutorial) of Zhiya Zuo
#
# <hr>
#
# NumPy is the fundamental package for scientific computing with Python. It contains among other things:
#
# - Powerful N-dimensional array object.
# - Useful linear algebra, Fourier transform, and random number capabilities.
# - And much more
#
# <img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/NumPy_logo.svg" alt="numpy logo" width="200"/>
#
# ## NumPy installation
#
# in the cmd run:
#
# ```bash
# pip install numpy
# ```
# ## Arrays

# %%
# After you install numpy, load it
import numpy as np  # you can use np instead of numpy to call the functions in numpy package


# %%
x = np.array([1, 2, 3])  # create a numpy array object
print(type(x))

# %% [markdown]
# We can call `shape` function designed for `numpy.ndarray` class to check the dimension

# %%
x.shape  # can be compared to 'len()' function that is used with list size

# %% [markdown]
# Unlike `list`, we have to use one single data type for all elements in an array

# %%
y = np.array([1, 'yes'])  # automatic type conversion from int to str
y

# %% [markdown]
# ### Multidimensional arrays

# %%
arr = np.array([[1, 2, 3, 8]])
arr.shape

# %%
arr

# %%
arr = np.array([[1, 2, 3, 8], [3, 2, 3, 2], [4, 5, 0, 8]])
arr.shape

# %%
arr

# %% [markdown]
# ### Special arrays
# There are many special array initialization methods to call:

# %%
np.zeros([3, 5], dtype=int)  # dtype can define the type of the array


# %%
np.ones([3, 5])


# %%
np.eye(3)

# %% [markdown]
# ## Operations
# The rules are very similar to R/Matlab: they are generally element wise

# %%
arr

# %%
arr - 5

# %%
arr * 6  # element-vise multiplication

# %%
arr * arr  # element-vise multiplication of two matrices

# %%
np.exp(arr)

# %% [markdown]
# More examples:

# %%
arr_2 = np.array([[1], [3], [2], [0]])
arr_2

# %%
arr_2_T = arr_2.T  # transpose
arr_2_T


# %%
arr @ arr_2  # matrix multiplication

# %%
arr

# %%
arr.max()

# %%
arr.cumsum()

# %% [markdown]
# **Note:** element-by-element operations is done row-by-row, unlike in Matlab (column-by-column)
# There are many class methods to calculate some statistics of the array itself along some axis:
# - `axis=1` means row-wise
# - `axis=0` means column-wise

# %%
arr.cumsum(axis=1)

# %% [markdown]
# ### Note about 1d arrays
# 1d array is **not a column vector** & **not entirely a row vector** and hence should be treated carefully when used with vector/matrix manipulation

# %%
a = np.array([1, 2, 3])
a, a.shape

# %%
c = np.array([[1, 2, 3]])
c, c.shape  # notice the shape diff

# %%
# can be multiply like a row vector
b = np.array([[1, 2], [3, 4], [5, 6]])
b

# %%
a @ b

# %%
# can't be transformed!
a.T, a.T.shape

# %% [markdown]
# A trick to transform 1d array into 2d row vector:

# %%
a_2d = a.reshape((1, -1))  # '-1' means to put all the rest of the elements in such a way that the reshape could fit
print(a_2d)
print(a_2d.T)

# %% [markdown]
# ## Indexing and slicing
# The most important part is how to index and slice a `np.array`. It is actually very similar to `list`, except that we now may have more index elements because there are more than one dimension for most of the datasets in real life
# ### 1 dimensional case

# %%
a1 = np.array([1, 2, 8, 100])
a1

# %%
a1[0]

# %%
a1[-2]

# %%
a1[[0, 1, 3]]

# %%
a1[1:4]

# %% [markdown]
# We can also use boolean values to index
# - `True` means we want this element

# %%
a1 > 3

# %% [markdown]
# ### Masking
# replacing values of array with another values according to a boolean mask
# %%
# this is the mask
a1[a1 > 3]

# %%
# this is a use of the above mask
a1[a1 > 3] = 100
a1
# %% [markdown]
# ### 2 dimensional case

# %%
arr

# %% [markdown]
# Using only one number to index will lead to a subset of the original multidimensional array: also an array

# %%
arr[0]


# %%
type(arr[0])

# %% [markdown]
# Since we have 2 dimensions now, there are 2 indices we can use for indexing the 2 dimensions respectively

# %%
arr[0, 0]

# %% [markdown]
# We can use `:` to indicate everything along that axis

# %%
arr[1]


# %%
arr[1, :]


# %%
arr[:, 1]  # watch out! we've got a 1d array again instead of column vector as maybe expected

# %%
# 2D masking
arr[arr > 3] = 55

# %% [markdown]
# ### 3 dimensional case
# As a final example, we look at a 3d array:

# %%
np.random.seed(1234)
arr_3 = np.random.randint(low=0, high=100, size=24)
arr_3

# %% [markdown]
# We can use `reshape` to manipulate the shape of an array

# %%
arr_3 = arr_3.reshape(3, 4, 2)
arr_3

# %% [markdown]
# **Note**: Are the printed array not what you though it would be? Did they mixed the shape? No!
# see [this for answers](https://stackoverflow.com/a/22982371/4879610)

# %%
arr_3[0]

# %%
arr_3[:, 3, 1]

# %%
arr_3[2, 3, 1]
