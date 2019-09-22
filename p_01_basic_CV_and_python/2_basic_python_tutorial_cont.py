#%% [markdown]
# # Python Workshop: Basics II
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YoniChechik/AI_is_Math/blob/master/p_01_basic_CV_and_python/2_basic_python_tutorial_cont.ipynb)
#
# <hr>
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
# ## Control Logics
# 
# In the following examples, we show examples of comparison, `if-else` loop, `for` loop, and `while` loop.
# ### Comparison
# Python syntax for comparison is the same as our hand-written convention: 
# 
# 1. Larger (or equal): `>` (`>=`)
# 2. Smaller (or equal): `<` (`<=`)
# 3. Equal to: `==`
# 4. Not equal to: `!=`

#%%
3 == 5 

#%%
72 >= 2

#%%
test_str = "test"
test_str == "test" # can also compare strings

#%% [markdown]
# ### If-Else

#%%
sum_ =0


#%%
if sum_ == 0:
    print("sum_ is 0")
elif sum_ < 0:
    print("sum_ is less than 0")
else:
    print("sum_ is above 0 and its value is " + str(sum_)) # Cast sum_ into string type.

#%% [markdown]
# Comparing strings are similar

#%%
store_name = 'Walmart'

#%%
if 'Wal' in store_name:
    print("The store is not Walmart. It's " + store_name + ".")
else:
    print("The store is Walmart.")

#%% [markdown]
# ### For loop

#%%
for letter in store_name:
    print(letter)

#%% [markdown]
# `range()` is a function to create integer sequences:

#%%
a_range = range(5)
print(a_range)
print("range(5) gives" + str(list(range(5)))) # By default starts from 0
print("range(1,9) gives: " + str(list(range(1, 9)))) # From 1 to 8 (Again the end index is exclusive.)


#%%
for index in range(len(store_name)): # length of a sequence
    print("The %ith letter in store_name is: %s"%(index, store_name[index]))

#%% [markdown]
# #### List comprehensions 
# List comprehensions provides an easy way to create lists:

#%%
x = [i for i in range(10)]
print(x)

#%% [markdown]
# a lot of cool things can be done in one line!

#%%
x = [i + 2 for i in range(10)]
print(x)

x = [i ** 2 for i in range(10) if i%2==0]
print(x)

#%% [markdown]
# ### While loop

#%%
x = 2


#%%
while x < 10:
    print(x)
    x = x + 1

#%% [markdown]
# #### Notes on `break` and `continue`
# `break` means get out of the loop immediately. Any code after the `break` will NOT be executed.

#%%
store_name = 'Walmart'

#%%
index = 0
while True:
    print(store_name[index])
    index += 1 # a += b means a = a + b
    if store_name[index] == "a":
        print("End at a")
        break # instead of setting flag to False, we can directly break out of the loop
        print("Hello!") # This will NOT be run

#%% [markdown]
# `continue` means get to the next iteration of loop. It will __break__ the current iteration and __continue__ to the next.

#%%
for letter in store_name:
    if letter == "a":
        continue # Not printing a
    else:
        print(letter)

#%% [markdown]
# ## Functions
# Structure of a function
# ```python
# def func_name(arg1, arg2, arg3, ...):
#     #####################
#     # Do something here #
#     #####################
#     return output
# ```
# 
# return output` is **NOT** required
# ###One input one output

#%%
def F(n): # bonus- what this function does? 
    if n<=0: 
        print("Incorrect input") 
    elif n==1: 
        return 1
    elif n==2: 
        return 1
    else: 
        return F(n-1)+F(n-2) 


#%%
print(F(2))

print(F(3))

print(F(5))

print(F(7))

#%% [markdown]
# ###Multiple outputs
# reference- geometric sequence equations:
# 
# $a_n = a_1 \cdot q^{n-1}$
# 
# $S_n = \frac{a_1\cdot(q^n-1)}{q-1}$

#%%
def geo_seq(a_1, q, n):
    a_n = a_1 * (q ** (n-1))
    S_n = (a_1 * (q ** n - 1)) / (q - 1)
    return a_n, S_n


#%%
print(geo_seq(2, 2, 1)) # multiple outputs returns as a tuple

print(geo_seq(2, 2, 2))

print(geo_seq(2, 2, 2))

print(geo_seq(2, 2, 3)[1]) # get only second element

#%% [markdown]
# ### optional args

#%%
def geo_seq_optional_args(a_1, q=2, n=1):
    a_n = a_1 * (q ** (n-1))
    S_n = (a_1 * (q ** n - 1)) / (q - 1)
    return a_n, S_n


#%%
print(geo_seq_optional_args(2))

print(geo_seq_optional_args(2, n=2))

#%% [markdown]
# ##Classes
# As been said before- Python is object oriented programing (OOP) language, so every variable is actually an instance of some class.
# 
# Here are some class basics:

#%%
class Employee:

  # the function that is being called each time a new instance is created
  def __init__(self, name="Jhon", salary=10000):
    # per instance variables
    self.name = name
    self.salary = salary

  def display_employee(self):
    print("Name : " + self.name + ", Salary: "+ str(self.salary))
    
  def change_salary(self, new_salary):
    self.salary = new_salary


#%%
emp1 = Employee() #create new instance
emp1.display_employee()

emp2 = Employee("Bob", salary=20000) #create new instance
emp2.display_employee()

emp2.change_salary(30000)
emp2.display_employee()

# instance variables are also accessible - no such thing private/public vars
emp2.name = "Larry"
emp2.display_employee()

#%% [markdown]
# ## FIle I/O
# This section is about some basics on reading and writing data, in Python native style
# ### Write data to a file

#%%
f = open("tmp1.csv", "w") # f is a file handler, while "w" is the mode (w for write)
for item in range(6):
    f.write(str(item) + "\n") 
f.close() # close the filer handler for security reasons.

#%% [markdown]
# *Note that without the typecasting from `int` to `str`, an error will be raised.*
# A more commonly used way:

#%%
with open("tmp2.csv", "w") as f:
    for item in range(4):
        f.write(str(item))
        f.write("\n") 
# no need to close file, when out of 'with' scope the file closes automatically


#%% [markdown]
# Occasionally, we need to _append new elements_ instead of _overwriting_ existing files. In this case, we should use `a` mode in our `open` function:

#%%
with open("tmp2.csv", "a") as f: # 'a' == append to end of file
    for item in range(15, 19):
        f.write(str(item)+"\n")

#%% [markdown]
# ### Read data to a file
# To read a text file into Python, we use `r` mode (for _read_)

#%%
f = open("tmp1.csv", "r") # this time, use read mode
contents = [item.strip("\n") for item in f] # list comprehension. This is the same as for-loop but more concise + stripping newline
print(contents)
f.close()

#%% [markdown]
# Also using `with`:

#%%
with open("tmp2.csv", "r") as f:
  print(f.readlines())

#%%
# delete the files...
import os
os.remove("tmp1.csv")
os.remove("tmp2.csv")
#%% [markdown]
# ## Packages
# Often times, we need either internal or external help for complicated computation tasks. In these occasions, we need to _import packages_. 
# ### Built-in packages
# Python provides many built-in packages to prevent extra work on some common and useful functions
# 
# We will use __math__ as an example.

#%%
import math # use import to load a library

#%% [markdown]
# To use functions from the library, do: `library_name.function_name`. For example, when we want to calculate the logarithm using a function from `math` library, we can do `math.log`

#%%
x = 3
print("e^x = e^3 = %f"%math.exp(x))
print("log(x) = log(3) = %f"%math.log(x))

#%% [markdown]
# You can also import one specific function:

#%%
from math import exp # You can import a specific function
print(exp(x)) # This way, you don't need to use math.exp but just exp

#%% [markdown]
# Or all:

#%%
from math import * # Import all functions - not recommended do to overriding of functions

#%%
print(exp(x))
print(log(x)) # Before importing math, calling `exp` or `log` will raise errors

#%% [markdown]
# You can import a package with a shortened name:

#%%
import math as m
m.exp(3)

#%% [markdown]
# Depending on what you want to achieve, you may want to choose between importing a few or all (by `*`) functions within a package.
# ### External Packages
# There are times you'll want some advanced utility functions not provided by Python. There are many useful packages by developers.
# 
# We'll use __numpy__ as an example. (__numpy__, __scipy__, __matplotlib__,and probably __pandas__ will be of the most importance to you for data analyses.
# 
# Installation of packages for Python is the easiest using <a href="https://packaging.python.org/installing/" target="_blank">pip</a>:
# ```bash
# ~$ pip install numpy
# ```
# We'll see use for external packages later on.

#%%
