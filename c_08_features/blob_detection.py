import numpy as np 
import matplotlib.pyplot as plt 
import cv2

# def log(s):
#     half_ker_sz = 3*s # should be bigger than sqrt(2)*s
#     X,Y = np.meshgrid(np.arange(-half_ker_sz,half_ker_sz),np.arange(-half_ker_sz,half_ker_sz))
    
#     coeff = 1/(np.pi*s**4)
#     alpha =(X**2+Y**2)/(2*s**2)
#     brackets = alpha -1
#     exp = np.exp(-alpha)

#     log = coeff*brackets*exp

#     return log

# def step(r):
#     # step = np.concatenate((np.zeros((2*sz,)),np.ones((sz,)),np.zeros((2*sz,))))
#     im_sz = 200
#     im = np.zeros((im_sz+1,im_sz+1,3))
#     im = cv2.circle(im, (int(im_sz/2), int(im_sz/2)), r, (255, 255, 255), -1)
#     return im

# plt.imshow(step(30))
# plt.show()
    
# plt.imshow(log(30))
# plt.show()

def log(s,x):
    # half_ker_sz = 3*s # should be bigger than sqrt(2)*s
    
    coeff = 1/(np.sqrt(2*np.pi)*s**3)
    alpha =(x**2)/(s**2)
    brackets = alpha -1
    exp = np.exp(-0.5*alpha)

    log = coeff*brackets*exp

    return log

sz = 100
step = np.concatenate((np.zeros((2*sz,)),np.ones((sz,)),np.zeros((2*sz,))))

# dx = 0.1
# x = np.arange(-half_ker_sz,half_ker_sz)

x = np.linspace(-100,100,)
#http://www.cim.mcgill.ca/~langer/558/2009/lecture11.pdf