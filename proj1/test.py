import numpy as np
import cv2
import matplotlib.pyplot as plt
from aux_funcs import *

cap = cv2.VideoCapture(r'C:\Users\jonathanch\Downloads\Dashcam on the freeway....mp4')
cap.set(cv2.CAP_PROP_POS_MSEC,30000)
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# while(cap.isOpened()):
frame = cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2GRAY)
frame = frame[380:575,:]
# cv2.imshow('frame',frame)
# if cv2.waitKey(1) & 0xFF == ord('q'):
#     break
# plt.figure()
# plt.imshow(frame)
# plt.show()
frame = frame>150
bokeh_imshow(frame)

cap.release()
cv2.destroyAllWindows()