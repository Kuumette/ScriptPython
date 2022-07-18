import sys
import numpy as np
import os
import cv2
from astropy.io import fits

from PIL import Image
from skimage.exposure import rescale_intensity

path = "C:\\Users\\Ballatore\\Desktop\\testImage\\data\\"
dir_list = os.listdir(path) 

print(dir_list)

for fit in dir_list:

    fitsfilename = path + '/' + fit
        
    d = fits.open(fitsfilename)[0].data
    print(len(d))
  
    p0,p99 = np.percentile(d,(10,99))

    a = rescale_intensity(d, in_range=(p0, p99))

    image = Image.fromarray(a)
    print(image)
    imagename = fitsfilename.replace('.fits', '.png')
 
    image.save(imagename)



