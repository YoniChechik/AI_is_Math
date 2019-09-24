#%% [markdown]
# # EX4: Circle Hough transform
# In the ex. we will implement step by step circle hough transform.
# Follow the code and fill in the missing parts
# ## Prep
# %%
# to run in google colab
import sys
if 'google.colab' in sys.modules:
    ! apt-get install subversion
    ! svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_04_curve_fitting/ex4/circles.bmp
    ! svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_04_curve_fitting/ex4/coins.png

# %%
import numpy as np
import matplotlib.pyplot as plt
import cv2
from aux_funcs import *


fig_size = (10, 10)
# %%
# to run interactively with vscode
import os
if os.getcwd().endswith("AI_is_Math"):
    os.chdir("c_05_image_formation/ex5")

#%%
calib_im = cv2.imread("calib_im.jpg")
calib_im = cv2.cvtColor(calib_im,cv2.COLOR_BGR2GRAY)
im_norm = calib_im.astype(float) - 255/2

X = np.arange(0, im_norm.shape[1])
Y = np.arange(0, im_norm.shape[0])
X, Y = np.meshgrid(X, Y)

x = X.reshape(-1,1)
y = Y.reshape(-1,1)
z = im_norm.reshape(-1,1)
#%%
rand_inds = np.random.choice(np.arange(x.shape[0]),10000)
xi = x[rand_inds,0].reshape(-1,1)
yi = y[rand_inds,0].reshape(-1,1)
zi = z[rand_inds,0].reshape(-1,1)
#%%
A = np.concatenate((xi,yi,xi*yi,xi**2,yi**2,yi**2*xi**4,yi**4*xi**2,xi**4*yi**4,yi**6,xi**6,np.ones(xi.shape)),axis=1)
b = np.linalg.lstsq(A, zi, rcond=None)[0]
#%%


A_full = np.concatenate((x,y,x*y,x**2,y**2,y**2*x**4,y**4*x**2,x**4*y**4,y**6,x**6,np.ones(x.shape)),axis=1)

rec = A_full@b
rec_im = rec.reshape(im_norm.shape)
plt.figure()
plt.imshow(rec_im)
plt.colorbar()
plt.show()

#%%
np.sqrt(np.mean((rec_im-im_norm)**2))



bokeh_imshow(np.abs(rec_im-im_norm), scale=0.5, colorbar=True, show=True,
             title='Gradient phase- quantized and thresholded')

#%%
b

#%%
