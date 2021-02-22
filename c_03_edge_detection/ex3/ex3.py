# %%
# to run in google colab
import sys
if 'google.colab' in sys.modules:
    import subprocess 
    subprocess.call('apt-get install subversion'.split())
    subprocess.call('svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_03_edge_detection/ex3/butterfly_noisy.jpg'.split())

# %%
import numpy as np
import matplotlib.pyplot as plt
import cv2

figsize = (10, 10)

# %%
def gaussian(x, sigma,mu=0):
    # TODO: get gaussin results (one line)
    return None

def distance(x, y, i, j):
    # TODO: get L2 distance function between two points (one line)
    return None

# %%
def bilateral_one_pixel(source, x, y, d, sigma_r, sigma_s):
    # === init vars
    filtered_pix = 0
    Wp = 0

    # TODO: 
    # 1. run on all neighboors (~3 lines)
    # 2. if neighboor out of matrix indices - don't count him in your computation (~2 lines)
    # 3. find filtered_pix (~6 lines)


    # make result uint8
    filtered_pix = np.clip(filtered_pix,0,255).astype(np.uint8)
    return filtered_pix

# %%
def bilateral_filter(source, d, sigma_r, sigma_s):
    # build empty filtered_image
    filtered_image = np.zeros(source.shape,np.uint8)  
    #make input float 
    source = source.astype(float)
    # d must be odd!
    d = np.floor(d/2)+1

    # TODO: run on all pixels with bilateral_one_pixel(...) (~4 lines)

    return filtered_image

# %%
#upload noisy image
src = cv2.imread("butterfly_noisy.jpg")
src = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(10,10))
plt.imshow(src,cmap=gray,vmin=0,vmax=255)
plt.colorbar()
plt.show()

# %%
# run bilateral_filter(...)
d = 5 #edge size of neighborhood perimeter 
sigma_r = 12 # sigma range
sigma_s = 16 # sigma spatial

filtered_image = bilateral_filter(src, d, sigma_r, sigma_s)

plt.figure(figsize=(10,10))
plt.imshow(filtered_image)
plt.colorbar()
plt.show()

# %%
# compare to opencv
filtered_image_OpenCV = cv2.bilateralFilter(src, d, sigma_r, sigma_s)

plt.figure(figsize=(10,10))
plt.imshow(filtered_image_OpenCV)
plt.colorbar()
plt.show()

# %%
# compare to regular gaussian blur
blur = cv2.GaussianBlur(gauss_noise_im,(d,d),sigma_s)
plt.figure(figsize=(10,10))
plt.imshow(blur)
plt.colorbar()
plt.show()

# %%
# copare canny results between the two images
th_low = 100
th_high = 200
res = cv2.Canny(filtered_image,th_low,th_high)
plt.figure(figsize=(10,10))
plt.imshow(res)
plt.colorbar()
plt.show()

res = cv2.Canny(gauss_noise_im,th_low,th_high)
plt.figure(figsize=(10,10))
plt.imshow(res)
plt.colorbar()
plt.show()
