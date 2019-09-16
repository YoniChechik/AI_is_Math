# %% [markdown]
# # Hough transform
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YoniChechik/AI_is_Math/blob/master/p_02_image_processing/noise_and_filtering.ipynb)
# ## Prep

#%%
# to run in google colab
import sys
if 'google.colab' in sys.modules:
    ! apt-get install subversion
    ! svn export https://github.com/YoniChechik/AI_is_Math/trunk/p_02_image_processing/Tour_Eiffel.jpg

# %% 
import numpy as np
import cv2
from matplotlib import pyplot as plt

fig_size = (10,10)
#%%
# to run interactively with vscode
import os
if os.getcwd().endswith("AI_is_Math"):
    os.chdir("p_04_curve_fitting")

#%%
# rect_im = np.zeros((100,100))
# rect_im[20:40,20] = 100
# rect_im[20:40,40] = 100
# rect_im[20,20:40] = 100
# rect_im[40,20:41] = 100

# plt.figure()
# plt.imshow(rect_im)

# #%%
# plt.figure(figsize=(10,10))
# mag_img=cv2.Canny(rect_im.astype(np.uint8),0,1)
# plt.imshow(mag_img)


#%%
im = cv2.imread("building.jpg")
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

plt.imshow(im, cmap='gray', vmin=0, vmax=255)
plt.show()
#%%
plt.figure(figsize=(10,10))
mag_img=cv2.Canny(im,50,400)
plt.imshow(mag_img)
plt.show()

rect_im = mag_img
#%%
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html

rmax = np.sqrt(im.shape[0]**2+im.shape[1]**2)
r_step = rmax/(20*2)
r=np.arange(-rmax,rmax,r_step)

t_step = np.pi/(36*2)
t=np.arange(0,np.pi,t_step)

acc_mat = np.zeros((r.shape[0],t.shape[0]))

edge_inds = np.argwhere(rect_im>0)

xy_acc_mat = [[[]]*t.shape[0]]*r.shape[0]

for t_ind, t0 in enumerate(t):
    for yx in edge_inds:
        x = yx[1]
        y = yx[0]

        r0 = x*np.cos(t0)+y*np.sin(t0)
        r0 = np.round(r0/r_step)*r_step
        r_ind = np.argmin(np.abs(r0-r))
        # r_ind = np.argwhere(r == r0)[0,0]

        acc_mat[r_ind,t_ind]+=1
        # xy_acc_mat[r_ind][t_ind].append(yx)

# acc_mat>acc_mat.max()*0.9
# max_inds =np.argwhere(acc_mat>0)

# res_im = np.zeros(rect_im.shape)
# for i,yx in enumerate(max_inds):
#     print(str(i)+"out of"+str(max_inds.shape[0]))
#     xy_in_max_arr = xy_acc_mat[yx[0]][yx[1]]
#     for yx0 in xy_in_max_arr:
#         res_im[yx0[0],yx0[1]] =1 

plt.figure()
plt.imshow(acc_mat)
# plt.figure()
# plt.imshow(res_im)
# plt.title("res")
# # plt.xticks(t)
plt.show()

#%%
