# %% [markdown]
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

# The simple approach:
# Getting a calibration image of a white wall and then simply divide this calib_im with each raw image to get a fixed image.
# The problem:
# Not enough memory in the camera to save multiple calib images per each lens configuration.
#
# The New process the we propose is as follows:
# 1. For each new lens the end-user wants to use, he will shoot one calibration image of a white wall.
# 2. Calibration params are saved for this lens configuration.
# 3. The user can now work with this lens configuration and the vignetting will be corrected for all images.

# Behind the scenes we need to build 3 functions:
# 1. `get_index_matrix()` that returns the
# index matrix (called `X` in our lesson). We will build this in python but our engineers will convert it to ASIC,
# so this function CAN'T change.
# 2. `get_calib_coeffs(calib_map)` that gets a raw image of the white wall and returns the betta vector (the calibration params).
# 3. `fix_raw_im(b, vig_im)` that gets the user image and the betta vector and fixes the image vignetting.
# It reconstruct the calib image input from (2) using (1) + betta vector and then divide the input image with this reconstructed calib_map to get a fixed image.

# %%
# to run in google colab
import sys

if "google.colab" in sys.modules:
    import subprocess

    subprocess.call("apt-get install subversion".split())
    subprocess.call(
        "svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_04a_curve_fitting/ex4a/calib_im1.jpg".split()
    )
    subprocess.call(
        "svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_04a_curve_fitting/ex4a/calib_im2.jpg".split()
    )
    subprocess.call(
        "svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_04a_curve_fitting/ex4a/calib_im3.jpg".split()
    )
    subprocess.call(
        "svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_04a_curve_fitting/ex4a/vignette_im1.jpg".split()
    )
    subprocess.call(
        "svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_04a_curve_fitting/ex4a/vignette_im2.jpg".split()
    )
    subprocess.call(
        "svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_04a_curve_fitting/ex4a/vignette_im3.jpg".split()
    )

# %%
import cv2
import matplotlib.pyplot as plt
import numpy as np

IMAGE_SHAPE = [768, 1366]


# %%
def get_index_matrix():

    # TODO: get x,y index for each pixel as column vectors
    # HINT: use np.meshgrid() + reshape
    pass
    x = None
    y = None

    # X is the raw dataset from which we will reconstruct the calib map
    # X@b = calib_map
    # TODO: build X using x,y and function of them
    # hint: use np.concatenate()
    # hint2: the calibration map looks radial- so to build a good representation of it we need to use x,y but also x^2, y^2 and even xy.
    # this is only one line, but a hard one
    X = None
    return X


# %%
def get_calib_coeffs(calib_map):
    # This is the calibration function when he user switches lenses.
    # Since it's memory consuming to save the intire calib map,
    # we will save only a parametric representation of it using X,b

    # TODO: transform calib_map to column vector for least-squares
    # one line
    y = None

    # build X
    X = get_index_matrix()

    # TODO: use least-squares to find the beta params for later use.
    # one line
    b = None

    return b


# %%


def fix_raw_im(b, vig_im):
    # Each image taken is passed through this block to correct for vignetting

    # build data matrix X
    X = get_index_matrix()

    # TODO: build reconstructed calib map using b params from calibration step
    # use X,b (this is the LS part!!!)
    # one line
    reconstructed_calib_im_column_vector = None
    # reshape into 2d image
    # build 3 copies of the 2d result and concat along the third dim, in order to divide with RGB images
    pass

    # TODO: divide the reconstructed calib image with the input image to get the fixed result
    # one line
    res = None

    # return the final result + rec_calib_map for debug and testing purposes.
    return res, rec_calib_map


# %%
def calib_testing(calib_map, rec_calib_map):
    # test your calib map reconstruction relative to the original
    # calib map
    # this is just for testing in the lab, not for the end user...

    # TODO:what is the RMSE of the reconstruction?
    # one line
    rmse = None

    # TODO: print L1 map of reconstruction
    # one line
    abs_error_map = None

    plt.figure()
    plt.imshow(abs_error_map)
    plt.colorbar()
    plt.title("rmse error is " + str(rmse) + ". L1 map:")
    plt.show()


# %%
if __name__ is "__main__":
    for i in range(3):
        calib_im = cv2.imread("calib_im" + str(i + 1) + ".jpg")
        calib_im = cv2.cvtColor(calib_im, cv2.COLOR_BGR2GRAY)
        calib_map = calib_im.astype(float) / 255

        vig_im = cv2.imread("vignette_im" + str(i + 1) + ".jpg")
        vig_im = cv2.cvtColor(vig_im, cv2.COLOR_BGR2RGB)

        # ===== happens in the factory per lens setup
        b = get_calib_coeffs(calib_map)

        # ===== b is then saved to the camera hardware coupled to the lens configuration.
        # so to fix the problem one must use b on the raw image each time he takes a photo:
        res, rec_calib_map = fix_raw_im(b, vig_im)

        # ===== plot results
        plt.figure()
        plt.imshow(vig_im)
        plt.title("original image")
        plt.show()

        plt.figure()
        plt.imshow(res)
        plt.title("fixed image")
        plt.show()

        calib_testing(calib_map, rec_calib_map)

# %%
