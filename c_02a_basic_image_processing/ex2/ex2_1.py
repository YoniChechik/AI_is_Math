# EX2_1
# build dilate and erode functions
import matplotlib.pyplot as plt
import numpy as np

figsize = (10, 10)


img = np.zeros((50, 50))
img[20:30, 20:30] = 1

plt.figure(figsize=figsize)
plt.imshow(img, cmap="gray")
plt.show()

kernel = np.zeros((5, 5), dtype=np.uint8)
kernel[2, :] = 1
kernel[:, 2] = 1


plt.figure(figsize=figsize)
plt.imshow(kernel, cmap="gray")
plt.show()


def my_dilate(img, kernel):
    # TODO: build dilate function without cv2.dilate
    pass


plt.figure(figsize=figsize)
plt.imshow(my_dilate(img, kernel), cmap="gray")
plt.show()

# TODO: show that cv2.dilate and my_dilate are the same using absolute difference
if ...:
    print("cv2.dilate & my_dilate are the same!")
else:
    print("try again...")


def my_erode(img, kernel):
    # TODO: build erode function without cv2.erode
    pass


plt.figure(figsize=figsize)
plt.imshow(my_erode(img, kernel), cmap="gray")
plt.show()

# TODO: show that cv2.erode and my_erode are the same using absolute difference
if ...:
    print("cv2.erode & my_erode are the same!")
else:
    print("try again...")
