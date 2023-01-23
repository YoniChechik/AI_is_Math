# Histogram equalization
Histogram equalization is a method used in image processing to enhance the contrast of an image. This is achieved by mapping the intensity values of the input image to new values in such a way that the output image has a uniform distribution of intensities. This is done by first calculating the histogram of the input image, which is a graph showing the number of pixels in the image with each intensity value. The histogram is then used to compute a cumulative distribution function (CDF) of the intensity values, which is a function that maps the intensity values to their corresponding cumulative probabilities.

The CDF is then used to map the intensity values in the input image to new intensity values in the output image. The new intensity values are chosen such that the output image has a uniform distribution of intensity values. This is done by choosing the new intensity values such that the CDF of the output image is a linear function.

Mathematically, the histogram equalization process can be described as follows. Let $I$ be the input image, with intensity values $i \in {0, 1, \dots, L-1}$, where $L$ is the number of possible intensity values. Let $H(i)$ be the histogram of the input image, which is a function that gives the number of pixels in the image with intensity value $i$. The CDF of the intensity values is given by:

$$F(i) = \sum_{j=0}^{i} H(j)$$

The new intensity values in the output image, $I'$, are given by:

$$I'(x,y) = \lfloor L \times F(I(x,y)) \rfloor$$

where $(x,y)$ are the coordinates of a pixel in the image, and $\lfloor \cdot \rfloor$ is the floor function, which rounds down to the nearest integer.

Histogram equalization can be used to improve the contrast of an image, making it easier to see details in the image that may not be visible with the original intensity values. It is especially useful for images with low contrast, or images with a non-uniform distribution of intensity values.