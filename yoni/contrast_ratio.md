We are writing lecture notes for my computer vision course. Write lecture notes with math notations in latex format. Here are some points that needs to be expanded:
Contrast in visual perception is the difference in appearance of two or more parts of a seen field.
The human visual system is more sensitive to contrast than absolute luminance; 
Contrast ratio, or dynamic range, is the ratio between the largest and smallest values of the image.
Lecture Notes:

Contrast in visual perception refers to the difference in appearance of two or more parts of a seen field. It is a fundamental concept in computer vision and image processing, as it is closely related to the visibility and interpretability of an image.

The human visual system is more sensitive to contrast than absolute luminance. This means that an image with a high contrast ratio will be perceived as more visually appealing and easier to interpret than an image with a low contrast ratio, even if the latter has a higher absolute luminance.

The contrast ratio, also known as dynamic range, is a quantitative measure of the contrast in an image. It is defined as the ratio between the largest and smallest values of the image. Mathematically, the contrast ratio of an image can be represented as:

$CR = \frac{\max(g(i,j,k))}{\min(g(i,j,k))}$

where $g(i,j,k)$ is the value of the pixel at position $(i,j)$ of the $k^{th}$ color channel $(k \in {0,1,2}$ for R,G,B respectively) of the input image.

A high contrast ratio indicates that the image has a wide range of intensity values, while a low contrast ratio indicates that the image has a narrow range of intensity values. For example, an image with a contrast ratio of 100:1 has a much wider range of intensity values than