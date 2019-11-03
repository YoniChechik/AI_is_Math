import numpy as np
import cv2
import matplotlib.pyplot as plt
from aux_funcs import *

# https://www.youtube.com/watch?v=YcAoqeOOrzA
cap = cv2.VideoCapture(r'C:\Users\jonathanch\Google Drive\cv_course\Dashcam on the freeway....mp4')
# switching lanes
cap.set(cv2.CAP_PROP_POS_MSEC,100000)
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
while(cap.isOpened()):
    frame = cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2GRAY)
    frame = frame[380:575,:]
    # bokeh_imshow(frame)


    # plt.figure()
    # plt.imshow(frame)
    # plt.show()
    frame_only_white = frame.copy()
    frame_only_white[frame<150]=0
    # bokeh_imshow(frame)

    frame_canny = cv2.Canny(frame_only_white.astype(np.uint8),105,120)
    res = np.concatenate((frame,frame_only_white,frame_canny),axis=0)

    # bokeh_imshow(res)
    cv2.imshow('frame',res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()