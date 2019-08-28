# %% [markdown]
# # Edge detection
# ## prep 

# %% 
import numpy as np
import cv2
from matplotlib import pyplot as plt
from aux_funcs import *

fig_size = (10,10)

import os
if not os.getcwd().endswith("p_03_edge_detection"):
    os.chdir("p_03_edge_detection")

# %% [markdown]
# ## original image
# %%
# bikes_url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/Bikesgray.jpg"
# img = get_image_from_url(bikes_url)
img = cv2.imread("Bikesgray.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure(figsize=fig_size)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title('original image')

# %% [markdown]
# ## filtering common errors
# ### kernel errors
# %% kernel errors
img = img.astype(float)  # 'uint8' doesn't work with minus sign - for filtering

# 1. cv2.filter2D is working with corelation rether than convolution
#    no need to flip the kernel
# 2. notice that kernel is 2D array - if 1d then column vector
kernel = np.array([[-1, 0, +1]])
dst = cv2.filter2D(img, -1, kernel)

plt.figure(figsize=fig_size)
plt.imshow(np.abs(dst), cmap='gray')
plt.colorbar()
plt.title('$f\'_x$: image filtered with '+str(kernel))

# %% [markdown]
# ### uint8 errors
# %% wrong filtering when keeping uint8 nstead of float
uint8_img = np.zeros((500, 500), dtype=np.uint8)
uint8_img[200:300, 200:300] = 1

kernel = np.array([[-1, 0, +1]])
dst = cv2.filter2D(uint8_img, -1, kernel)

fig, axs = plt.subplots(1, 2, figsize=(20,20))
axs[0].imshow(uint8_img, cmap='gray')
axs[0].title.set_text('original image')
axs[1].imshow(dst, cmap='gray')
axs[1].title.set_text('uint8 WRONG filtering')

# %% [markdown]
# ## y grad filter
# %%
kernel = np.array([[-1, 0, +1]]).T
dst = cv2.filter2D(img, -1, kernel)

plt.figure(figsize=fig_size)
plt.imshow(dst, cmap='gray')
plt.colorbar()
plt.title('$f\'_y$: image filtered with\n '+str(kernel))

# %% [markdown]
# ## comparison of x gradient filters
# %% comparison x gradient
plt.rcParams['figure.figsize'] = [20, 20]

plt.subplot(4, 2, 1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title('original image')

#######################################
kernel = 1/2*np.array([[-1, 0, +1]])
dst_sym = cv2.filter2D(img, -1, kernel)

plt.subplot(4, 2, 2)
plt.imshow(dst_sym, cmap='gray')
plt.title('$f\'_x$: image filtered with symmetric derivative')

#######################################
kernel = 1/6*np.array([
    [-1, 0, +1],
    [-1, 0, +1],
    [-1, 0, +1]])
dst_prewitt = cv2.filter2D(img, -1, kernel)

plt.subplot(4, 2, 3)
plt.imshow(dst_prewitt, cmap='gray')
plt.title('$f\'_x$: image filtered with Prewitt')

#######################################
# cv2.Sobel() also exist
kernel = 1/8*np.array([
    [-1, 0, +1],
    [-2, 0, +2],
    [-1, 0, +1]])
dst_sobel = cv2.filter2D(img, -1, kernel)

plt.subplot(4, 2, 4)
plt.imshow(dst_sobel, cmap='gray')
plt.title('$f\'_x$: image filtered with Sobel')

#######################################
plt.subplot(4, 2, 5)
plt.imshow(np.abs(dst_sobel-dst_sym))
plt.colorbar()
plt.title('|sobel-symmetric|')

#######################################
plt.subplot(4, 2, 6)
plt.imshow(np.abs(dst_sobel-dst_prewitt))
plt.colorbar()
plt.title('|sobel-prewitt|')

#######################################
plt.subplot(4, 2, 7)
plt.imshow(np.abs(dst_sym-dst_prewitt))
plt.colorbar()
plt.title('|symmetric-prewitt|')
# %% [markdown]
# ## magnitude and phase images

# %%
kernel = 1/8*np.array([
    [-1, 0, +1],
    [-2, 0, +2],
    [-1, 0, +1]])
sobel_x = cv2.filter2D(img, -1, kernel)

kernel = kernel.T
sobel_y = cv2.filter2D(img, -1, kernel)

mag_img = np.sqrt(sobel_x**2+sobel_y**2)

phase_img = cv2.phase(sobel_x, -sobel_y, angleInDegrees=True)

phase_img_masked = -100*np.ones(phase_img.shape)
TH_PRC = 0.15
th = mag_img.max()*TH_PRC
phase_img_masked = phase_img_masked*(mag_img <= th) + phase_img*(mag_img > th)


bokeh_imshow(mag_img, scale=1, colorbar=True,
             show=True, title='gradient magnitude')

bokeh_imshow(phase_img_masked, scale=1, colorbar=True,
             show=True, title='gradient phase thresholeded')

# %% [markdown]
# ## Edge thinning 
# <div id="foo"></div>
# ### LoG filter

# %%
blur = cv2.blur(img, (1, 1))
kernel = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]])
dst_sobel = cv2.filter2D(blur, -1, kernel)

plt.figure(figsize=fig_size)
plt.imshow(dst_sobel)
# %% [markdown]
# ### naive way for zero crossings

# %%
sign_im = dst_sobel > 0
sign_im_left = sign_im[:, :-1]
sign_im_right = sign_im[:, 1:]
res = np.logical_xor(sign_im_left, sign_im_right)

sign_im_left = res[:, 1:]
sign_im_right = res[:, :-1]
res = np.logical_and(sign_im_left, sign_im_right)

plt.figure(figsize=fig_size)
plt.imshow(res)
plt.title('naive way for zero crossings')


# %% [markdown]
# ## quantizing the phase image

# %%
phase_img_q = phase_img.copy()
for i in range(mag_img.shape[0]):
    for j in range(mag_img.shape[1]):
        phase_img_q[i, j] = np.mod(phase_img_q[i, j]+22.5, 180)
        phase_img_q[i, j] = (phase_img_q[i, j])//45  # integer devider

phase_img_q_masked = -1*np.ones(phase_img.shape)
TH_PRC = 0.1
th = mag_img.max()*TH_PRC
phase_img_q_masked = phase_img_q_masked * \
    (mag_img <= th) + phase_img_q*(mag_img > th)

bokeh_imshow(phase_img_q_masked, scale=1, colorbar=True, show=True,
             title='gradient phase- quantized and thresholded')


# %% [markdown]
# ## NMS

# %%
nms = mag_img.copy()

for i in range(1, mag_img.shape[0]-1):
    for j in range(1, mag_img.shape[1]-1):
        if phase_img_q[i, j] == 0 and (mag_img[i, j+1] > mag_img[i, j] or mag_img[i, j-1] > mag_img[i, j]):
            nms[i, j] = -50
        if phase_img_q[i, j] == 1 and (mag_img[i+1, j-1] > mag_img[i, j] or mag_img[i-1, j+1] > mag_img[i, j]):
            nms[i, j] = -50
        if phase_img_q[i, j] == 2 and (mag_img[i-1, j] > mag_img[i, j] or mag_img[i+1, j] > mag_img[i, j]):
            nms[i, j] = -50
        if phase_img_q[i, j] == 3 and (mag_img[i-1, j-1] > mag_img[i, j] or mag_img[i+1, j+1] > mag_img[i, j]):
            nms[i, j] = -50

bokeh_imshow(nms, scale=1, colorbar=True, show=True, title='NMS')

# %% [markdown]
# ## double TH

# %%
nms_th = np.zeros(nms.shape)
TH_l = 3
TH_h = 13
nms_th[nms >= TH_h] = 2
nms_th[np.bitwise_and(TH_l <= nms, nms < TH_h)] = 1

bokeh_imshow(nms_th, scale=1, colorbar=True, title='double TH')

# %% [markdown]
# ## iterative hysteresis

# %%
canny_res = nms_th.copy()

canny_progress = []
is_weak_to_strong = True
while is_weak_to_strong:
    is_weak_to_strong = False
    for i in range(1, nms.shape[0]-1):
        for j in range(1, nms.shape[1]-1):
            if canny_res[i, j] == 2:
                weak_edges_mask = canny_res[i-1:i+2, j-1:j+2] == 1
                if np.any(weak_edges_mask):
                    is_weak_to_strong = True
                    canny_res[i-1:i+2, j-1:j+2][weak_edges_mask] = 2
    # for later
    canny_progress.append(canny_res.copy())

#all other weak edges are not edges...
canny_res[canny_res == 1] = 0

bokeh_imshow(canny_res, scale=1, title='Canny final result')

# %% [markdown]
# ### let's see the iterative process in depth
# **Note:** this process can also be done with connected components!
#%%
import ipywidgets as widgets

slider_out = widgets.IntSlider(
    description='frame num',
    value=0, # initial running value
    min=0,
    max=len(canny_progress)-1,
    step=10,
    continuous_update=False # False -> update only after user finished sliding
    ) 

def fig_update_func(frame_num):
    plt.figure(figsize=fig_size) # figure MUST be defined inside update func
    plt.imshow((canny_progress[frame_num]*255/2).astype(np.uint8))
    plt.title("frame num "+str(frame_num))
    plt.show()
    
out = widgets.interactive_output(fig_update_func, {'frame_num': slider_out})

widgets.HBox([slider_out, out])
# %% [markdown]
# ## cv2 Canny

# %%
res = cv2.Canny(img.astype(np.uint8),105,120)
bokeh_imshow(res, scale=1, title='cv2.Canny final result')

# %%
