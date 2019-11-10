# pip uninstall opencv-python
# pip install -U opencv-contrib-python==3.4.0.12


#https://towardsdatascience.com/image-stitching-using-opencv-817779c86a83

import cv2
import numpy as np
import matplotlib.pyplot as plt
from random import randrange

rgb1 = cv2.cvtColor(cv2.imread("right.JPG"),cv2.COLOR_BGR2RGB)
gray1 = cv2.cvtColor(rgb1,cv2.COLOR_RGB2GRAY)
rgb2 = cv2.cvtColor(cv2.imread("left.JPG"),cv2.COLOR_BGR2RGB)
gray2 = cv2.cvtColor(rgb2,cv2.COLOR_RGB2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(gray1,None)
kp2, des2 = sift.detectAndCompute(gray2,None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m in matches:
    if m[0].distance < 0.5*m[1].distance:
        good.append(m)
matches = np.asarray(good)

# show only 30 matches
im_matches = cv2.drawMatchesKnn(rgb1,kp1,rgb2,kp2,good[0:30],None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(im_matches)
plt.show()

test=cv2.drawKeypoints(rgb1,kp1,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(test)
plt.show()


src = np.float32([ kp1[m.queryIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
dst = np.float32([ kp2[m.trainIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)

# dst = cv2.warpPerspective(rgb1,H,(rgb2.shape[1] + rgb1.shape[1], rgb1.shape[0]+rgb2.shape[0]))
# dst[0:rgb2.shape[0], 0:rgb2.shape[1]] = rgb2

print(H)

# plt.figure()
# plt.imshow(dst)
# plt.show()

def warpTwoImages(img1, img2, H):
    '''warp img2 to img1 with homograph H
    from: https://stackoverflow.com/questions/13063201/how-to-show-the-whole-image-when-using-opencv-warpperspective
    '''
    h1,w1 = img1.shape[:2]
    h2,w2 = img2.shape[:2]
    pts1 = np.float32([[0,0],[0,h1],[w1,h1],[w1,0]]).reshape(-1,1,2)
    pts2 = np.float32([[0,0],[0,h2],[w2,h2],[w2,0]]).reshape(-1,1,2)
    pts2_ = cv2.perspectiveTransform(pts2, H)
    pts = np.concatenate((pts1, pts2_), axis=0)
    [xmin, ymin] = np.int32(pts.min(axis=0).ravel() - 0.5)
    [xmax, ymax] = np.int32(pts.max(axis=0).ravel() + 0.5)
    t = [-xmin,-ymin]
    Ht = np.array([[1,0,t[0]],[0,1,t[1]],[0,0,1]]) # translate

    result = cv2.warpPerspective(img2, Ht@H, (xmax-xmin, ymax-ymin))
    result[t[1]:h1+t[1],t[0]:w1+t[0]] = img1
    return result

result = warpTwoImages(rgb2, rgb1, H)

plt.figure()
plt.imshow(result)
plt.show()