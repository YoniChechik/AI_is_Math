We are writing lecture notes for my computer vision course. Write lecture notes with math notations in latex format. Here are some points that needs to be expanded:
gamma correction for image enhancments.

Lecture Notes:

Gamma correction is a technique used to adjust the brightness and contrast of an image. It is based on the non-linear relationship between the perceived brightness of an image and the intensity values of its pixels.

The human visual system perceives the brightness of an image in a non-linear way, with small changes in intensity values resulting in large changes in perceived brightness at low levels, and small changes in perceived brightness at high levels. Gamma correction is used to correct this non-linearity, by adjusting the intensity values of the pixels in an image to match the non-linear perception of brightness.

Gamma correction can be applied to an image by performing a non-linear transformation on its intensity values. The most common form of this transformation is the power law function:

$g(i,j,k) = c * (f(i,j,k))^{\gamma}$

where $f(i,j,k)$ is the input pixel value at position $(i,j)$ of the $k^{th}$ color channel $(k \in {0,1,2}$ for R,G,B respectively), $g(i,j,k)$ is the output pixel value after gamma correction, $c$ is a constant that controls the overall brightness of the image, and $\gamma$ is the gamma correction value.

A value of $\gamma>1$ will result in an image with increased brightness and increased contrast, while




Yoni Chechik
continue
A value of $\gamma<1$ will result in an image with decreased brightness and decreased contrast.

Gamma correction can be used to enhance images that appear too dark or too bright, or to improve the visibility of details in images with a narrow contrast range. It is commonly used in image processing applications such as video displays, digital cameras, and image editing software.

It's worth noting that the gamma correction can be achieved by using the function $g(i,j,k) = c * (f(i,j,k))^{1/\gamma}$ too where $\gamma$ is the gamma correction value.

In summary, gamma correction is a technique used to adjust the brightness and contrast of an image by performing a non-linear transformation on its intensity values. It is based on the non-linear relationship between the perceived brightness of an image and the intensity values of its pixels, and can be used to enhance images that appear too dark or too bright, or to improve the visibility of details in images with a narrow contrast range.