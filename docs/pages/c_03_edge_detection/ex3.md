---
title: Edge detection
subtitle: Ex3
bigimg: /pages/c_03_edge_detection/c_03_bigimg.jpg
layout: page
---

# EX3: Bilateral filter

Ordinary smoothing of an image impact the edges and make them less sharp.
The bilateral filter is a filter that is considered "edge-aware":
If regular smoothing is done by taking all neighbooring pixels and suming them with weights only dependent by the distance from the chosen pixel (spatial kernel), in the bilateral filter the weight is also determined by the **distance of the intensities** of each neighbooring pixel (range kernel).

With the range dependance, nighbooring pixels that are far in the intensity values, will be less important in the weighting.

Let's look at the math (modified from Wikipedia):

$I^\text{filtered}(x) = \frac{\sum_{x_i \in \Omega_x} I(x)w_p(x,x_i)}{\sum_{x_i \in \Omega_x} w_p(x,x_i)}$

and:

$$w_p(x,x_i) = g_s(\|x_i - x\|)f_r(\|I(x_i) - I(x)\|)$$

where:

- $I^\text{filtered}$ is the filtered image;
- $I$ is the original input image to be filtered;
- $x$ are the coordinates of the current pixel to be filtered;
- $\Omega_x$ is the neighboorhood of $x$.
- $f_r$ is the range kernel for smoothing differences in intensities.
- $g_s$ is the spatial (or domain) kernel for smoothing differences in coordinates.

Let's write it in 2D image form, where $f_r$ and $g_s$ are gaussian functions:

$I^{filtered}(x, y) = \frac{\sum_{i, j} I(i, j) w_p(x, y, i, j)}{\sum_{i, j} w_p(x, y, i, j)}$

where: 

$w_p(x, y, i, j) = \exp\left(-\frac{(x-i)^2 + (y-j)^2}{2 \sigma_d^2}\right)\cdot  \exp\left(- \frac{\|I(x, y) - I(i, j)\|^2}{2 \sigma_r^2}\right)$


This is an Image showing the full filter on one pixel input (the normalization.
(In the most right, the half transparent image is the result of applying the filter to all of the pixels).
A regular gaussian (spatial) filter would have resulted in a slop connecting the to planes, but the bilateral filter has better results!


![](images/2019-09-25-18-10-03.png)
