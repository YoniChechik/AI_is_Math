#%% [markdown]
# # EX4a: Vignetting 
# In photography and optics, vignetting is a reduction of an 
# image's brightness or saturation toward the periphery compared 
# to the image center.
#
# Mechanical vignetting (for example) occurs when light beams emanating from 
# object points located off-axis are partially blocked by 
# external objects such as thick or stacked filters, secondary 
# lenses, and improper lens hoods. [Wikipedia]
# 
# Read more about it here:

# https://en.wikipedia.org/wiki/Vignetting

# https://photographylife.com/what-is-vignetting
#
# You are an algorithm engineer in a new cutting-edge camera 
# startup with a new problem of automatically correct vignetting problems.
# The team wants to correct the vignetting problem no metter what other lenses
# or lens hoods the user is putting on the camera.
# 
# Each time the user switches to a new setup, he needs to calibrate the camera
# by shooting a white wall (calib_im*.jpg).
# The method you came up with is using least-squares to correct the image
# from the given calibration map, by taking the beta params (least squares params)
# and applying it back to each shot image later.
#
# %%
# to run in google colab
import sys
if 'google.colab' in sys.modules:
    import subprocess 
    subprocess.call('apt-get install subversion'.split())
    subprocess.call('svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_04a_curve_fitting/ex4a/calib_im1.jpg'.split())
    subprocess.call('svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_04a_curve_fitting/ex4a/calib_im2.jpg'.split())
    subprocess.call('svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_04a_curve_fitting/ex4a/calib_im3.jpg'.split())
    subprocess.call('svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_04a_curve_fitting/ex4a/vignette_im1.jpg'.split())
    subprocess.call('svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_04a_curve_fitting/ex4a/vignette_im2.jpg'.split())
    subprocess.call('svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_04a_curve_fitting/ex4a/vignette_im3.jpg'.split())


# %%
import numpy as np
import matplotlib.pyplot as plt
import cv2

figsize = (10, 10)

#%%
def build_A(im_shape):
    # building A from the indices of the image shape.
    # This is hard-coded block of code in the camera
    # that once out of the factory can't be changed.

    # TODO: get X,Y index for each pixel in a matrix:
    # use np.meshgrid()
    # ~ one line
    X, Y = None, None

    # TODO: transform to x,y column vectors
    x = None
    y = None
    
    # A is the raw dataset from which we will reconstruct the calib map
    # A@b = calib_map
    # TODO: build A using x,y and function of them
    # hint: use np.concatenate()
    # this is only one line, but a hard one
    A = None
    return A

#%%
def get_calib_coeffs(calib_map):
    # This is the calibration function when he user switches lenses.
    # Since it's memory consuming to save the intire calib map,
    # we will save only a parametric representation of it using A,b

    # TODO: transform calib_map to column veot for least-squares
    # one line
    z = None

    # build A
    A = build_A(calib_map.shape)

    # TODO: use least-squares to find the beta params for later use.
    # one line
    b = None

    return b

#%%

def fix_raw_im(b,vig_im):
    # Each image taken is passed through this block to correct for vignetting

    # build data matrix A
    im_shape_yx = (vig_im.shape[0],vig_im.shape[1])
    A = build_A(im_shape_yx)

    # TODO: build reconstructed calib map using b params from calibration step
    # use A,b (this is the LS part!!!)
    # one line
    rec1d = None

    # transform into 2d image
    rec_calib_map = rec1d.reshape(im_shape_yx)
    rec_calib_map_3d = np.transpose(np.tile(rec_calib_map,(3,1,1)),(1,2,0))

    # TODO: apply calib_map to image to get fixed result
    # one line
    res = None

    return res, rec_calib_map


#%% 
def calib_testing(calib_map,rec_calib_map):
    # test your calib map reconstruction relative to the original 
    # calib map
    # this is just for testing in the lab, not for the end user...

    # TODO:what is the RMSE of the reconstruction?
    # one line
    rmse = None

    # TODO: print L1 map of reconstruction
    # one line
    abs_error_map = None

    plt.figure(figsize=figsize)
    plt.imshow(abs_error_map)
    plt.colorbar()
    plt.title("rmse error is "+str(rmse)+". L1 map:") 
    plt.show()


#%%
if __name__ is "__main__":
    for i in range(3):
        calib_im = cv2.imread("calib_im"+str(i+1)+".jpg")
        calib_im = cv2.cvtColor(calib_im,cv2.COLOR_BGR2GRAY)
        calib_map = calib_im.astype(float)/255

        vig_im = cv2.imread("vignette_im"+str(i+1)+".jpg")
        vig_im = cv2.cvtColor(vig_im,cv2.COLOR_BGR2RGB)

        b = get_calib_coeffs(calib_map)
        res, rec_calib_map = fix_raw_im(b,vig_im)

        plt.figure(figsize=figsize)
        plt.imshow(vig_im)
        plt.title("original image")
        plt.show()

        plt.figure(figsize=figsize)
        plt.imshow(res)
        plt.title("fixed image")
        plt.show()

        calib_testing(calib_map,rec_calib_map)

#%%
