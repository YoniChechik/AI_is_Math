# %% [markdown]
# # Edge detection
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YoniChechik/AI_is_Math/blob/master/c_03_edge_detection/edge_detection.ipynb)

# %%
# to run in google colab
import sys

if "google.colab" in sys.modules:

    def download_from_web(url):
        import requests

        response = requests.get(url)
        if response.status_code == 200:
            with open(url.split("/")[-1], "wb") as file:
                file.write(response.content)
        else:
            raise Exception(
                f"Failed to download the image. Status code: {response.status_code}"
            )

    download_from_web(
        "https://github.com/YoniChechik/AI_is_Math/raw/master/c_03_edge_detection/Bikesgray.jpg"
    )


# save plotly as html frames
import plotly.io as pio

if (pio.renderers.default != "vscode") & (pio.renderers.default != "colab"):
    pio.renderers.default = "iframe_connected"
# %%
import cv2
import numpy as np
import plotly.express as px
from matplotlib import pyplot as plt

figsize = (10, 10)

# %% [markdown]
# ## Original image
# %%
img = cv2.imread("Bikesgray.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure(figsize=figsize)
plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.title("Original image")
plt.show()


# %% [markdown]
# ## Magnitude and phase images

# %%
img = img.astype(float)

kernel = 1 / 8 * np.array([[-1, 0, +1], [-2, 0, +2], [-1, 0, +1]])
sobel_x = cv2.filter2D(img, -1, kernel)

kernel = kernel.T
sobel_y = cv2.filter2D(img, -1, kernel)

mag_img = np.sqrt(sobel_x**2 + sobel_y**2)

phase_img = cv2.phase(sobel_x, -sobel_y, angleInDegrees=True)
# %% [markdown]
# ### Debug results
# %%
px.imshow(mag_img, title="Gradient magnitude")

# %%
phase_img_masked = -100 * np.ones(phase_img.shape)
TH_PRC = 0.15
th = mag_img.max() * TH_PRC
phase_img_masked = phase_img_masked * (mag_img <= th) + phase_img * (mag_img > th)

px.imshow(phase_img_masked, title="Gradient phase thresholeded")

# %% [markdown]
# ## Edge thinning
# ### LoG filter
# One way to implement edge thinning is to use LoG and then zero crossing finder.
# Below is an example of abs LoG. Look at the handlebar to see the zero crossings.
# %%
kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
dst_LoG = cv2.filter2D(img, -1, kernel)

px.imshow(np.abs(dst_LoG).clip(0, 300), title="abs LoG")

# %% [markdown]
# ## NMS
# Non maximum suppression (NMS) is another way for edge thinning.
# ### NMS preliminary step: Quantizing the phase image

# %%
phase_img_q = phase_img.copy()
for i in range(mag_img.shape[0]):
    for j in range(mag_img.shape[1]):
        phase_img_q[i, j] = np.mod(phase_img_q[i, j] + 22.5, 180)
        phase_img_q[i, j] = (phase_img_q[i, j]) // 45  # integer devider

# %% [markdown]
# ### Debug results
# %%
phase_img_q_masked = -1 * np.ones(phase_img.shape)
TH_PRC = 0.1
th = mag_img.max() * TH_PRC
phase_img_q_masked = phase_img_q_masked * (mag_img <= th) + phase_img_q * (mag_img > th)

px.imshow(phase_img_q_masked, title="Gradient phase- quantized and thresholded")


# %% [markdown]
# ### NMS main step

# %%
nms = mag_img.copy()

for i in range(1, mag_img.shape[0] - 1):
    for j in range(1, mag_img.shape[1] - 1):
        if phase_img_q[i, j] == 0 and (
            mag_img[i, j + 1] > mag_img[i, j] or mag_img[i, j - 1] > mag_img[i, j]
        ):
            nms[i, j] = -50
        if phase_img_q[i, j] == 1 and (
            mag_img[i + 1, j - 1] > mag_img[i, j]
            or mag_img[i - 1, j + 1] > mag_img[i, j]
        ):
            nms[i, j] = -50
        if phase_img_q[i, j] == 2 and (
            mag_img[i - 1, j] > mag_img[i, j] or mag_img[i + 1, j] > mag_img[i, j]
        ):
            nms[i, j] = -50
        if phase_img_q[i, j] == 3 and (
            mag_img[i - 1, j - 1] > mag_img[i, j]
            or mag_img[i + 1, j + 1] > mag_img[i, j]
        ):
            nms[i, j] = -50

px.imshow(nms, title="NMS")

# %% [markdown]
# ## double TH

# %%
nms_th = np.zeros(nms.shape)
TH_l = 3
TH_h = 13
nms_th[nms >= TH_h] = 2
nms_th[np.bitwise_and(TH_l <= nms, nms < TH_h)] = 1

px.imshow(nms_th, title="double TH")

# %% [markdown]
# ## Iterative hysteresis
# We will do the iterative process with connected components (CC):
# 1. Take a mask of combined weak and strong edges and run CC algorithm on it.
# 2. For each such CC group- test if there is intersection with ONLY strong edges mask.
# 3. If intersection exist, then weak edges in CC group is actually strong edges, so unite the masks.

# %%

nms_weak_and_strong = np.zeros(nms_th.shape, dtype=bool)
nms_strong = np.zeros(nms_th.shape, dtype=bool)

nms_weak_and_strong[nms_th > 0] = 1
nms_strong[nms_th == 2] = 1

num_w_s_CCs, w_s_CC_mask = cv2.connectedComponents(nms_weak_and_strong.astype(np.uint8))

# for each CC group of weak and strong edge mask
for w_s_CC_i in range(1, num_w_s_CCs):
    # get MASK of weak_and_strong edge from index w_s_CC_i
    w_s_CC_mask_i = np.zeros(nms_th.shape, dtype=bool)
    w_s_CC_mask_i[w_s_CC_mask == w_s_CC_i] = 1

    # if w_s_CC_mask_i has intersection with strong edges mask, add to strong edge mask
    if np.any(np.bitwise_and(w_s_CC_mask_i, nms_strong)):
        nms_strong = np.bitwise_or(w_s_CC_mask_i, nms_strong)

px.imshow(nms_strong, title="Canny final result")

# %% [markdown]
# ## cv2 Canny
# let's see the results from the default canny of cv2
# %%
res = cv2.Canny(img.astype(np.uint8), 105, 120)
px.imshow(res, title="cv2.Canny final result")
