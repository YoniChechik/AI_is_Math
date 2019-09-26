# ## Prep
# %%
# to run in google colab
import sys
if 'google.colab' in sys.modules:
    ! apt-get install subversion
    ! svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_03_edge_detection/ex3/butterfly_noisy.jpg

# %%
import numpy as np
import matplotlib.pyplot as plt
import cv2

figsize = (10, 10)
# %%
# to run interactively with vscode
import os
if os.getcwd().endswith("AI_is_Math"):
    os.chdir("c_02_image_processing/ex2")

#%%
im = cv2.imread("test2.jpg")
im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

plt.figure(figsize=figsize)
plt.imshow(im_gray,cmap="gray",vmin=0,vmax=255)
plt.show()
# #%%
# equ = cv2.equalizeHist(im_gray)
# plt.figure(figsize=figsize)
# plt.imshow(equ,cmap="gray",vmin=0,vmax=255)
# plt.show()
#%%
im_th = (im_gray<150).astype(np.uint8)

plt.figure(figsize=(20,20))
plt.imshow(im_th)
plt.show()

#%%
# kernel = np.ones((2,2),np.uint8)
# erode = cv2.erode(im_th,kernel,iterations = 1)

kernel = np.ones((1,6),np.uint8)
dilation = cv2.dilate(im_th,kernel,iterations = 1)

plt.figure(figsize=(20,20))
plt.imshow(dilation)
plt.show()

#%%
num_labels, labels = cv2.connectedComponents(dilation)

# for i in range(num_labels):

# def imshow_components(labels):
# Map component labels to hue val
# label_hue = np.uint8(179*labels/np.max(labels))
# blank_ch = 255*np.ones_like(label_hue)
# labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

# # cvt to BGR for display
# labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

# # set bg label to black
# labeled_img[label_hue==0] = 0

# plt.figure(figsize=(20,20))
# plt.imshow(labeled_img)
# plt.show()


#%%
# word_list = []
res = im.copy()
for i in range(1,num_labels):
    i_im = labels==i
    xy = np.nonzero(i_im)
    # print(xy)
    y = xy[0]
    x = xy[1]
    left = x.min()
    right = x.max()
    up = y.min()
    down = y.max()

    # word = im_th[up:down+1,left:right+1]
    # word_list.append(word)
    res = cv2.rectangle(res, (left, up), (right, down), (0, 20, 200), 2)

#%%
# for i in np.random.choice(np.arange(1,num_labels),10):
#     plt.figure(figsize=(20,20))
#     plt.imshow(word_list[i])
#     plt.show()
plt.figure(figsize=(20,20))
plt.imshow(res)
plt.show()


#%%

kernel = np.ones((5,5),np.uint8)
erode = cv2.erode(im_th,kernel,iterations = 1)

kernel = np.ones((1,1),np.uint8)
dilation = cv2.dilate(erode,kernel,iterations = 1)

plt.figure(figsize=(20,20))
plt.imshow(dilation)
plt.show()


#%%
