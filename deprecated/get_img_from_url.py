import os
import urllib.request
import cv2

def get_image_from_url(url):

    file_name = os.path.basename(url)
    urllib.request.urlretrieve(url, file_name)
    img = cv2.imread(file_name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img
