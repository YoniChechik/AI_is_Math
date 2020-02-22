# %% [markdown]
# # HSV color space
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YoniChechik/AI_is_Math/blob/master/c_02a_basic_image_processing/hsv.ipynb)

#%%
# to run in google colab
import sys
if 'google.colab' in sys.modules:
    import subprocess
    subprocess.call('apt-get install subversion'.split())
    subprocess.call('svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_02a_basic_image_processing/grass.jpg'.split())

#%%
# Adopted from: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html

import numpy as np
import cv2
import matplotlib.pyplot as plt 

figsize = (10,10)

# %% [markdown]
# Import basic image:

#%%
im = cv2.imread("grass.jpg")
plt.figure(figsize=figsize)
plt.imshow(cv2.cvtColor(im,cv2.COLOR_BGR2RGB))
# %% [markdown]
# We want to separate the grass from the sky. we'll do this by masking all pixels in the image that are not green.
# 
# First, find HSV green

#%%
rgb_green = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(rgb_green,cv2.COLOR_RGB2HSV)[0,0,:]
print(hsv_green)

# %% [markdown]
# Second, convert the image to HSV and threshold only the green color and neighborhood.
#
# We will take hue TH of +30 and -70 (because it's farther from blue- the sky).
# Let's take all saturation and value variants of green in the TH.
#
# Masking all that is in the TH should give us only the grass

#%%
# Convert BGR to HSV
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

# define range of hue and intensity 
lower_blue = hsv_green-np.array([70,200,200])
upper_blue = hsv_green+np.array([30,0,0])

# Threshold the HSV image
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(im,im, mask= mask)


plt.figure(figsize=figsize)
plt.imshow(mask)
plt.title("resulted mask")
plt.figure(figsize=figsize)
plt.imshow(cv2.cvtColor(res,cv2.COLOR_BGR2RGB))
plt.title("output image")