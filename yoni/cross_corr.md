# Cross Correlation in Image Processing
Cross correlation is a mathematical operation that is widely used in image processing to compare two images or image patches. It is a measure of similarity between two images, and is often used in applications such as image registration, object detection, and pattern recognition.

## Mathematical Formulation
The mathematical formula for cross correlation is given by:

$$ C_{xy} = \sum_{i=-\infty}^{\infty} \sum_{j=-\infty}^{\infty} f(i,j) \cdot g(i+x,j+y) $$

where $C_{xy}$ is the cross correlation at a displacement of $(x,y)$, $f$ is the first image or image patch, and $g$ is the second image or image patch.

## Zero Mean Cross Correlation
One common variation of the cross correlation operation is zero mean cross correlation, which is obtained by subtracting the mean of the images or image patches from their values before computing the cross correlation. This has the effect of removing the average intensity from the images, which can be useful for comparing images with different mean intensities.

The mathematical formula for zero mean cross correlation is given by:

$$ C_{xy} = \sum_{i=-\infty}^{\infty} \sum_{j=-\infty}^{\infty} (f(i,j) - \mu_f) \cdot (g(i+x,j+y) - \mu_g) $$

where $\mu_f$ and $\mu_g$ are the means of the image patches $f$ and $g$, respectively.

## Zero Mean Normalized Cross Correlation
Zero mean normalized cross correlation (ZNCC) is a variant of cross correlation that is commonly used in computer vision applications. It is a measure of similarity between two images or image patches that accounts for differences in mean and variance.

The mathematical formula for ZNCC is given by:

$$ ZNCC_{xy} = \frac{\sum_{i=-\infty}^{\infty} \sum_{j=-\infty}^{\infty} (f(i,j) - \mu_f) \cdot (g(i+x,j+y) - \mu_g)}{\sqrt{\sum_{i=-\infty}^{\infty} \sum_{j=-\infty}^{\infty} (f(i,j) - \mu_f)^2} \cdot \sqrt{\sum_{i=-\infty}^{\infty} \sum_{j=-\infty}^{\infty} (g(i+x,j+y) - \mu_g)^2}} $$

where $ZNCC_{xy}$ is the ZNCC at a displacement of $(x,y)$, $f$ is the first image or image patch, $g$ is the second image or image patch, $\mu_f$ is the mean of $f$, and $\mu_g$ is the mean of $g$.

ZNCC has several advantages over other algorithms that are used to compare images or image patches. One of the main advantages is that it is robust to differences in mean and variance between the two images. This is particularly useful in applications where the images may have different lighting conditions or contrast levels.

# Summary
Cross correlation, zero mean cross correlation, and ZNCC are all mathematical operations used in image processing to compare two images or image patches. Cross correlation measures the similarity between the two images, but does not account for differences in mean and variance. Zero mean cross correlation adjusts for differences in mean, but not variance. ZNCC, on the other hand, accounts for both differences in mean and variance, making it a more robust measure of similarity. ZNCC is also symmetric, computationally efficient, and easy to implement, making it a popular choice in many computer vision applications.