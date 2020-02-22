# %% [markdown]
# # Histogram equalization
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YoniChechik/AI_is_Math/blob/master/c_02_basic_image_processing/histogram_equalization.ipynb)

#%%
# to run in google colab
import sys
if 'google.colab' in sys.modules:
    import subprocess
    subprocess.call('apt-get install subversion'.split())
    subprocess.call('svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_02_basic_image_processing/Tour_Eiffel.jpg'.split())

#%%
import numpy as np
import matplotlib.pyplot as plt
import cv2
#%%
# read as grayscale
I = cv2.imread("Unequalized_Hawkes_Bay_NZ.jpg",0)
plt.imshow(I, cmap='gray', vmin=0, vmax=255)
#%%
bins_edges_min_max = [0,256]
num_bins=256
bin_count,bins_edges = np.histogram(I,num_bins,bins_edges_min_max)
bins_start = bins_edges[:-1]
#%%
def draw_hist(x_axis,input):
    fig,ax = plt.subplots()
    plt.bar(x_axis, input, width=input.shape[0]/(x_axis[-1]-x_axis[0]+1))
    return fig,ax

draw_hist(bins_start,bin_count)

# %%
pdf = bin_count/np.sum(bin_count)
draw_hist(bins_start,pdf)
# %%
cdf = np.cumsum(pdf)
plt.plot(cdf)

# %%
fig,ax = draw_hist(bins_start,pdf)
ax.plot(cdf*np.max(pdf),'r')

# %%
f_eq = np.round(cdf*255).astype(int)

f_eq
#%%
I_eq = f_eq[I]
plt.imshow(I_eq, cmap='gray', vmin=0, vmax=255)

# %%
bin_count,bins_edges = np.histogram(I_eq,num_bins,bins_edges_min_max)
bins_start = bins_edges[:-1]

draw_hist(bins_start,bin_count)

# %%
pdf = bin_count/np.sum(bin_count)
cdf = np.cumsum(pdf)
fig,ax = draw_hist(bins_start,pdf)
ax.plot(cdf*np.max(pdf),'r')

# %%
I_eq_cv2 = cv2.equalizeHist(I)
plt.imshow(I_eq_cv2, cmap='gray', vmin=0, vmax=255)


# %%
