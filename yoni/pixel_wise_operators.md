We are writing lecture notes for my computer vision course. Write lecture notes with math notations in latex format. Here are some points that needs to be expanded:
Pixel-wise operators, or point operators, are defined as such that each output pixel’s value depends on only the corresponding input pixel value.
Lecture Notes:

Pixel-wise operators, also known as point operators, are a type of image processing technique that operate on individual pixels of an image. The basic idea behind these operators is that the value of each output pixel depends only on the corresponding input pixel value.

Mathematically, a pixel-wise operator can be represented as a function $f$, where $f: R^{3} \rightarrow R^{3}$, with $f(i,j,k)$ as the output pixel value at position $(i,j)$ of the $k^{th}$ color channel $(k \in {0,1,2}$ for R,G,B respectively) of the output image, and $g(i,j,k)$ as the input pixel value at position $(i,j)$ of the $k^{th}$ color channel of the input image.

Some examples of pixel-wise operators include thresholding, where each pixel is set to a certain value based on whether it is above or below a threshold value, and contrast stretching, where the intensity values of each pixel are scaled to a new range of values. These operators are simple to implement and can be used as building blocks for more complex image processing operations.

In summary, pixel-wise operators are a type of image processing technique that operate on individual pixels of an image, where the output pixel value depends only on the corresponding input pixel value. They can be represented mathematically as a function and are used as building blocks for more complex image processing operations.