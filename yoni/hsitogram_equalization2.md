We are writing lecture notes for my computer vision course. Write lecture notes with math notations in latex format. Here are some points that needs to be expanded:
Histogram equalization is a method in image processing of contrast adjustment using the image's histogram.
This method is used to increase the global contrast of an image and is useful in images with backgrounds and foregrounds that are both bright or both dark. 
Histogram equalization accomplishes this by effectively spreading out the most frequent intensity values.
Lecture Notes:

Histogram equalization is a method in image processing that is used to adjust the contrast of an image by modifying its histogram. The goal of histogram equalization is to increase the global contrast of an image, making it more visually appealing and easier to interpret.

The basic idea behind histogram equalization is to stretch the image's histogram such that it spans the entire range of possible intensity values. This is accomplished by effectively spreading out the most frequent intensity values.

The process of histogram equalization can be mathematically represented as follows:

Compute the histogram of the image, $H(i)$, which gives the number of pixels with intensity value $i$.

Compute the cumulative distribution function (CDF) of the histogram, $F(i)$, which gives the probability that a pixel has an intensity less than or equal to $i$.

Transform the intensity values of the image, $f(i,j)$, according to the following formula:

$g(i,j) = T(f(i,j)) = F(f(i,j)) * L - 1$

where $L$ is the total number of intensity levels in the image.

The output image, $g(i,j)$, will have a histogram that is approximately flat, with the intensity values spread out evenly across the entire range of possible values.

Histogram equalization is particularly useful in images with backgrounds and foregrounds that are both bright or both dark. In such images, the histogram is often concentrated in the middle intensity values, resulting in a low contrast image. By spreading out the most frequent intensity values, histogram equalization increases the global contrast of the image, making it more visually appealing and easier to interpret.