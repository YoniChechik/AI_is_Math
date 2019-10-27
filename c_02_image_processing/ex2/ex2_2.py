#%% [markdown]
# # EX2_2
# Find different words in newspaper article
# We'll do this using morphology operators and connected components.
# %%
# to run in google colab
import sys
if 'google.colab' in sys.modules:
    import subprocess
    subprocess.call('apt-get install subversion'.split())
    subprocess.call('export https://github.com/YoniChechik/AI_is_Math/trunk/c_02_image_processing/ex2/news.jpg'.split())

# %%
import numpy as np
import matplotlib.pyplot as plt
import cv2

figsize = (10, 10)

#%%
im = cv2.imread("news.jpg")
im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

plt.figure(figsize=figsize)
plt.imshow(im_gray,cmap="gray",vmin=0,vmax=255)
plt.show()

#%%
# TODO: let's start with turning the image to a binary one

plt.figure(figsize=(20,20))
plt.imshow(im_th)
plt.show()

#%%
# TODO: next, merge all pixels of the same word together to make one connected component using a morphologic operator

plt.figure(figsize=(20,20))
plt.imshow(dilated_im)
plt.show()

#%%

def find_words(dilated_im,im):
    res = im.copy()

    # TODO: draw rectengles around each word:
    # 1. find all connected components
    # 2. build a mask of only one connected component each time, and find it extremeties
    # TODO: did it came out perfect? Why? Why not?
    return res

def plot_rec(mask,res_im):
    # plot a rectengle around each word in res image using mask image of the word
    xy = np.nonzero(mask)
    y = xy[0]
    x = xy[1]
    left = x.min()
    right = x.max()
    up = y.min()
    down = y.max()

    res_im = cv2.rectangle(res_im, (left, up), (right, down), (0, 20, 200), 2)
    return res_im
#%%
plt.figure(figsize=(20,20))
plt.imshow(find_words(dilated_im,im))
plt.show()


#%%
# TODO: now we want to mark only the big title words, and do this ONLY using morphological operators


plt.figure(figsize=(20,20))
plt.imshow(find_words(binary_only_title_cc_img,im))
plt.show()
