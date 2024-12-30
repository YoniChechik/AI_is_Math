# # Image to chars
# We want to represent images with chars to get a cool matrix effect
#
# All data that we are working on can be found here: https://github.com/YoniChechik/AI_is_Math

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont

im_bgr = cv2.imread("image_to_chars/matrix.jpg")
im_rgb = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2RGB)

plt.imshow(im_rgb)
plt.title("Wanted result style")
plt.show()

# Let's read an image to start and experiment on
im_bgr = cv2.imread("image_to_chars/person.jpg")
im_rgb = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2RGB)

plt.imshow(im_rgb)
plt.title("original image")
plt.show()

# Start with 2 functions to convert chars to pixel array representation
# You don't really need to understand it, we simply copy it from the web...


def max_char_window_size(char_list, font_path, fontsize):
    font = ImageFont.truetype(font_path, fontsize)
    max_w = max_h = 0
    for c in char_list:
        _, _, w, h = font.getbbox(c)
        if w > max_w:
            max_w = w
        if h > max_h:
            max_h = h
    return max_w, max_h


def char_to_pixels(text, window_size_wh, font_path, fontsize):
    """
    Based on https://stackoverflow.com/a/36386628/4879610

    """
    font = ImageFont.truetype(font_path, fontsize)
    image = Image.new("L", window_size_wh, 1)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font)
    arr = np.asarray(image)
    arr = arr == 0
    return arr


# Next we will build the chars we want to use for the image representation.
# download the font from here: https://github.com/YoniChechik/AI_is_Math/tree/master/other_tutorials
FONT_PATH = "image_to_chars/whitrabt.ttf"
FONT_SIZE = 14
REPRESENTATION_CHARS = [" ", ".", ":", "+", "*", "e", "$", "@"]

window_size_wh = max_char_window_size(REPRESENTATION_CHARS, FONT_PATH, FONT_SIZE)

char_pix_list = []
for c in REPRESENTATION_CHARS:
    char_pix_list.append(char_to_pixels(c, window_size_wh, FONT_PATH, FONT_SIZE))


def display(arr):
    result = np.where(arr, "#", " ")
    print("\n".join(["".join(row) for row in result]))


for c, c_pix in zip(REPRESENTATION_CHARS, char_pix_list):
    print(c)
    display(c_pix)

# This is the tricky part...
# Each small block of the image should be represented as the closest char from our list.
# By doing decimation on the graylevel image we can get the *mean intensity of the block*,
# and then we can convert it to a char that corresponds to this intensity.
w = window_size_wh[0]
h = window_size_wh[1]

im_gray = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2GRAY)
im_resize = cv2.resize(im_gray, (im_gray.shape[1] // w, im_gray.shape[0] // h))

plt.imshow(im_resize)
plt.colorbar()
plt.title("resized gray image")
plt.show()

# Each block now has a corresponding number to our `REPRESENTATION_CHARS`
# LUT = look-up table
quantization_step = 256 / len(REPRESENTATION_CHARS)
im_lut = np.floor(im_resize / quantization_step).astype(int)

plt.imshow(im_lut)
plt.colorbar()
plt.title("LUT representation of the image")
plt.show()

# Now simply build a new image block by block from our `im_lut`
res = np.zeros((im_lut.shape[0] * h, im_lut.shape[1] * w))

for col in range(im_lut.shape[0]):
    for row in range(im_lut.shape[1]):
        res[col * h : col * h + h, row * w : row * w + w] = char_pix_list[im_lut[col, row]]

plt.imshow(res)
plt.title("Final result")
plt.show()


# Building our entire code as a function and running it on a video stream.
# (This will not work in google colab, only in your own computer with a camera)
def im_to_chars(im_bgr, char_pix_list, window_size_wh):
    w = window_size_wh[0]
    h = window_size_wh[1]

    im_gray = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2GRAY)
    im_resize = cv2.resize(im_gray, (im_gray.shape[1] // w, im_gray.shape[0] // h))

    quantization_step = 256 / len(REPRESENTATION_CHARS)
    im_lut = np.floor(im_resize / quantization_step).astype(int)

    res = np.zeros((im_lut.shape[0] * h, im_lut.shape[1] * w))

    for col in range(im_lut.shape[0]):
        for row in range(im_lut.shape[1]):
            res[col * h : col * h + h, row * w : row * w + w] = char_pix_list[im_lut[col, row]]

    return res


cap = cv2.VideoCapture(0)

# Check if camera was opened correctly
if not (cap.isOpened()):
    print("Could not open video device")

# Set the resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# Capture frame-by-frame
while True:
    ret, frame = cap.read()

    # Display the resulting frame
    res = im_to_chars(frame, char_pix_list, window_size_wh)

    cv2.imshow("preview", res)
    cv2.imshow("im", frame)

    # Waits for a user input to quit the application
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
