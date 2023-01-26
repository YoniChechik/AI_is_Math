onvolution is a mathematical operation that is widely used in image processing and computer vision. It is used to apply a filter to an image, which can be used for various tasks such as image smoothing, edge detection, and feature extraction.

The convolution operation is defined as the integral of the product of two functions, where one function is the image and the other is the filter kernel. Mathematically, it can be represented as:

 

Where $f(x,y)$ is the image, $g(x,y)$ is the filter kernel, and $(f*g)(x,y)$ is the convolution result.

In digital image processing, the continuous integral is replaced with a discrete sum, resulting in a discrete convolution:

(f*g)(x,y) = $\sum_{m=-\infty}^{\infty} \sum_{n=-\infty}^{\infty} f(m,n)g(x-m,y-n)$

Convolution can be implemented using different techniques such as full convolution, same convolution, and valid convolution. Full convolution pads the image with zeros, same convolution pads the image with the same values, and valid convolution doesn't pad the image.

Convolution is a powerful technique and is widely used in various computer vision tasks such as image classification, object detection, and semantic segmentation.

===============
gaussian filter
A Gaussian filter is a kind of blur filter used in image processing. It is defined by its size and standard deviation (STD). The filter is designed to blur the image by averaging the pixels within the kernel. The kernel is a discrete representation of a Gaussian function, where the bins correspond to the wanted kernel size. Since the Gaussian function is infinite, the kernel is truncated at a certain point, usually at 2-3 standard deviations. This is done to reduce computation time.

The Gaussian filter is particularly effective in reducing Gaussian noise, which is an additive noise that can appear in images due to system electrical circuitry. However, it is not as effective in reducing other types of noise, such as salt and pepper noise. The mean filter is another filter commonly used for this purpose.

===========
median
ecture Notes:

Median Filter

A median filter is a non-linear digital filtering technique that is used to remove noise from an image.
It works by taking the median value from a set of neighboring pixels. For example, if the neighborhood pixels are [1, 0, 100], the median value would be 1.
Median filter is good against salt and pepper noise and against Gaussian noise (but not as effective as a gaussian filter).
Median filter can be considered as a blur filter, but it also has edge preserving properties.
The median filter is more computationally expensive than mean or gaussian filters.
The median filter is not a linear time-invariant (LTI) system because it is not linear on some weights.
Mathematically, the median filter can be represented as:

$output(i,j)=median(p1,p2,…,pn)$

Where $output(i,j)$ is the output pixel at position (i,j), and $p_1,p_2,…,p_n$ are the neighborhood pixels around position (i,j).




