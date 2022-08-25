import matplotlib.pyplot as plt
from matplotlib import image
import numpy as np
from PIL import Image
import cv2 as cv
import imageio

z = imageio.imread('033.jpg')  
z = z[:,:,1]

zimg = plt.imshow(z,cmap="gray")


x = np.linspace(-10, 10, 1024)
y = np.linspace(-10, 10, 1024)
x, y = np.meshgrid(x, y)
x_0 = 0
y_0 = 0
mask = np.sqrt((x-x_0)**2+(y-y_0)**2)



r =9.5
for x in range(0,1023):
        for y in range(0,1023):
                if mask[x,y] < r:
                        mask[x,y] = 256
                elif mask[x,y] >= r:
                        mask[x,y] = 0

maskimg = plt.imshow(mask,cmap="gray")


z_masked = np.multiply(z,mask)

zimg_masked = plt.imshow(z_masked,cmap="gray")

imageio.imsave("023.jpg", z_masked)
