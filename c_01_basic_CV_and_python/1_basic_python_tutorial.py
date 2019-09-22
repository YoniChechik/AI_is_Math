# %% [markdown]
# # Python Workshop: Basics I
#
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YoniChechik/AI_is_Math/blob/master/c_01_basic_CV_and_python/site_data/site_data1_basic_python_tutorial.ipynb)
#
#  <hr>
#
# Based on:
#
# this [git](https://github.com/zhiyzuo/python-tutorial) of Zhiya Zuo
#
# &
#
# tutorials from [tutorialspoint](https://www.tutorialspoint.com/python)
#
# <hr>
#
# ## Introduction
#
# Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability. The language construction and object-oriented approach aims to help programmers write clear, logical code for small and large-scale projects. [Wikipedia]
#
# - Python is Interpreted - Python is processed at runtime by the interpreter. You do not need to compile your program before executing it. This is similar to PERL, PHP and MATLAB.
#
# - Python is Interactive - You can actually sit at a Python prompt and interact with the interpreter directly to write your programs.
#
# - Python is Object-Oriented - Python supports Object-Oriented style or technique of programming that encapsulates code within objects.
#
# - Popular Language for Data Analysis - Most of the time, you will need external packages to assist data analyses.
#
#  ![Python Packages](http://i.imgur.com/Q8trGd1.png)
#
# ### PyCharm
#
# Pycharm is currently (2019) the most commonly used IDE (Integrated development environment) for programing in python.
#
# for complete tutorial on **installation** of Python + Pycharm + additional packages please refer to [this](https://github.com/YoniChechik/AI_is_Math/blob/master/python_pycharm_installation/python_pycharm_installation.md) page.
#
# <img src="https://upload.wikimedia.org/wikipedia/commons/a/a1/PyCharm_Logo.svg" alt="pycharm logo" width="200"/>
#
# ### Jupyter notebook
#
# Jupyter is an easy way to merge code and explanations in a beautiful way.
#
# The easiest way to interact with such notebook (.ipynb) is with [google colab](https://colab.research.google.com). There you can run each cell independently or all cells combined through 'Runtime' section or the play button.
#
# the main disadvantage of google colab is that debugging there is problematic.
#
# <img src="https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg" alt="jupyter logo" width="200"/>
#
# ### Naming convention
# 
# There are two commonly used style in programming:
#
# 1. __camelCase__
# 2. __snake_case__ or __lower_case_with_underscore__
#
# Always make sure you use one convention consistently across one project.
#
# All variable (function and class) names must start with a letter or underscore (_). You can include numbers, but it can't be the first char.

# %%
myStringHere = 'my string'  # valid
x = 3  # valid
x_3 = "xyz"  # valid
# 3_x = "456" # invalid. Numbers cannot be in the first position.

# %% [markdown]
# ### Lines and indentation
# Python doesn't need braces to indicate blocks of code for class and function definitions or flow control. 
# Blocks of code are denoted by line indentation (Tabs), which is rigidly enforced.

# %%
if True:
    print("True")
else:
    print("False")

# %% [markdown]
# ### Indexing
#
# Indexing in python start from 0 (like c, unlike Matlab). Accessing a range of list/array is, by convetion, `some_list[start_ind:end_ind_minus_one]`
#

# %%
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

y = x[0] #get element 0 
print("y = " + str(y))

y = x[2] #get element 2 
print("y = " + str(y))

y = x[0:2] #get elements 0,1
print("y = " + str(y))

y = x[:2]  # same as [0:2]
print("y = " + str(y))

y = x[3:10]
print("y = " + str(y))

y = x[3:]  # same as above
print("y = " + str(y))

# %% [markdown]
# You can also go to last element easily:

# %%
y = x[-1]  # last element
print("y = " + str(y))

y = x[:-1]  # all until the last element - noninclusive
print("y = " + str(y))

y = x[-3:]  # last three elements
print("y = " + str(y))

# %% [markdown]
# Step size is also an option:

# %%
y = x[0:3:2]  # only evens until 3 noninclusive
print("y = " + str(y))

y = x[1:5:2]  # only odds until 5 noninclusive
print("y = " + str(y))

y = x[::3]  # +3 step size - entire list
print("y = " + str(y))

y = x[::-1]  # reverse!
print("y = " + str(y))

# %% [markdown]
# ## Primitives
# In this section, we go over some common primitive data types in Python.
# While the word _primitive_ looks obscure, we can think of it as the most basic data type that cannot be further decomposed into simpler ones.
# ### Numbers
# numbers without fractional partsare called ___integer___. In Python, they are abbreviated as `int`

# %%
x = 3
type(x)

# %% [markdown]
# numbers with fractional part are floating point numbers. They are named `float` in Python.

# %%
y = 3.0
type(y)

# %% [markdown]
# We can apply arithmetic to these numbers. However, one thing we need to be careful about is ___type conversion___. See the example below.

# %%
z = 2 * x  # int times int
type(z)


# %%
z = y ** x  # int to the power float
print(z)
type(z)


# %%
z = x / 2  # what will happen when dividing two ints?
z

# %% [markdown]
# ### Boolean
# Boolean type comes in handy when we need to check conditions. For example:

# %%
my_error = 1.6
compare_result = my_error < 0.1
print(compare_result)
print(type(compare_result))

# %% [markdown]
# There are two valid Boolean values: `True` and `False`. We can also think of them as `1` and `0`, respectively.

# %%
my_error > 0

# %% [markdown]
# When we use Boolean values for arithmetic operations, they will become `1/0` automatically

# %%
(my_error > 0) + 2

# %% [markdown]
# ### Strings
# In Python, we use `str` type for storing letters, words, and any other characters.
#
# To initialize a string variable, you can use either double or single quotes.

# %%
my_str1 = "see you"
print(my_str1)
print(type(my_str1))

my_str2 = 'see you later'
print(my_str2)
print(type(my_str2))

# %% [markdown]
# We can also use `+` to _concatenate_ different strings

# %%
my_str1 + ' tomorrow'

# %% [markdown]
# One way of formatting strings is equivalent to c language:

# %%
print("1/3 is approximately %.2f" % (1/3))  # %f for floating point number
print(" '%s' != '%s'" % (my_str1, my_str2))  # %s for string

# %% [markdown]
# you can also simply do string concatenation:

# %%
print("Printing a string: " + my_str1 + ", and printing a number: " + str(3))

# %% [markdown]
# `str` is an **iterable object,** meaning that we can iterate through each individual character:

# %%
print(my_str1[0])
print(my_str1[2:6])

# %% [markdown]
# ## Data Structures
# In this section, we discuss some ___nonprimitive___ data structures in Python.
# ### List
# Initialize a list with brackets. You can store anything in a list, even if they are different types
#

# %%
a_list = [1, 2, 3]  # commas to separate elements
print("Length of a_list is: %i" % (len(a_list)))
print("The 3rd element of a_list is: %s" %
      (a_list[2]))  # Remember Python starts with 0
print("The last element of a_list is: %s" % (a_list[-1]))  # -1 means the end
print("The sum of a_list is %.2f" % (sum(a_list)))

# %% [markdown]
# We can put different types in a list

# %%
b_list = [20, True, "good", "good"]
print(b_list)

# %% [markdown]
# Update a list: __pop__, __remove__, __append__, __extend__

# %%
print(a_list)
print("Pop %i out of a_list" % a_list.pop(1))  # pop the value of an index
print(a_list)


# %%
print("Remove the string good from b_list:")
b_list.remove("good")  # remove a specific value (the first one in the list)
print(b_list)


# %%
a_list.append(10)
print("After appending a new value, a_list is now: %s" % (str(a_list)))

# %% [markdown]
# merge `a_list` and `b_list`:

# %%
a_list.extend(b_list)
print("Merging a_list and b_list: %s" % (str(a_list)))

# %% [markdown]
# We can also use `+` to concatenate two lists

# %%
a_list + b_list

# %% [markdown]
# ### Tuple
# Tuple is a special case of list whose elements cannot be changed (immutable).
#
# Initialize a tuple with parenthesis:

# %%
a_tuple = (1, 2, 3, 10)
print(a_tuple)
print("First element of a_tuple: %i" % a_tuple[0])

# %% [markdown]
# You can't change the values of a tuple:

# %%
# a_tuple[0] = 5

# %% [markdown]
# In order to create a single value tuple, you need to add a ','

# %%
a_tuple = (1)  # this would create a int type
print(type(a_tuple))
b_tuple = (1,)  # this would create a tuple type, take note of the comma.
print(type(b_tuple))

# %% [markdown]
# ### Dictionary
#  Dictionary: key-value pairs
#
# Initialize a dict by curly brackets `{}`

# %%
d = {}  # empty dictionary
# add a key-value by using bracket (key). You can put anything in key/value.
d[1] = "1 value"
print(d)


# %%
# Use for loop to add values
for index in range(2, 10):
    d[index] = "%i value" % index
print(d)
print("All the keys: " + str(d.keys()))
print("All the values: " + str(d.values()))


# %%
for key in d:
    print("Key is: %i, Value is : %s" % (key, d[key]))

# %% [markdown]
# ###Side note: mutable Vs. immutable objects
#
# **Everything in Python is an object**, and object can be either mutable (changeable after creation) or immutable.
# Almost all Python objects are mutable, except from the primitives (numbers, booleans, strings) and tuples
#
# Why it's interesting? because when you reference a new variable, it's always soft link (like a shortcut in windows), and if you change a mutable object, it reference changes too! Something that can cause big bugs!

# %%
# mutable object: no problem
a = 'Hello'
b = a
b = b + ' World!'
print(a)
print(b)


# %%
# immutable object: big problem
a = ['Hello']
b = a
b[0] = 'World!'
print(a)
print(b)


# %%
# use .copy() to overcome this:

c = a.copy()
c[0] = "other world"
print(a)
print(c)
